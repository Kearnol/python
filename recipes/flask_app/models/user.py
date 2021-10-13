from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask import session, redirect
import re

class User:
    def __init__(self, data) -> None:
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)"
        user_id = connectToMySQL("recipes").query_db(query, data)
        return user_id

    @staticmethod
    def validate_reg(data):
        email_regex = re.compile(r'^[a-zA-Z0-9.+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]+$')
        password_regex = re.compile(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,15}$')
        # requires 8-20 chars, 1 upper, 1 lower, 1 number.
        is_valid = True
        
        if len(data["first_name"]) < 2:
            flash("A first name is required.")
            is_valid = False
        if len(data["last_name"]) < 2:
            flash("A last name is required.")
        if not email_regex.match(data["email"]):
            flash("Invalid email address.")
            is_valid = False  
        if data["password"] != data["confirm_pass"]:
            flash("Passwords don't match.")
            is_valid = False
        if not password_regex.match(data["password"]):                  
            flash("Password doesn't meet criteria.")
            is_valid = False
        return is_valid

    @classmethod
    def get_user_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s"
        user_db = connectToMySQL("recipes").query_db(query, data)
        if len(user_db) < 1:
            return False
        return (User(user_db[0]))

    @classmethod
    def get_user_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        user_db = connectToMySQL("recipes").query_db(query, data)
        if len(user_db) < 1:
            return False
        return (User(user_db[0]))

    @staticmethod
    def logged_in_check():
        if "user_id" not in session:
            flash("Must be logged in")
            return redirect("/login")
            
            

