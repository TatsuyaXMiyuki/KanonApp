import time

from KanonApp import Zdb


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


def get_number_of_waifus(user_token):
    return Zdb.get_json_result("SELECT COUNT(*) AS UserWaifuCount "
                               "From UserWaifus "
                               "WHERE UserId = ?", (user_token,))


def get_top_waifus(number_of_waifus):
    max_number_of_waifus = 25
    if number_of_waifus > max_number_of_waifus:
        number_of_waifus = max_number_of_waifus

    return Zdb.get_json_result(
        "SELECT count(WaifuId) as TotalFavoriteCount, WaifuName, AnimeId, WaifuId, ImageURL "
        "FROM UserWaifus "
        "GROUP BY WaifuId "
        "ORDER BY TotalFavoriteCount DESC "
        "LIMIT ?", (number_of_waifus,))


def get_waifus_by_token_and_anime_id(user_token, anime_id):
    return Zdb.get_json_result(
        "SELECT WaifuId, AnimeId, WaifuName, ImageURL, DateCreated "
        "FROM UserWaifus "
        "WHERE UserId = ? AND AnimeId = ? "
        "ORDER BY DateCreated DESC",
        (user_token, anime_id))


def get_waifus_by_list_of_waifu_ids(user_token, list_of_waifu_ids):
    query = "SELECT WaifuId FROM UserWaifus WHERE UserId = ? AND WaifuId IN ({})".format(
        ','.join(['?'] * len(list_of_waifu_ids)))
    return Zdb.get_json_result(query, args=(user_token, *list_of_waifu_ids))


def delete_waifu(user_id, waifu_id):
    Zdb.delete("DELETE FROM UserWaifus WHERE UserId = ? AND WaifuId = ?", (user_id, waifu_id))
