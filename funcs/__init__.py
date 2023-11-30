from config import Database as DB

from contextlib import contextmanager
from typing import Optional, Union

import requests
from pymysql import connect
from pymysql.cursors import DictCursor


def get_page(url: str = None, data: dict = None, method: str = 'GET') -> requests.Response | None:
    global res
    if url is None:
        return None

    if data is not None:
        if method == 'GET':
            res = requests.get(url, data=data)
        if method == 'POST':
            res = requests.post(url, data=data)
    else:
        if method == 'GET':
            res = requests.get(url)
        if method == 'POST':
            res = requests.post(url)
    if res.status_code == 200:
        return res
    else:
        return None


@contextmanager
def __get_conn() -> object:
    global conn
    conn = connect(
        host=DB.host,
        port=DB.port,
        user=DB.user,
        password=DB.password,
        db=DB.db,
        charset='utf8',
        cursorclass=DictCursor
    )
    try:
        yield conn
    finally:
        conn.close()


def query(sql: str = None, *args, commit: bool = False) -> Optional[Union[list[dict], bool]] | None:
    try:
        with __get_conn() as db_conn:
            with db_conn.cursor() as cur:
                if len(args) > 0:
                    cur.execute(sql, args)
                else:
                    cur.execute(sql)
                if commit:
                    db_conn.commit()
                    return True
                else:
                    res = cur.fetchall()
                    if len(res) > 0:
                        return res
                    else:
                        return None
    except Exception as e:
        print(f'DB>INIT>QUERY: {e}')
        return False
