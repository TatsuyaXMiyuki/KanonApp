import json
import sqlite3

import appconfig


# useful when bulk inserting
def get_conn(foreign_key_check=False, with_rows=False):
    conn = sqlite3.connect(appconfig.DATABASE_FILE)
    if foreign_key_check:
        conn.execute('pragma foreign_keys=ON')
    if with_rows:
        conn.row_factory = sqlite3.Row
    return conn


# useful when you want to insert just one thing
def insert(query, args=()):
    conn = get_insert_conn()
    with conn:
        conn.execute(query, args)


def get_insert_conn():
    return get_conn(foreign_key_check=True, with_rows=False)


def delete(query, args=()):
    conn = get_conn(foreign_key_check=True, with_rows=False)
    with conn:
        conn.execute(query, args)


def get_json_result(query, args=()):
    conn = get_conn(with_rows=True)
    with conn:
        cur = conn.execute(query, args)
        data = cur.fetchall()
        return json.dumps([dict(ix) for ix in data])


def get_simple_value(query, args=(), force_one=True):
    conn = get_conn(with_rows=False)
    with conn:
        cur = conn.execute(query, args)
        data = cur.fetchone()
        if force_one:
            return data[0]
        return data
