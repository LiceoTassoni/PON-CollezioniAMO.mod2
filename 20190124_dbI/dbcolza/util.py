# vim:fileencoding=utf-8

from __future__ import print_function, division

import os.path

def static_path():
    mpath = os.path.split(os.path.abspath(__file__))[0]
    return mpath+'/static/'

opj      = os.path.join
app_home = os.path.abspath("./dbcolza/")
dbf_home  = opj(app_home, "dbm", "test")
