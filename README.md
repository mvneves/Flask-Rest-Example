# Flask and REST example

A very simple RESTful Flask CRUD

## Dependencies

Install Virtualenv:

    pip install --user virtualenv
    export PATH=$PATH:$HOME/.local/bin/

Create a new virtualenv instance and activate it:

    virtualenv flaskapp
    . flaskapp/bin/activate

Install Flask:

    pip install Flask


## Running it

Just run on terminal:

    $ cd flask-rest-example
    $ python app.py


Web Service will be running on [http://127.0.0.1:5000/]()



## Test it using cURL command line tool

### GET /books - returns the list of books

Get a list of books:

    curl -s -H "Content-Type: application/json" -X GET \
    http://localhost:5000/books | python -m json.tool

Output:

	[
	    {
	        "author": "Tolkien, J. R. R.",
	        "id": 1,
	        "title": "Lord of the Rings"
	    },
	    {
	        "author": "Asimov, Isaac",
	        "id": 2,
	        "title": "Foundation"
	    }
	]

### GET /books/<id> - returns the book entry specified by id

Get a list of books:

    curl -s -H "Content-Type: application/json" -X GET \
    http://localhost:5000/books/1 | python -m json.tool

Output:

	{
	    "author": "Tolkien, J. R. R.",
	    "id": 1,
	    "title": "Lord of the Rings"
	}

### POST /books - creates a new book entry

Create a new book entry:

    curl -s -H "Content-Type: application/json" -X POST \
    --data '{"author": "Verne, Jules",
             "title": "Twenty Thousand Leagues Under the Sea"}' \
    http://localhost:5000/books | python -m json.tool

Output:

	{
	    "author": "Verne, Jules",
	    "id": 3,
	    "title": "Twenty Thousand Leagues Under the Sea"
	}


### PUT /books/<id> - update the book entry specified by id

Create a new book entry:

    curl -s -H "Content-Type: application/json" -X PUT \
    --data '{"title": "Journey to the Center of the Earth"}' \
    http://localhost:5000/books/2 | python -m json.tool

Output:

	{
	    "author": "Asimov, Isaac",
	    "id": 2,
	    "title": "Journey to the Center of the Earth"
	}

### DELETE /books/<id> - delete the book entry specified by id

Delete a book entry:

    curl -s -H "Content-Type: application/json" -X DELETE \
    http://localhost:5000/books/1 | python -m json.tool

Output:

	{
	    "author": "Tolkien, J. R. R.",
	    "id": 1,
	    "title": "Lord of the Rings"
	}

## It is also possible to test it with Postman

Download Postman from [https://www.getpostman.com/]()

    $ tar xzf Postman-linux-x64-6.3.0.tar.gz
    $ cd Postman
    $ ./Postman
