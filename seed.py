import json, pdb
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Text, ForeignKey

app = Flask(__name__)

with open('BLS_data.json') as BLS_data:
    data = json.load(BLS_data)

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///BLS_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Year(db.Model):
    __tablename__ = 'years'
    id = db.Column(Integer, primary_key = True)
    year = db.Column(Integer)
    demographics = db.relationship('Demographic', back_populates='years')

class Demographic(db.Model):
    __tablename__ = 'demographics'
    id = db.Column(Integer, primary_key = True)
    year_id = db.Column(Integer, ForeignKey('years.id'))
    edu_level = db.Column(Text)
    expenses = db.relationship('Expense', back_populates='demographic')
    years = db.relationship('Year', back_populates='demographics')

class Expense(db.Model):
    __tablename__ = 'expenses'
    id = db.Column(Integer, primary_key = True)
    category = db.Column(Text)
    demographic_id = db.Column(Integer, ForeignKey('demographics.id'))
    demographic = db.relationship('Demographic', back_populates='expenses')