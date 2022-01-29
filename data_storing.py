import pyodbc
import pandas as pd
import sqlalchemy as sa
from sqlalchemy import create_engine, event, text
from sqlalchemy import Column, Integer, String, ForeignKey, Float
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

"""
# Path for dataset
data = r"ml-25m/movies.csv"
movies_df = pd.read_csv(data)
movies_df["title"] = movies_df["title"].apply(format_title)
movies_df["year"]  = movies_df["title"].apply(split_title)
movies_df["title"] = movies_df["title"].apply(split_title)
movies_df["title"]  = movies_df["title"].apply(lambda num : str(num[0]))
movies_df["year"]  = movies_df["year"].apply(lambda num : str(num[1]))
movies_df["genres"] = movies_df["genres"].apply(convert_genres)
#movies_df["year"]  = movies_df["year"].astype(int)
#print(movies_df["year"][movies_df["year"].isnull()])
#print(movies_df.describe())
#print(type(movies_df["year"][0]))
#print(type(movies_df["movieId"].loc[0]))
#print(movies_df)

ratings_df = pd.read_csv(r'ml-25m/ratings.csv')
#print(ratings_df)
print(len(ratings_df))

engine = sa.create_engine('mssql+pyodbc://DESKTOP-GG7MN0N/movielensdb?driver=SQL+Server+Native+Client+11.0',echo = False, fast_executemany=True)
#engine = sa.create_engine('mssql+pyodbc://DESKTOP-GG7MN0N/movielens_db?driver=SQL Server?Trusted_Connection=yes')
#engine = create_engine('mssql+pyodbc://localhost:8080/movie_db')
ratings_df.to_sql('ratings', con = engine, if_exists = 'append', index = False)


@event.listens_for(engine, 'before_cursor_execute')
def receive_before_cursor_execute(conn, cursor, statement, params, context, executemany):
    print("FUNC call")
    if executemany:
        cursor.fast_executemany = True


Base = declarative_base()

class Movies(Base):
   __tablename__ = 'movies'
   movieId = Column(Integer, primary_key=True, autoincrement=False)
   title = Column(String)
   genres = Column(String)
   year = Column(String)

Base.metadata.create_all(engine)
conn = engine.connect()
cursor = conn.cursor()
cursor.fast_executemany = True

#movies_df.to_sql('movies', con = engine, if_exists = 'append', index = False)

import re
from tqdm import tqdm
import urllib.request
from dask import dataframe as dd
from collections import defaultdict
from typing import List, Tuple, Dict, Any
from pyravendb.store.document_store import DocumentStore, DocumentSession



title = movies_df["title"][0]

row = movies_df[movies_df["movieId"]== 209171]
print(type(row["genres"].iloc[0]))


if row["genres"].iloc[0] == "(no genres listed)":
    genres = ["No-Genre"]
else:
    genres = row["genres"].iloc[0].split("|")
print(genres)

"""

"""

driver = 'SQL Server'
server = 'DESKTOP-GG7MN0N'
db1 = 'movielensdb'
tcon = 'yes'

conn = pyodbc.connect(driver='{SQL Server}', host=server, database=db1,
                      trusted_connection=tcon)

ratings_df = pd.read_csv(r'ml-25m/ratings.csv')
cursor = conn.cursor()
#cursor.execute("SELECT * FROM movies") 
for _, row in ratings_df.iterrows():
    #print(type(row))
    #print(row[0], row[1], row[2], row[3])
    #print(tuple(row))
    row = [tuple(row)]
    cursor.executemany('INSERT INTO [ratings] (userId, movieId, rating, timestamp) VALUES (?, ?, ?, ?)', row)
cursor.commit()
conn.close()  
"""
"""
from sqlalchemy import event
ratings_df = pd.read_csv(r'ml-25m/ratings.csv')
engine = sa.create_engine('mssql+pyodbc://DESKTOP-GG7MN0N/moviedb?driver=SQL+Server+Native+Client+11.0',echo = False)
@event.listens_for(engine, "before_cursor_execute")
def receive_before_cursor_execute(
       conn, cursor, statement, params, context, executemany
        ):
            if executemany:
                cursor.fast_executemany = True

ratings_df.to_sql('ratings', engine, index=False, if_exists="append", schema="dbo", chunksize=10000)
"""

import numpy as np
import pandas as pd
import sqlalchemy as sa

engine = sa.create_engine('mssql+pyodbc://DESKTOP-GG7MN0N/testdb1?driver=SQL+Server+Native+Client+11.0',echo = False, fast_executemany=True)

"""
Base = declarative_base()

class Movies(Base):
   __tablename__ = 'movies'
   movieId = Column(Integer, primary_key=True, index = True, unique = True, autoincrement=False)
   title = Column(String(200))

class Genres(Base):
   __tablename__ = 'genres'
   genreId = Column(Integer, primary_key=True, autoincrement=True)
   genre = Column(String(200))

class Movies_Genres(Base):
   __tablename__ = 'movie_genres'
   id = Column(Integer, primary_key = True, autoincrement=True)
   movieId = Column(Integer, ForeignKey('movies.movieId'))
   genreId = Column(Integer, ForeignKey('genres.genreId'))

class Ratings(Base):
   __tablename__ = 'ratings'
   id = Column(Integer, primary_key=True, index = True, unique = True, autoincrement=True)
   userId = Column(Integer)
   movieId = Column(Integer, ForeignKey('movies.movieId'), index = True)
   rating = Column(Float, index = True)
   timestamp = Column(Integer)

Base.metadata.create_all(engine)
"""
"""
Base = declarative_base()

class Movies(Base):
   __tablename__ = 'movies'
   movieId = Column(Integer, primary_key=True, index = True, unique = True, autoincrement=False)
   title = Column(String)
   genres = Column(String(200))
   year = Column(String)


class Ratings(Base):
   __tablename__ = 'ratings'
   id = Column(Integer, primary_key=True, autoincrement=True)
   userId = Column(Integer)
   movieId = Column(Integer, ForeignKey('movies.movieId'), index = True)
   rating = Column(Float, index = True)
   timestamp = Column(Integer)

Base.metadata.create_all(engine)
"""
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

"""
data = r"ml-25m/movies.csv"
movies_df = pd.read_csv(data)
movies_df["title"] = movies_df["title"].apply(format_title)
movies_df["year"]  = movies_df["title"].apply(split_title).apply(lambda x:x[1]).astype('Int64')
movies_df["genres"] = movies_df["genres"].apply(convert_genres).astype(str)

movies_df.to_sql('movies', engine, index=False, if_exists="append", schema="dbo", chunksize=1000)


ratings_df = pd.read_csv(r"ml-25m/ratings.csv")
ratings_df.to_sql('ratings', engine, index=False, if_exists="append", schema="dbo", chunksize=10000)
"""
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)
session = Session()
#print(list(session.query(Movies).from_statement(text("SELECT * FROM movies")).all()))

"""
conn = engine.connect()
result = conn.execute(Movies.select())

for row in result:
   print (row)
"""
#stmt = text("select distinct a.*, ((c.Avg_Rating * c.User_Count) + 6) / fake as L_Rating, User_Count from movies a left join ratings b on (a.movieId = b.movieId) left join (select movieId, count(userId) User_Count, count(userId) +2 as fake, avg(rating) Avg_Rating from ratings group by movieId ) c on (a.movieId = c.movieId) where genres like '%Romance%' or genres like '%Drama%' order by L_Rating  desc ")
#for cust in session.query(Movies, Ratings).from_statement(stmt).all():
 #   print(cust.title)

#stmt = "select distinct a.*, ((c.Avg_Rating * c.User_Count) + 6) / fake as L_Rating, User_Count from movies a left join ratings b on (a.movieId = b.movieId) left join (select movieId, count(userId) User_Count, count(userId) +2 as fake, avg(rating) Avg_Rating from ratings group by movieId ) c on (a.movieId = c.movieId) where genres like '%Romance%' or genres like '%Drama%' order by L_Rating  desc "

# Connecting to Database
driver = 'SQL Server'
server = 'DESKTOP-GG7MN0N'
db1 = 'testdb1'
tcon = 'yes'

conn = pyodbc.connect(driver='{SQL Server}', host=server, database=db1,
                      trusted_connection=tcon)

#cursor = conn.cursor()
#cursor.execute("select * from movies") 

title = "Toy Story"
sql = "select * from movies where title like '"+"%"+title+"%'"
data = pd.read_sql(sql, conn)
data = data.to_json(orient ='records')
print(data)
conn.close()
