from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
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
        user_id = connectToMySQL("login_reg").query_db(query, data)
        return user_id

    @staticmethod
    def validate_reg(data):
        email_regex = re.compile(r'^[a-zA-Z0-9.+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]+$')
        password_regex = re.compile(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,15}$')
        # requires 8-20 chars, 1 upper, 1 lower, 1 number.
        is_valid = True
        
        if len(data["first_name"]) < 2:
            flash("We need a first name...")
            is_valid = False
        if len(data["last_name"]) < 2:
            flash("...and a last name.")
        if not email_regex.match(data["email"]):
            flash("We're gonna need a valid email.")
            is_valid = False  
        if data["orig_pass"] != data["confirm_pass"]:
            flash("Passwords don't match....you gotta fix that.")
        if not password_regex.match(data["orig_pass"]):                  
            flash("Password doesn't meet criteria")
            is_valid = False
        
        return is_valid

    @classmethod
    def validate_user_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s"
        user_db = connectToMySQL("login_reg").query_db(query, data)
        if len(user_db) < 1:
            return False
        return (User(user_db[0]))

