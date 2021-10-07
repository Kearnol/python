from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.dojo import Dojo

@app.route("/")
def add_select_dojo():
    dojo = Dojo.get_all_dojos()
    print(dojo)
    return render_template ("index.html", dojo = dojo)

@app.route("/dojodisplay/<int:id>")
def show_dojo(id):
    data = {
        "id": id
    }
    dojo = Dojo.get_dojos_ninjas(data)
    return render_template("display_dojo.html", dojo = dojo)
    

@app.route("/adddojo", methods=["POST"])
def add_dojo():
    data = {
        "name": request.form["name"],
    }
    newdojo = Dojo.save_dojo(data)
    return redirect("/")

@app.route("/deletedojo/<int:id>")
def delete_dojo(id):
    data = {
        "id": id
    }
    Dojo.delete_dojo(data)
    return redirect("/")