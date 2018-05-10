import Zdb


def get_relations(mal_id):
     return Zdb.get_json_result("SELECT DISTINCT * FROM AnimeEntries WHERE Id = ?", (mal_id,))
