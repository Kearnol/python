from flask import Flask, render_template, redirect, request, session
from user import User


app = Flask(__name__)

@app.route("/")
def create():
    return render_template("create.html")

@app.route("/adduser", methods=["POST"])
def addUser():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    User.insert_user(data)
    return redirect("/read")


@app.route("/read")
def read():
    users = User.get_all_users()
    return render_template("read.html", users=users)

if __name__ == "__main__":
    app.run(debug=True)

