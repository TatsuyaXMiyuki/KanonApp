import time

import Zdb


def get_waifus_by_token(user_token):
    return Zdb.get_json_result(
        "SELECT WaifuId, AnimeId, WaifuName, ImageURL, DateCreated "
        "FROM UserWaifus "
        "WHERE UserId = ? "
        "ORDER BY DateCreated DESC", (user_token,))


def save_waifu(user_token, json_body):
    Zdb.insert("REPLACE INTO UserWaifus(UserId, WaifuId, AnimeId, WaifuName, ImageURL, DateCreated) "
               "VALUES(?,?,?,?,?,?)",
               (user_token, json_body["WaifuId"], json_body["AnimeId"], json_body["WaifuName"],
                json_body["ImageURL"], int(time.time()))
               )


def get_waifus_by_token_and_anime_id(user_token, anime_id):
    return Zdb.get_json_result(
        "SELECT WaifuId, AnimeId, WaifuName, ImageURL, DateCreated "
        "FROM UserWaifus "
        "WHERE UserId = ? AND AnimeId = ? "
        "ORDER BY DateCreated DESC",
        (user_token, anime_id))


def delete_waifu(user_id, waifu_id):
    Zdb.delete("DELETE FROM UserWaifus WHERE UserId = ? AND WaifuId = ?", (user_id, waifu_id))
