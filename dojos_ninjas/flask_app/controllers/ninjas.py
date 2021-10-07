from flask_app import app
from flask import request, redirect, render_template, session
from flask_app.models import dojo
from flask_app.models.ninja import Ninja

@app.route("/addninja")
def add_ninja():
    dojos = dojo.Dojo.get_all_dojos()
    return render_template("addninja.html", dojos = dojos)

@app.route("/saveninja", methods =["POST"])
def save_ninja():
    data = {
        "dojo_id":request.form["dojo"],
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"]
    }
    Ninja.save_ninja(data)
    return redirect("/dojodisplay/"+str(data["dojo_id"]))