from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Recipe:
    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.description = data["description"]
        self.instructions = data["instructions"]
        self.made_on = data["made_on"]
        self.under_30 = data["under_30"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]

    @classmethod
    def validate_recipe(cls, data):
        is_valid = True      
        if len(data["name"]) < 1:
            flash("A name is required.")
            is_valid = False
        if len(data["description"]) < 1:
            flash("Description is required.")
            is_valid = False
        if len(data["instructions"]) < 1:
            flash("Instructions are required")
            is_valid = False  
        if not data["made_on"]: 
            flash("Made On date required")
            is_valid = False   
        return is_valid

    @classmethod
    def save_recipe(cls, data):
        query = "INSERT INTO recipes (name, description, instructions, made_on, under_30, user_id) VALUES (%(name)s, %(description)s, %(instructions)s, %(made_on)s, %(under_30)s, %(user_id)s)"
        flash("Recipe added!")
        return connectToMySQL("recipes").query_db(query, data)
        #returns the recipe ID 

    @classmethod
    def get_all_recipes(cls):
        query = "SELECT * FROM recipes"
        db_recipes = connectToMySQL("recipes").query_db(query)
        all_recipes = []
        for recipe in db_recipes:
            if recipe["under_30"] == 0:
                recipe["under_30"] = "No"
            if recipe["under_30"] == 1:
                recipe["under_30"] = "Yes"
            all_recipes.append(Recipe(recipe))
        return all_recipes

    @classmethod
    def get_recipe_by_id(cls,data):
        query = "SELECT * FROM recipes JOIN users ON user_id = users.id WHERE recipes.id = %(id)s"
        db_recipe = connectToMySQL("recipes").query_db(query, data)
        if db_recipe[0]["under_30"] == 0:
            db_recipe[0]["under_30"] = "No"
        if db_recipe[0]["under_30"] == 1:
            db_recipe[0]["under_30"] = "Yes"
        return Recipe(db_recipe[0])
        
        #returns instance of recipe 

    @classmethod
    def update_recipe(cls, data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, made_on = %(made_on)s, under_30 = %(under_30)s WHERE id = %(id)s"
        return connectToMySQL("recipes").query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s"
        return connectToMySQL("recipes").query_db(query, data)

    @staticmethod
    def pretty_date(self):
        self.created_at = self.created_at.strftime("%B %d, %Y")
        self.updated_at = self.updated_at.strftime("%B %d, %Y")
        self.made_on = self.made_on.strftime("%B %d, %Y")
        return
        