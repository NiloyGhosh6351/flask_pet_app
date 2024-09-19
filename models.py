from flask import Flask, render_template, redirect, url_for
from models import db, Pet

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    type = db.Column(db.String(100), nullable=False)
