from flask import Flask, render_template

app = Flask(__name__)

@app.route("/play")
def display_boxes_3():
    return render_template("play.html", num=3, color="rgb(127, 127, 242)")

@app.route("/play/<int:num>")
def display_boxes_num(num):
    return render_template("play.html", num=num, color="rgb(127, 127, 242)")

@app.route("/play/<int:num>/<string:color>")
def display_box_num_color(num, color):
    return render_template ("play.html", num=num, color=color)
if __name__ == "__main__":
    app.run(debug=True)
