from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.book import Book
from flask import flash


class Author:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.books = []

    @classmethod
    def get_all_authors(cls):
        query = "SELECT * FROM authors"
        all_db_authors = connectToMySQL("authors_books").query_db(query)
        all_authors = []
        for obj in all_db_authors:
            all_authors.append(Author(obj))
        return all_authors

    @classmethod
    def save(cls, data):
        if not data["name"]:
            flash ("We won't adding ~nothing~!")
            return
        query = "INSERT INTO authors (name) VALUES (%(name)s)"
        author_id = connectToMySQL("authors_books").query_db(query, data)
        return author_id

    @classmethod
    def get_author(cls, data):
        query = "SELECT * FROM authors WHERE id = %(id)s"
        author_db = connectToMySQL("authors_books").query_db(query, data)
        author = Author(author_db[0])
        return author
    
    @classmethod
    def get_authors_books(cls, data):
        query = "SELECT * FROM authors LEFT JOIN favorites ON favorites.author_id = authors.id LEFT JOIN books ON favorites.book_id = books.id WHERE authors.id = %(id)s"
        author_db = connectToMySQL("authors_books").query_db(query, data)
        author = Author(author_db[0])
        for row in author_db:
            book_data = {
                "id": row["books.id"],
                "title": row["title"],
                "num_of_pages": row["num_of_pages"],
                "created_at": row["books.created_at"],
                "updated_at": row["books.updated_at"]
            }
            author.books.append(Book(book_data))
        return author 

    @classmethod
    def add_fav_book(cls, data):
        query = "INSERT INTO favorites (author_id, book_id) VALUES (%(id)s, %(book_id)s)"
        connectToMySQL("authors_books").query_db(query, data)
        return flash("Success! Book added")

    @classmethod
    def get_other_books(cls, data):
        # query = "SELECT * FROM favorites JOIN books ON book_id = books.id WHERE author_id != %(id)s GROUP BY author_id,book_id"
        query = "SELECT * FROM books LEFT JOIN favorites ON book_id = books.id JOIN authors ON authors.id = favorites.author_id WHERE author_id != 2"
        other_books_db = connectToMySQL("authors_books").query_db(query,data)
        other_books = []
        for book in other_books_db:
            other_books.append(Book(book))
        return other_books