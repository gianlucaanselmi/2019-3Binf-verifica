from flask import Flask
from anselmi import books
import json

app = Flask("Biblioteca_marconi")

@app.route("/")
def data_book():
    return json.dumps( 
        [book.__dict__ for book in books]
)
