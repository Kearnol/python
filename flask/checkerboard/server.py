from flask import Flask, render_template
from flask.templating import render_template_string

app = Flask(__name__)

@app.route("/")
def display_checkerboard():
    return render_template("index.html",width=8,height=8)

@app.route("/<int:height>")
def display_checkerboard_height(height):
    return render_template("index.html", height=height, width= 8)

@app.route("/<int:width>/<int:height>")
def display_checkerboard_num(width, height):
    return render_template("index.html", height=height, width=width)

@app.route("/<int:width>/<int:height>/<string:color1>/<string:color2>")
def display_checkerboard_num_color(width, height, color1, color2):
    return render_template("index.html", height=height, width=width, color1=color1, color2=color2) 

if __name__ == "__main__":
    app.run(debug=True)