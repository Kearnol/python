from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user import User
from flask import flash
from flask_bcrypt import Bcrypt #install into pipenv (> pipenv install flask-bcrypt)
bcrypt = Bcrypt(app) # need to add this to be able to hash 

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/register", methods=["POST"])
def register():

    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email":request.form["email"],
        "confirm_pass": request.form["confirm_pass"],
        "orig_pass": request.form["password"]
    }
    
    if User.validate_reg(data):
        pw_hash = bcrypt.generate_password_hash(request.form["password"])
        data["password"] = pw_hash
        user_id = User.save(data)
        session["user_id"] = user_id
        session["first_name"] = data["first_name"]
        flash("User created!")
        return redirect("/success")
    
    return redirect("/")

    
@app.route("/success")
def success():
    if "user_id" not in session:
        flash("Must be logged in.")
        return redirect ("/login")
    
    return render_template("success.html", session = session)

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

@app.route("/login")
def login():
    return render_template ("login.html")

@app.route("/loginprocess", methods=["POST"])
def process_login():
    data = {
        "email": request.form["email"]
        }
    
    user_in_db = User.validate_user_by_email(data)
    
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/login")
    if not bcrypt.check_password_hash(user_in_db.password, request.form["password"]):
        flash("Invalid Email/Password")
        return redirect("/login")
    session["user_id"] = user_in_db.id
    session["first_name"] = user_in_db.first_name
    return redirect("/success")
