import pandas as pd
import sqlite3
from sqlalchemy import create_engine,Column, Integer, String, MetaData, Table
from flask import Flask, jsonify, request
from datos_dummy import books  # Al estar en la misma carpeta usa books como variable
import json


churro = "sqlite:///books.db"
engine = create_engine(churro)

query = "SELECT * FROM books"
df = pd.read_sql(query, con=engine)

app = Flask(__name__)

# Endpoint para obtener todos los libros
@app.route("/books", methods=['GET'])
def get_books():
    # books = df.to_dict(orient='records')
    return df.to_string
    # return jsonify(books)

# @app.route("/", methods=['GET']) # Para que llegaraga directamente a la landing page
# def get_books():
#     query = "SELECT * FROM books"
#     df = sql_query(query)
#     return jsonify(df.to_dict(orient='records'))


@app.route('/books/<string:title>', methods=['GET'])
def get_title():
    results = []

    if 'title' in request.args:
        title = request.args['title']
        for book in books:
            if book['title']==title:
                results.append(book)
        if results == []:
            return "Title not found with the title requested"    
        else:
            return jsonify(results)
    else:
        return "No id field provided"
    

@app.route('/books/<string:id>', methods=['GET'])
def book_id():
    results = []
    if 'id' in request.args:
        if str(request.args["id"]).isdigit():
            id = int(request.args['id'])
            for book in books:
                if book['id']==id:
                    results.append(book)
            if results == []:
                return "Book not found with the id requested"    
            else:
                return jsonify(results)
        else:
            return "invalid number"
    else:
        return "No id field provided"




app.run(debug=True)
