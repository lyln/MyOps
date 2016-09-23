__author__ = 'ljd'
from flask import Flask
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config.from_object('config')

from app import views

bootstrap = Bootstrap(app)



