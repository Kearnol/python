from flask_app import app
from flask import render_template, redirect, request, session
from flask_bcrypt import Bcrypt
from flask_app.models.email import Email
from flask import flash

@app.route("/")
def index(): 
    return render_template("index.html")

@app.route("/checkemail", methods=["POST"])
def check_for_email():
    data = {
        "email": request.form["email"]
    }
    if not Email.validate(data):
        return redirect("/")
    
    user_db = Email.get_user_by_email(data)
    
    if not user_db:
        session["input"] = request.form["email"]
        return redirect("/")
    else:
        session["id"] = user_db.id
        session["email"] = user_db.email
        print(session)    
        return redirect("/success")

@app.route("/save", methods=["POST"])
def save():
    data = { 
        "email": request.form["email"]
    }
    if not Email.validate(data):
        return redirect("/")
    else:
        is_unique = Email.is_unique(data)
        if not is_unique:
            return redirect("/")
        user_id = Email.save_email(data)
        session["id"] = user_id
        print(session["id"])
        return redirect ("/success")

@app.route("/success")
def success():
    if "id" in session:
        db_emails = Email.get_all_emails()
        return render_template("success.html", emails = db_emails)
    else:
        flash("Must be logged in.")
        return redirect("/")

@app.route("/delete/<int:id>")
def delete(id):
    data = {
        "id":id
    }
    Email.delete_email(data)
    return redirect("/success")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")