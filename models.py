From sqlalchemy import *
From sqlalchemy.ext.declarative import declarative_base
From sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Year(Base):
    __tablename__ = 'years'
    id = Column(Integer, primary_key = True)
    year = Column(Integer)
    education = relationship('Education', back_populates='years')

class Education(Base):
    __tablename__ = 'education'
    id = Column(Integer, primary_key = True)
    year_id = Column(Integer, ForeignKey('years.id'))

class Expenditure(Base):
