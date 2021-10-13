from flask_app import app
from flask import render_template, request, redirect, session
from flask import flash
from flask_app.models.recipe import Recipe
from flask_app.models.user import User

@app.route("/create")
def create():
    if "user_id" not in session:
        flash("Must be logged in.")
        return redirect("/login")
    return render_template("create.html")

@app.route("/saverecipe", methods=["POST"])
def save_recipe():
    print(request.form)
    if not Recipe.validate_recipe(request.form):
        return redirect("/create")
    data = {
        "name": request.form["name"],
        "description": request.form["description"],
        "instructions": request.form["instructions"],
        "made_on": request.form["made_on"],
        "under_30": request.form["under_30"],
        "user_id": session["user_id"]
    }
    Recipe.save_recipe(data)
    return redirect("/dashboard") 

@app.route("/editrecipe/<int:id>")
def edit_recipe(id):
    if "user_id" not in session:
        flash("Must be logged in.")
        return redirect("/login")
    data = {
        "id": id
    }
    recipe = Recipe.get_recipe_by_id(data)
    if recipe.under_30 == 1:
        yes = "checked"
        no = ""
    else:
        no = "checked"
        yes = ""
    return render_template("editrecipe.html", recipe=recipe, yes=yes, no=no)

@app.route("/updaterecipe/<int:id>",methods =["POST"])
def update_recipe(id):
    if not Recipe.validate_recipe(request.form):
        return redirect("/create")
    data = {
        "id": id,
        "name": request.form["name"],
        "description": request.form["description"],
        "instructions": request.form["instructions"],
        "made_on": request.form["made_on"],
        "under_30": request.form["under_30"],
    }
    Recipe.update_recipe(data)
    flash("Recipe Updated!")
    return redirect("/editrecipe/"+str(id))
    
@app.route("/deleterecipe/<int:id>")
def delete_recipe(id):
    if "user_id" not in session:
        flash("Must be logged in.")
        return redirect("/login")
    data = {
        "id": id
    }
    Recipe.delete(data)
    return redirect("/dashboard")

@app.route("/viewrecipe/<int:id>")
def view_recipe(id):
    if "user_id" not in session:
        flash("Must be logged in.")
        return redirect("/login")
    data = {
        "id":id
    }
    recipe = Recipe.get_recipe_by_id(data)
    Recipe.pretty_date(recipe)
    print(recipe.created_at)
    return render_template("viewrecipe.html", recipe = recipe)