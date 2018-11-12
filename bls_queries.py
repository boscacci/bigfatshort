from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from subscripts import bls_api_query_app as BLS
import pdb, json

Base = declarative_base()

BLS_API_KEY = '72a1e58047ab47f49ad31306a90aa0b8'

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

def get_expenditure_by_demo_code(item_code, demo_code, decile, year):
    query_code = 'CXU' + item_code + demo_code + decile +'M'
    toops = get_bls_row(query_code)
    newList = []
    try:
        newList.append([toop[1] for toop in toops if int(toop[0]) == year][0])
    except IndexError:
        pass
    return newList

#############################################################

# class Year(Base):
#     __tablename__ = 'years'
#     id = Column(Integer, primary_key = True)
#     year = Column(Integer)
#     demographics = relationship('Demographic', back_populates='years')

# class Demographic(Base):
#     __tablename__ = 'demographics'
#     id = Column(Integer, primary_key = True)
#     year_id = Column(Integer, ForeignKey('years.id'))
#     edu_level = Column(Text)
#     expenses = relationship('Expense', back_populates='demographic')
#     years = relationship('Year', back_populates='demographics')

# class Expense(Base):
#     __tablename__ = 'expenses'
#     id = Column(Integer, primary_key = True)
#     category = Column(Text)
#     demographic_id = Column(Integer, ForeignKey('demographics.id'))
#     demographic = relationship('Demographic', back_populates='expenses')

################

categories = ['INCAFTTX', 'HOUSING', 'FOODHOME', 'FOODAWAY', 'HEALTH', 'ALCBEVG', 'APPAREL', 'TRANS', 'ENTRTAIN']
# takes a year and a edu_level and returns list of all expenses

def get_all_expenses_for_demo_and_year(demo_code, decile, year):
    expenses = {}
    for category in categories:
        expenses[category] = get_expenditure_by_demo_code(category, demo_code, decile, year)
    return expenses

####################

def get_all_expenses_all_levels(year):
    
    demo_code = 'LB13'
    levels = ['03', '04', '06', '08', '09'] # edu_levels
    # ed_level_labels = ['sub_hs', 'high_school', 'AD', 'BD', 'MA+']
    
    # levels = ['02','03','04','05','06'] # income_deciles
    # demo_code = 'LB01'
    
    # levels = ['03','04','05'] # housing_levels
    # demo_code = 'LB08'
    
    all_levels = {}
    for level in levels:
        expenses = get_all_expenses_for_demo_and_year(demo_code,level, year)
        all_levels[level] = expenses
    return all_levels

####################
def get_all_data_all_years(start, end):
    alldata_allyears = {}
    for year in range(start,end):
        alldata_allyears[year] = get_all_expenses_all_levels(year)
    return alldata_allyears

data = get_all_data_all_years(2002,2012)

with open('BLS_data_edu.json', 'w') as BLS_data:
    json.dump(data, BLS_data)

#### This script makes so many gosh darn requests, we filed for many API keys with many fake email addys
