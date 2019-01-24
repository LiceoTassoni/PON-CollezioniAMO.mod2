# vim:fileencoding=utf-8

from __future__ import print_function, division

from flask import Flask, json, request
from flask_cors import CORS

from .io import exceldb_gen
from .util import *

from .dbm.sql import manager, objects
#from .dbm.cdb import manager as cmn, trial

#
#from . import italian as ita

conn   = manager.initialize()
exceldb = exceldb_gen()
app    = Flask(__name__)
CORS(app)

@app.route("/fetch")
def fetch_object():
    return json.jsonify(next(exceldb))

@app.route("/save", methods=["GET", "POST"])
def add_trial():
    print(request.form)
    objects.save_data(conn, request.form)
    return json.jsonify([0])


def wsgiserver():
    app.run(port=8088,host="0.0.0.0")#, debug=True)

if __name__ == "__main__":
    wsgiserver()
