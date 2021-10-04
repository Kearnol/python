from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "xxxyyy"  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    session["cart"] = {
        "apple": request.form["apple"],
        "strawberry": request.form["strawberry"],
        "raspberry": request.form["raspberry"],
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "student_id": request.form["student_id"],
        "count": int(int(request.form["apple"]) + int(request.form["strawberry"]) + int(request.form["raspberry"]))
        }
    print(f"RECEIPT: Charging {session['cart']['first_name']} {session['cart']['last_name']} for {session['cart']['count']} fruit. Customer #: {session['cart']['student_id']}  ")
    print(request.form)
    return render_template("checkout.html", strawberry = session["cart"]["strawberry"], apple = session["cart"]["apple"], raspberry = session["cart"]["raspberry"], first_name = session["cart"]["first_name"], last_name=session["cart"]["last_name"], student_id=session["cart"]["student_id"])

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    