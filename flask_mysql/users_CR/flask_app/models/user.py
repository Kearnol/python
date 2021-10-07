from flask_app.config.mysqlconnection import connectToMySQL
from datetime import datetime

class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created = data["created_at"].strftime('%I:%M %p, %B %d, %Y')
        self.updated = data["updated_at"].strftime('%I:%M %p, %B %d, %Y')

    @classmethod
    def insert_user(cls,data):
        query = "INSERT INTO users (first_name, last_name, email) VALUE (%(first_name)s, %(last_name)s, %(email)s)"
        return connectToMySQL("Users").query_db(query,data)

    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users"
        db_users = connectToMySQL("Users").query_db(query)
        users = []
        for u in db_users:
            users.append(User(u))
        return users

    @classmethod
    def get_user(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        user = connectToMySQL("Users").query_db(query,data)
        print(user)
        return User(user[0])
    
    @classmethod
    def update_user(cls,data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s"
        return connectToMySQL("Users").query_db(query,data)

    @classmethod
    def delete_user(cls,data):
        query = "DELETE FROM users WHERE id = %(id)s"
        return connectToMySQL("Users").query_db(query,data)