from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

class Email:
    def __init__(self, data) -> None:
        self.id = data["id"]
        self.email = data["email"]

    @classmethod
    def get_user_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s"
        user_db = connectToMySQL("users_db").query_db(query, data)
        if len(user_db) < 1:
            flash("Email not in database")
            return False
        else:
            flash("Success! An email address match was found.")
        return Email(user_db[0])

    @staticmethod
    def validate(data):
        regex_pass = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        is_valid = True
        if not regex_pass.match(data["email"]):
            flash("Text input did not match email address format.")
            is_valid = False
        return is_valid

    @classmethod
    def get_all_emails(cls):
        query = "SELECT * FROM users"
        db_emails = connectToMySQL("users_db").query_db(query)
        return db_emails


    @classmethod
    def delete_email(clas, data):
        query = "DELETE FROM users WHERE id = %(id)s"
        return connectToMySQL("users_db").query_db(query, data)
    
    @classmethod
    def save_email(clas, data):
        query = "INSERT INTO users (email) VALUES (%(email)s)"
        new_email_id = connectToMySQL("users_db").query_db(query, data)
        return new_email_id

    @classmethod
    def is_unique(cls, data):
        query = "SELECT email FROM users;"
        all_db_emails = connectToMySQL("users_db").query_db(query, data)
        is_unique = True
        for i in all_db_emails:
            print(i["email"])
            if i["email"] == data["email"]:
                flash("That email already exists")
                is_unique = False
        return is_unique

