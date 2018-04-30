from functools import wraps

import requests
from flask import Flask, render_template
from flask import request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from werkzeug.exceptions import BadRequest, abort

import AnimeRepository
import NotesRepository
import UserRepository
import WaifuRepository

app = Flask(__name__)

app.config['RATELIMIT_HEADERS_ENABLED'] = True
aud_public = "GOOGLE_LOGIN_GOES_HERE.com"
API_KEY = "APP_KEY_GOES_HERE"

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["10 per minute", "1 per second"],
)


# region decorators
def get_user_id_from_header(_request):
    return request.headers.get('UserToken') or None


def inject_token(view_function):
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        token = get_user_id_from_header(request)
        if token is not None and len(token) > 0:
            kwargs['user_token'] = get_user_id_from_header(requests)
            print("Token found: {}".format(token))
            return view_function(*args, **kwargs)

        print("Headers did not contain the user token")
        abort(401)

    return decorated_function


def requires_app_key(view_function):
    @wraps(view_function)
    def wrapper(*args, **kw):
        api_key = request.headers.get('APIKey') or None
        if api_key and api_key == API_KEY:
            print("valid api key...")
            return view_function(*args, **kw)
        else:
            print("Invalid APIKey given")
            abort(400)

    return wrapper


def valid_json(view_function):
    @wraps(view_function)
    def wrapper(*args, **kw):
        try:
            assert 0 < len(request.json) < 1000
        except BadRequest as e:
            print("Request must contain a json body that only has max 1000 items")
            abort(400)
        return view_function(*args, **kw)

    return wrapper


# endregion


@app.route("/relations/<int:anime_id>", methods=['GET'])
@limiter.limit("10/minute")
@requires_app_key
def better_relations(anime_id):
    return AnimeRepository.get_relations(anime_id)


# region Login
@app.route("/register", methods=['POST'])
@limiter.limit("10/day")
def register():
    id_token = request.values["id_token"]

    if id_token is None or len(id_token) < 20:
        print("[register] token was null or length was smaller than 20")
        return "Incorrect token provided <1>", 400

    # validate on Google's backend
    r = requests.get("https://www.googleapis.com/oauth2/v3/tokeninfo?id_token={0}".format(id_token))
    print(r.status_code)
    if r.status_code != 200:
        print("[register] Could not authorize with google. status code was {}".format(r.status_code))
        return "Incorrect status code <2>", 400

    # validate AUD
    valid_aud = r.json()["aud"] == aud_public
    if not valid_aud:
        print("[register] the aud wasn't the same")
        return "Incorrect request <3>", 400

    # retrieve user id
    google_user_id = r.json()["sub"]
    print(google_user_id)

    # check if already exists, if not create token. if it does, retrieve token
    try:
        token = UserRepository.get_user_token_by_google_id(google_user_id)
        if token and len(token) > 0:
            return token
    except Exception as e:
        print(e)

    token = UserRepository.create_new_user(google_user_id)
    if token is None:
        print("create_new_user failed, was null")
        return "Could not create an account <4>", 400

    return token, 200


@app.route("/authorized_user", methods=['GET'])
@limiter.limit("5/minute")
def authorized_user():
    token = request.values["token"]
    return render_template('authorized_user.html', token=token)


@app.route("/login", methods=['GET'])
@limiter.limit("5/minute")
def login():
    return render_template('login.html', endpoint=aud_public)


# endregion

# region Waifus

@app.route("/waifus", methods=['GET'])
@limiter.limit("10/minute")
@inject_token
@requires_app_key
def get_waifus_by_user_token(user_token):
    return WaifuRepository.get_waifus_by_token(user_token)


@app.route("/waifus/anime/<int:anime_id>", methods=['GET'])
@limiter.limit("10/minute")
@inject_token
@requires_app_key
def get_waifu_by_token_and_anime_id(anime_id, user_token):
    return WaifuRepository.get_waifus_by_token_and_anime_id(user_token, anime_id)


@app.route("/waifus/<int:waifu_id>", methods=['DELETE'])
@limiter.limit("5/second;30/minute;100/day")
@inject_token
@requires_app_key
def delete_waifu(waifu_id, user_token):
    try:
        WaifuRepository.delete_waifu(user_token, waifu_id)
        return "success", 200
    except Exception as e:
        print("Error in delete_waifu {}".format(str(e)))
        return "Could not delete the waifu...", 400


@app.route("/waifus", methods=['POST'])
@limiter.limit("5/second;30/minute;100/day")
@inject_token
@valid_json
@requires_app_key
def save_waifu(user_token):
    try:
        WaifuRepository.save_waifu(user_token, request.json)
        return "success", 200
    except Exception as e:
        print("Error in delete_waifu {}".format(str(e)))
        return "Could not delete the waifu...", 400


# endregion

# region Notes

@app.route("/notes", methods=['POST'])
@limiter.limit("3/second;30/minute;100/day")
@inject_token
@valid_json
@requires_app_key
def save_note(user_token):
    try:
        NotesRepository.create_note(user_token, request.json)
        return "success", 200
    except Exception as e:
        print("Error {}".format(e))
        return "Could not add note...", 400


@app.route("/notes/anime/<int:anime_id>", methods=['GET'])
@limiter.limit("10/minute")
@inject_token
@requires_app_key
def get_notes_by_anime_id(user_token, anime_id):
    return NotesRepository.get_notes_by_anime(user_token, anime_id)


# endregion


if __name__ == '__main__':
    app.run(debug=True, port=80)
