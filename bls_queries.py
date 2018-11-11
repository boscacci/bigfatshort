from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from subscripts import bls_api_query_app as BLS
import pdb, json

Base = declarative_base()

BLS_API_KEY = '9452301636e9423cac8ae92d442161df'

# A year has many consumer demographics
# A consumer demographic has many expenditures
# An expenditure belongs to a consumer demographic
# A consumer demographic belongs to a year

def get_bls_row(query_code):
    df = BLS.get_series([query_code], 2002, 2012, BLS_API_KEY)
    print('\n')
    years = [year.year for year in df.axes[0]]
    values = [year[0] for year in df.values]
    return(list(zip(years,values)))

#############################################################

def get_expenditure_by_education(item_code, edu_level, year):
    query_code = 'CXU' + item_code + 'LB13' + edu_level +'M'
    toops = get_bls_row(query_code)
    newList = []
    try:
        newList.append([toop[1] for toop in toops if int(toop[0]) == year][0])
    except IndexError:
        pass
    return newList

#############################################################

class Year(Base):
    __tablename__ = 'years'
    id = Column(Integer, primary_key = True)
    year = Column(Integer)
    demographics = relationship('Demographic', back_populates='years')

class Demographic(Base):
    __tablename__ = 'demographics'
    id = Column(Integer, primary_key = True)
    year_id = Column(Integer, ForeignKey('years.id'))
    edu_level = Column(Text)
    expenses = relationship('Expense', back_populates='demographic')
    years = relationship('Year', back_populates='demographics')

class Expense(Base):
    __tablename__ = 'expenses'
    id = Column(Integer, primary_key = True)
    category = Column(Text)
    demographic_id = Column(Integer, ForeignKey('demographics.id'))
    demographic = relationship('Demographic', back_populates='expenses')

################

categories = ['HOUSING', 'FOODHOME', 'FOODAWAY', 'HEALTH', 'ALCBEVG', 'APPAREL', 'TRANS', 'ENTRTAIN']
# takes a year and a edu_level and returns list of all expenses
def get_all_expenses_for_ed_and_year(edu_level, year):
    expenses = {}
    for category in categories:
        expenses[category] = get_expenditure_by_education(category, edu_level, year)
    return expenses

####################

def get_all_expenses_all_levels(year):
    ed_level_labels = ['sub_hs', 'high_school', 'AD', 'BD', 'MA+']
    ed_levels = ['03', '04', '06', '08', '09']
    all_levels = {}
    for ed_level in ed_levels:
        expenses = get_all_expenses_for_ed_and_year(ed_level, year)
        all_levels[ed_level] = expenses
    return all_levels

####################
def get_all_data_all_years(start, end):
    alldata_allyears = {}
    for year in range(start,end):
        alldata_allyears[year] = get_all_expenses_all_levels(year)
    return alldata_allyears

data = get_all_data_all_years(2002,2012)

with open('BLM_data.json', 'w') as BLM_data:
    json.dump(data, BLM_data)


