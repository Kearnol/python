from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def display_checkerboard():
    return render_template("index.html",width=8,height=8)

@app.route("/<int:width>/<int:height>")
def display_checkerboard_num(width, height):
    return render_template("index.html", height=height, width=width)

@app.route("/10/10")
def display_checkerboard_10():
    return render_template("index.html", height=10, width=10)

if __name__ == "__main__":
    app.run(debug=True)