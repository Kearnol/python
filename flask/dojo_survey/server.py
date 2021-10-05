from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = "xxxyyy"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    print(request.form)
    session["form"] = {
        "name": request.form["name"],
        "location": request.form["location"],
        "language": request.form["language"],
        "comment": request.form["comment"],
        "preferred": request.form["optin"],
        "subscribe": request.form["subscribe"],
    }
    return redirect("/results")

@app.route("/results")
def results():
    print(session["form"])
    return render_template("results.html", name = session["form"]["name"], location = session["form"]["location"], language = session["form"]["language"], comment = session["form"]["comment"], preferred = session["form"]["preferred"], subscribe = session["form"]["subscribe"])

if __name__ == "__main__":
    app.run(debug=True)