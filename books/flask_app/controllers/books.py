from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.author import Author
from flask_app.models.book import Book

@app.route("/addbook")
def add_book():
    books = Book.get_all_books()
    return render_template("addbook.html", books = books)

@app.route("/savebook", methods=["POST"])
def save_book():
    data = {
        "title": request.form["title"],
        "num_of_pages": request.form["num_of_pages"]
    }
    book_id = Book.save(data)
    return redirect("/showbook/"+str(book_id))

@app.route("/showbook/<int:id>")
def show_book(id):
    data = {
        "id": id
    }
    book = Book.get_books_authors(data)
    authors = Author.get_all_authors()
    return render_template("showbook.html", book = book, authors = authors)
