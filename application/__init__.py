from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']=os.getenv("SQLURI")
app.config['SECRET_KEY']=os.getenv("SECKEY")

db = SQLAlchemy(app)

from application import models, routes

