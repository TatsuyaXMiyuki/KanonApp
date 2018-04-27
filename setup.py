import Zdb
import appconfig

with open(appconfig.SCHEMA_FILE) as fp:
    conn = Zdb.get_conn()
    with conn:
        conn.executescript(fp.read())

print("Done setting up the initial scheme!")
