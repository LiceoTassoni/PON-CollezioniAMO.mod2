# vim:fileencoding=utf-8


import os.path

opj = os.path.join
app_home = os.path.abspath("./dbcolza/")
dbf_home  = opj(app_home, "dbm", "test")

def static_path():
    mpath = os.path.split(os.path.abspath(__file__))[0]
    # return mpath+'/static/'
    return opj(mpath, "static")
