from config.database import Base
from sqlalchemy import Column, Integer, String, Float

class Movie(Base):

    __tablename__ = "movies"

    id = Column(Integer, primary_key = True)
    tittle = Column(String)
    review = Column(String)
    year = Column(Integer)
    ranking = Column(Float)
    category = Column(String)