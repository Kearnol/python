from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.dojo import Dojo

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    print(request.form)
    data = {
        "name": request.form["name"],
        "location": request.form["location"],
        "language": request.form["language"],
        "comment": request.form["comment"],
        "communication": request.form["optin"],
        "subscribe": request.form["subscribe"],
    }

    if Dojo.validate(data):
        dojoID =Dojo.save_dojo(data)
        return redirect("/results/"+str(dojoID))
    else: 
        return redirect("/")

@app.route("/results/<int:id>")
def results(id):
    data = {
        "id": id
    }
    dojo = Dojo.get_dojo(data)
    return render_template("results.html", name = dojo.name, location = dojo.location, language = dojo.language, comment = dojo.comment, communication = dojo.communication, subscribe = dojo.subscribe)
