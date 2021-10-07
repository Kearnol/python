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

@app.route("/edit/<int:id>")
def edit_user(id):
    data = {
        "id": id
    }
    user = User.get_user(data)
    return render_template("edit.html", user=user)

@app.route("/editprocess/<int:id>", methods=["POST"])
def renderedit(id):
    data = { 
        "id": id,
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    User.update_user(data)
    return redirect("/show/"+str(id))

@app.route("/show/<int:id>")
def show(id):
    data = {
        "id": id
    }
    user = User.get_user(data)
    return render_template("user.html", user=user)

@app.route("/delete/<int:id>")
def delete_user(id):
    data ={
        "id": id
    }
    User.delete_user(data)
    return redirect("/read")


if __name__ == "__main__":
    app.run(debug=True)

