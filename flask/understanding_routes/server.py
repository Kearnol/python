from flask import Flask

app = Flask(__name__)

@app.route("/")
def say_hello():
    return "Hello World!"

@app.route("/dojo")
def say_dojo():
    return "Dojo!"

@app.route("/<string:input>")
def say_hi_input(input):
    return "Hi " +input +"!"

@app.route("/<int:num>/<string:word>/")
def say_hello_mult(num,word):
    return  word * num

@app.route("/")


if __name__ == "__main__":
    app.run(debug = True)