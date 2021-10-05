from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = "xxxyyy"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    request.form
    session["form"] = {
        "name": request.form["name"],
        "location": request.form["location"],
        "language": request.form["language"],
        "comment": request.form["comment"]
    }
    return redirect("/results")

@app.route("/results")
def results():
    return render_template("results.html", name = session["form"]["name"], location = session["form"]["location"], language = session["form"]["language"], comment = session["form"]["comment"])

if __name__ == "__main__":
    app.run(debug=True)