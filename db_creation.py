import pyodbc
import pandas as pd
import sqlalchemy as sa
from sqlalchemy import create_engine, event
from sqlalchemy import Column, Integer, String, Float, TIMESTAMP, Index
from sqlalchemy.ext.declarative import declarative_base

def format_title(text):
	"""
	Handle any unicode character present in the movie title
	"""
	return text.replace(u"\xa0", u" ")

def split_title(title):
    """
    Splits the year from the movie title
    """
    year = None
    title = title.strip()
    if title[-6:].strip("()").isnumeric():
        year = int(title[-6:].strip("()"))
        title = title[:-6].strip()
    return title, year

def convert_genres(genre):
	if genre == "(no genres listed)":
		genres = ["No-Genre"]
	else:
		genres = genre.split("|")
	return genres

data = r"ml-25m/movies.csv"
movies_df = pd.read_csv(data)
movies_df["title"] = movies_df["title"].apply(format_title)
movies_df["year"]  = movies_df["title"].apply(split_title).apply(lambda x:x[1]).astype('Int64')
movies_df["genres"] = movies_df["genres"].apply(convert_genres).astype(str)

engine = sa.create_engine('mssql+pyodbc://DESKTOP-GG7MN0N/movielensdb?driver=SQL+Server+Native+Client+11.0',echo = False, fast_executemany = True)

Base = declarative_base()

class Movies(Base):
   __tablename__ = 'movies'
   movieId = Column(Integer, primary_key=True, index = True, unique = True, autoincrement=False)
   title = Column(String)
   genres = Column(String(200), index = True)
   year = Column(String)


class Ratings(Base):
   __tablename__ = 'ratings'
   id = Column(Integer, primary_key=True, autoincrement=True)
   userId = Column(Integer)
   movieId = Column(Integer, index = True)
   rating = Column(Float, index = True)
   timestamp = Column(Integer)

Base.metadata.create_all(engine)

movies_df.to_sql('random_1', engine, index=False, if_exists="replace", schema="dbo", chunksize=1000)

ratings_df = pd.read_csv(r"ml-25m/ratings.csv")
ratings_df.to_sql('ratings', engine, index=False, if_exists="replace", schema="dbo", chunksize=10000)
