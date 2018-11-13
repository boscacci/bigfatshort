from pkg import db

class By_Edu(db.Model):
    __tablename__ = 'by_edu'
    id = db.Column(db.Integer, primary_key = True)
    year = db.Column(db.Integer)
    edu_level = db.Column(db.Integer)
    income = db.Column(db.Integer)
    housing = db.Column(db.Integer)
    foodhome = db.Column(db.Integer)
    foodaway = db.Column(db.Integer)
    health = db.Column(db.Integer)
    alcbevg = db.Column(db.Integer)
    apparel = db.Column(db.Integer)
    trans = db.Column(db.Integer)
    entrtain = db.Column(db.Integer)

class By_Housing(db.Model):
    __tablename__ = 'by_housing'
    id = db.Column(db.Integer, primary_key = True)
    year = db.Column(db.Integer)
    housing_type = db.Column(db.Integer)
    income = db.Column(db.Integer)
    housing = db.Column(db.Integer)
    foodhome = db.Column(db.Integer)
    foodaway = db.Column(db.Integer)
    health = db.Column(db.Integer)
    alcbevg = db.Column(db.Integer)
    apparel = db.Column(db.Integer)
    trans = db.Column(db.Integer)
    entrtain = db.Column(db.Integer)

class By_Income(db.Model):
    __tablename__ = 'by_income'
    id = db.Column(db.Integer, primary_key = True)
    year = db.Column(db.Integer)
    income_quintile = db.Column(db.Integer)
    income = db.Column(db.Integer)
    housing = db.Column(db.Integer)
    foodhome = db.Column(db.Integer)
    foodaway = db.Column(db.Integer)
    health = db.Column(db.Integer)
    alcbevg = db.Column(db.Integer)
    apparel = db.Column(db.Integer)
    trans = db.Column(db.Integer)
    entrtain = db.Column(db.Integer)

class GDP_Percap(db.Model):
    __tablename__ = 'gdp_percap'
    id = db.Column(db.Integer, primary_key = True)
    year = db.Column(db.Integer)
    gdp = db.Column(db.Integer)

