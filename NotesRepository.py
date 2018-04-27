import time

import Zdb


def create_note(user_token, json_body):
    Zdb.insert("REPLACE INTO UserEpisodeNotes(UserId, AnimeId, EpisodeNumber, Note, DateCreated) VALUES (?,?,?,?,?)",
               (user_token, json_body["AnimeId"], json_body["EpisodeNumber"], json_body["Note"][0:512],
                int(time.time())))


def get_notes_by_anime(user_token, anime_id):
    return Zdb.get_json_result(
        "SELECT AnimeId, EpisodeNumber, Note, DateCreated FROM UserEpisodeNotes WHERE AnimeId = ? AND UserId = ?",
        (anime_id, user_token))
