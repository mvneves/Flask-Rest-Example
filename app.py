from werkzeug import url_decode
from flask import Flask, render_template, request, redirect, url_for, flash
import json

book_list = []

class Book(object):
    """A Fake model"""

    def __init__(self, id, author, title):
        self.id = id
        self.author = author
        self.title = title

    def export_data(self):
        return {"id": self.id,
                "author": self.author,
                "title": self.title
               }

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'secret'

@app.route('/books')
def list_books():
    """GET /books

    Lists all books"""

    books = []
    for book in book_list:
        books.append(book.export_data())

    return json.dumps(books, indent=4)

@app.route('/books/<id>')
def get_book(id):
    """GET /books/<id>

    Get a book by its id"""
    
    rv = {}
    for book in book_list:
        if book.id == int(id):
            rv = book.export_data()
            break

    return json.dumps(rv, indent=4)

@app.route('/books', methods=['POST'])
def create_book():
    """POST /books

    Receives a book data and saves it"""

    data = request.get_json(force=True)

    next_id = 0
    for book in book_list:
        if book.id > next_id:
            next_id = book.id
    next_id = next_id + 1

    book = Book(id=next_id, author=data["author"], title=data["title"])
    book_list.append(book)

    flash('Book %s sucessful saved!' % book.title)

    return json.dumps(book.export_data(), indent=4)


@app.route('/books/<id>', methods=['PUT'])
def update_book(id):
    """PUT /books/<id>

    Updates a book"""

    data = request.get_json(force=True)

    rv = {}
    for book in book_list:
        if book.id == int(id):
            if "title" in keys(data):
                book.title = data["title"]
            rv = book.export_data()
            flash('Book %s sucessful updated!' % book.title)
            break

    return json.dumps(rv, indent=4)

@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    """DELETE /books/<id>

    Deletes a books"""

    rv = {}
    for book in book_list:
        if book.id == int(id):
            flash('Book %s sucessful deleted!' % book.title)
            rv = book.export_data()
            book_list.remove(book)
            break

    return json.dumps(rv, indent=4)


if __name__ == '__main__':
    book_list.append(Book(id=1, author=u'Tolkien, J. R. R.', title=u'Lord of the Rings'))
    book_list.append(Book(id=2, author=u'Asimov, Isaac', title=u'Foundation'))

    app.run()
