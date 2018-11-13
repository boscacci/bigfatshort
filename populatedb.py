from things_to_import import *

with open('BLS_data_edu.json') as BLS_data:
    data_edu = json.load(BLS_data)
with open('BLS_data_housing.json') as BLS_data:
    data_housing = json.load(BLS_data)
with open('BLS_data_income_quants.json') as BLS_data:
    data_income = json.load(BLS_data)

engine = create_engine('sqlite:///blsdata.db')

# Base.metadata.create_all(engine)

data_edu_table = []
for year in data_edu.keys():
    for edu_level in data_edu[year]:
        row = By_Edu(income = data_edu[year][edu_level]['INCAFTTX'][0])
        row.edu_level = int(edu_level)
        row.year = int(year)
        row.housing = data_edu[year][edu_level]['HOUSING'][0]
        row.foodhome = data_edu[year][edu_level]['FOODHOME'][0]
        row.foodaway = data_edu[year][edu_level]['FOODAWAY'][0]
        row.health = data_edu[year][edu_level]['HEALTH'][0]
        row.alcbevg = data_edu[year][edu_level]['ALCBEVG'][0]
        row.apparel = data_edu[year][edu_level]['APPAREL'][0]
        row.trans = data_edu[year][edu_level]['TRANS'][0]
        row.entrtain = data_edu[year][edu_level]['ENTRTAIN'][0]
        data_edu_table.append(row)

data_housing_table = []
for year in data_housing.keys():
    for housing_type in data_housing[year]:
        row = By_Housing()
        row.housing_type = int(housing_type)
        row.year = int(year)
        try:
            row.housing = data_housing[year][housing_type]['HOUSING'][0]
        except IndexError:
            row.housing = None
        try:
            row.income = data_edu[year][housing_type]['INCAFTTX'][0]
        except KeyError:
            row.income = None
        try:
            row.foodhome = data_housing[year][housing_type]['FOODHOME'][0]
        except IndexError:
            row.foodhome = None
        try:
            row.foodaway = data_housing[year][housing_type]['FOODAWAY'][0]
        except IndexError:
            row.foodaway = None
        try:
            row.health = data_housing[year][housing_type]['HEALTH'][0]
        except IndexError:
            row.health = None
        try:
            row.alcbevg = data_housing[year][housing_type]['ALCBEVG'][0]
        except IndexError:
            row.alcbevg = None
        try:
            row.apparel = data_housing[year][housing_type]['APPAREL'][0]
        except IndexError:
            row.apparel = None
        try:
            row.trans = data_housing[year][housing_type]['TRANS'][0]
        except IndexError:
            row.trans = None
        try:
            row.entrtain = data_housing[year][housing_type]['ENTRTAIN'][0]
        except IndexError:
            row.entrtain = None
        data_housing_table.append(row)

gdp_year_table = []
gdp_list = get_usa_gdp_per_cap()
for year in gdp_list.keys():
    row = GDP_Percap(year = int(year), gdp = float(gdp_list[year]))
    gdp_year_table.append(row)

Session = sessionmaker(bind=engine)
session = Session()
#add and commit the actors and roles below
session.add_all(gdp_year_table)
session.add_all(data_edu_table)
session.add_all(data_housing_table)
session.commit()
