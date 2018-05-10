import Zdb


def get_relations(mal_id):
     return Zdb.get_json_result("SELECT DISTINCT * FROM AnimeEntries WHERE Id = ?", (mal_id,))


def get_ratings(shows):
    query = "SELECT * FROM AnimeRating WHERE AnimeId IN ({})".format(
        ','.join(['?'] * len(shows)))
    return Zdb.get_json_result(query, args=(*shows,))
