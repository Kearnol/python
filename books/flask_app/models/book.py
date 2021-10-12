from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author
from flask import flash

class Book:
    def __init__(self, data):
        self.id = data["id"]
        self.title = data["title"]
        self.num_of_pages = data["num_of_pages"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.authors = []

    @classmethod
    def get_all_books(cls):
        query = "SELECT * FROM books"
        books_db = connectToMySQL("authors_books").query_db(query)
        books = []
        for book in books_db:
            books.append(Book(book))
        return books

    @classmethod
    def save(cls, data):
        query = "INSERT INTO books (title, num_of_pages) VALUES (%(title)s, %(num_of_pages)s)"
        book_id = connectToMySQL("authors_books").query_db(query, data)
        flash("Book added!")
        return book_id

    @classmethod
    def get_book(cls, data):
        query = "SELECT * FROM authors WHERE id = %(id)s"
        book_db = connectToMySQL("authors_books").query_db(query, data)
        book = Book(book_db[0])
        return book

    @classmethod
    def get_books_authors(cls, data):
        query = "SELECT * FROM books LEFT JOIN favorites ON favorites.book_id = books.id LEFT JOIN authors ON favorites.author_id = authors.id WHERE books.id = %(id)s"
        books_db = connectToMySQL("authors_books").query_db(query, data)
        book = Book(books_db[0])
        for row in books_db:
            author_data = {
                "id": row["authors.id"],
                "name": row["name"],
                "created_at": row["authors.created_at"],
                "updated_at": row["authors.updated_at"]
            }
            book.authors.append(author.Author(author_data))
        return book 

    