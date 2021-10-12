from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.author import Author
from flask_app.models.book import Book

@app.route("/")
def index():
    authors = Author.get_all_authors()
    return render_template("index.html", authors = authors)

@app.route("/addauthor", methods=["POST"])
def add_author():
    print(request.form)
    data = {
        "name": request.form["name"]
    }
    author_id = Author.save(data)
    if not author_id:
        return redirect("/")
    return redirect("/showauthor/"+str(author_id))

@app.route("/showauthor/<int:id>")
def show_author(id):
    data = {
        "id": id
    }
    author_books = Author.get_authors_books(data)
    books = Author.get_other_books(data)

    return render_template("showauthor.html", author = author_books, books = books)

@app.route("/addauthfav/<int:id>", methods=["POST"])
def add_auth_fav(id):
    data = {
        "id": id,
        "book_id": request.form["book"]
    }
    Author.add_fav_book(data)
    return redirect("/showauthor/"+str(id))

@app.route("/addbookfav/<int:id>", methods=["POST"])
def add_book_fav(id):
    data = { 
        "book_id": id,
        "id": request.form["author"]
    }
    Author.add_fav_book(data)
    return redirect("/showbook/"+str(data["book_id"]))
