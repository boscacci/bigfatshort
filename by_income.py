import json, pdb
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Text, ForeignKey

app = Flask(__name__)

# app.config['DEBUG'] = True
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///BLS_data.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
# db = SQLAlchemy(app)

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class By_Income(Base):
    __tablename__ = 'by_income'
    id = Column(Integer, primary_key = True)
    year = Column(Integer)
    income_quintile = Column(Integer)
    income = Column(Integer)
    housing = Column(Integer)
    foodhome = Column(Integer)
    foodaway = Column(Integer)
    health = Column(Integer)
    alcbevg = Column(Integer)
    apparel = Column(Integer)
    trans = Column(Integer)
    entrtain = Column(Integer)
