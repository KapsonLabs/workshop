# from dataclasses import dataclass
from flask import Flask
# from flask_cors import CORS
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import UniqueConstraint
import requests


app = Flask(__name__)

# app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:@hall65536@db/workshop'
# CORS(app)

# db = SQLAlchemy(app)

# @dataclass
# class Product(db.Model):
#     id: int
#     title: str
#     image: str

#     id = db.Column(db.Integer, primary_key=True, autoincrement=False)
#     title = db.Column(db.String(200))
#     image = db.Column(db.String(200))

@app.route('/')
def index():
    return "Hello"

if __name__ == '__main__':
    print("app started")
    app.run(debug=True, host='0.0.0.0')