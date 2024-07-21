#Carly Grubbss - 7/12/2024
#M04 Lab - Case Study: Python APIs

#importing needed items 
from flask import Flask, request, jsonify
app = Flask(__name__)

#setting up the applicaiton to use flask


#Creating the books dictionary
books = [
    {
        "id": 1,
        "book_name": "River Strong",
        "author": "BJ Daniels",
        "publisher": "Canary Street Press"
    },
    {
        "id": 2,
        "book_name": "Harry Potter and the Sorcerer\'s Stone",
        "author": "J.K. Rowling",
        "publisher": "Pottermore Publishing"
    },
    {
        "id": 3,
        "book_name": "This Calder Range",
        "author": "Janet Dailey",
        "publisher": "Gallery Books"
    },
    {
        "id": 4,
        "book_name": "NIV Study Bible",
        "author": "Men & Women of the Bible",
        "publisher": "Zondervan"
    }
]

#Making sure that the website works
@app.route("/")
def index():
    return "Hello!"

#Making sure that the website will go to the next page use /test
@app.route("/test")
def test():
    return{"books": "book data"}

#Getting the list of books use /books
@app.route("/books", methods=["GET"])
def get_booklist():
    return jsonify(books)

#Getting a specific book"s information use /books_id/(1 - 4)
@app.route("/books_id/<int:id>", methods=["GET"])
def get_books(id):
    book = [book for book in books if book["id"] == id]
    return jsonify(book)

#Adding a new book
@app.route("/books_add", methods=["POST"])
def add_book():
    book = {
        "id": books[-1]["id"] + 1,
        "book_name": request.json["Introduction To Python"],
        "author": request.json["Bill Lubanovic"],
        "publisher": request.json["O\'Rielly"]
        }
    books.append(book)
    return jsonify(book)

#Changes an existing book
@app.route("/books_put/<int:id>", methods=["PUT"])
def update_book(id):
    book = [book for book in books if book["id"] == id]
    book[0]["book_name"] = request.json.get("book_name", book[0]["book_name"])
    book[0]["author"] = request.json.get("author", book[0]["author"])
    book[0]["publisher"] = request.json.get("publisher", book[0]["publisher"])
    return jsonify(book[0])

#Deletes an existing book
@app.route("/books_delete/<int:id>", methods=["DELETE"])
def delete_book(id):
    book = [book for book in books if book["id"] == id]
    books.remove(book[0])
    return jsonify({"result": "Book deleted"})

#Running the application
if __name__ == "__main__":
    app.run()