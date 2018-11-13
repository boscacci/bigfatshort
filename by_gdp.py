from get_usa_gdp import *
from sqlalchemy import *

gdps = get_usa_gdp_per_cap()

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class GDP_Percap(Base):
    __tablename__ = 'gdp_percap'
    id = Column(Integer, primary_key = True)
    year = Column(Integer)
    gdp = Column(Integer)

engine = create_engine('sqlite:///blsdata.db')
Base.metadata.create_all(engine)
