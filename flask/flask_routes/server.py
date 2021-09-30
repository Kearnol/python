from flask import Flask, render_template
import facts

app = Flask(__name__) # the main area where the code is being executed ( = "__main__")

@app.route("/") #this defines the "route" (aka the path) where people will access the information within this @section. "/" is essentially the main page.  "http://127.0.0.1:5000/" or "localhost:5000/"
def welcome():
    return render_template("index.html")

@app.route("/monsters/<monster>") #through abstraction, app.route associates the function directly beneath it with the the route path in the ()
def monster_page(monster):
    if monster == "dracula":
        return render_template("monster.html", monster_name=monster.capitalize(), facts = facts.dracula_facts)
    if monster == "frankenstein":
        return render_template("monster.html", monster_name=monster.capitalize(), facts = facts.frankenstein_facts)
    if monster == "mummy":
        return render_template("monster.html", monster_name=monster.capitalize(), facts = facts.mummy_facts)

if __name__ == "__main__": # <-- this needs to be the last thing
    app.run(debug=True) # <-- this needs to be turned on. 