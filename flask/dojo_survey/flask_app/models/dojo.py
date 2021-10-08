from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Dojo:
    def __init__(self, data) -> None:
        self.id = data["id"]
        self.name = data["name"]
        self.location = data["location"]
        self.language = data["language"]
        self.comment = data["comment"]
        self.communication = data["communication"]
        self.subscribe = data["subscribe"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def save_dojo(cls, data):
        query = "INSERT INTO dojos (name, location, language, comment, communication, subscribe) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s, %(communication)s, %(subscribe)s)"
        dojoID = connectToMySQL("dojo_survey_schema").query_db(query, data)
        return dojoID

    @classmethod
    def get_dojo(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s"
        db_dojo = connectToMySQL("dojo_survey_schema").query_db(query, data)
        dojo = Dojo(db_dojo[0])
        return dojo

    

    @staticmethod
    def validate(data):
        is_valid = True

        if len(data["name"]) < 1:
            flash("Please enter a name")
            is_valid = False
        if len(data["location"]) < 1:
            flash("Please enter a location")
            is_valid = False
        if "language" not in data:
            flash("Please enter a language")
            is_valid = False
        if len(data["comment"]) < 1:
            flash("A short comment is required")
            is_valid = False

        return is_valid
