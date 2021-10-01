from flask import Flask, redirect, request, render_template, session

app = Flask(__name__)
app.secret_key = "xxxyyy"

@app.route("/")
def index():
    if "visits" not in session:
        session["visits"] = 0 
    if "count" not in session:    
        session["count"] = 0   
    session["visits"] += 1
    print(session["count"])
    return render_template("index.html", visits=session["visits"], counter=session["count"])

@app.route("/+2")
def add_two():
    session["count"] += 2
    print(session["count"])
    return redirect("/")

@app.route("/add_custom", methods=["POST"])
def add_custom():
    session["count"] += int(request.form["user_add"]) 
    return redirect("/")

@app.route("/destroy_session")
def clear():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
