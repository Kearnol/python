from mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        

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