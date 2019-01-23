# vim:fileencoding=utf-8

from __future__ import print_function, division

import os
import os.path
import sqlite3

from  ...util import *
from . import objects


def get_conn():
    """Creates db connection to be shared across the app."""

    if not os.path.exists(dbf_home):
        os.mkdir(dbf_home)

    conn = sqlite3.connect(opj(dbf_home,"mydb.db"), check_same_thread=False)

    return conn

def sanitize_db(ext_conn):
    """Creates missing tables."""
    c   = ext_conn.cursor()
    res = c.execute("SELECT name FROM sqlite_master WHERE type='table';")

    # list of database tables, and creator function
    tbl_list = {
                    "names":["objects"],
                    "crf": [
                        objects.create_objects_table
                    ]
               }


    tb_names = list([k[0] for k in res])
    for i, j in enumerate(tbl_list["names"]):
        if j not in tb_names:
            tbl_list["crf"][i](ext_conn)

    return 0

def initialize():
    """Initializes SQL database."""
    conn = get_conn()
    sanitize_db(conn)

    return conn

def close_conn(ext_conn):
    """Close db connection."""
    ext_conn.close()
