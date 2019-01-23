# vim:fileencoding=utf-8

from __future__ import print_function, division

from flask import Flask, json, request
from flask_cors import CORS

from .io import exceldb_gen
from .util import *

#from .dbm.sql import manager, school, user, classes, subjects, students, mistakes
#from .dbm.cdb import manager as cmn, trial

#
#from . import italian as ita

#c_db = cmn.initialize()
#conn   = manager.initialize()


exceldb = exceldb_gen()

app    = Flask(__name__)
CORS(app)





@app.route("/fetch")
def fetch_object():
    return json.jsonify(next(exceldb))






#@app.route("/addtrial", methods=["GET", "POST"])
#def add_trial():
#    trial.add_new_trial(c_db, request.form)
#    return json.jsonify([0])
#
#@app.route("/listtrials")
#def trials_list():
#    resp = trial.list_trials(c_db, request.args)
#    return json.jsonify(resp)
#
#@app.route("/updatetrial", methods=["GET", "POST"])
#def update_trial():
#    trial.update_trial(c_db, request.form)
#    return json.jsonify([0])
#
#@app.route("/addmistake", methods=["GET", "POST"])
#def add_mistake():
#    mistakes.add_new_mistake(conn, request.form)
#    return json.jsonify([0])
#
#@app.route("/listmistakes")
#def mistakes_list():
#    return json.jsonify(mistakes.get_mistake_list(conn))
#
#@app.route("/addstudents", methods=["GET", "POST"])
#def add_student():
#    students.add_new_student(conn, request.form)
#    return json.jsonify([0])
#
#@app.route("/liststudents")
#def students_list():
#    return json.jsonify(students.get_students_list(conn, request.args))
#
#@app.route("/addclass", methods=["GET", "POST"])
#def add_class():
#    classes.add_new_class(conn, request.form)
#    return json.jsonify([0])
#
#@app.route("/listclasses")
#def classes_list():
#    return json.jsonify(classes.get_class_list(conn, request.args))
#
#@app.route("/listschools")
#def school_list():
#    return json.jsonify(school.get_school_list(conn))
#
#@app.route("/addschool", methods=["GET", "POST"])
#def add_school():
#    school.add_new_school(conn, request.form)
#    return json.jsonify([0])
#
#@app.route("/listusers")
#def user_list():
#    return json.jsonify(user.get_user_list(conn))
#
#@app.route("/adduser", methods=["GET", "POST"])
#def add_user():
#    user.add_new_user(conn, request.form)
#    return json.jsonify([0])
#
#@app.route("/listsubjects")
#def subject_list():
#    return json.jsonify(subjects.get_subject_list(conn))
#
#@app.route("/sctypes_it")
#def school_types_it():
#    return json.jsonify(ita.load_it_system())

def wsgiserver():
    app.run(port=8088)

if __name__ == "__main__":
    wsgiserver()
