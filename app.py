import pyodbc
import pandas as pd
import sqlalchemy as sa
from flask import Flask, abort, send_file, request

app = Flask(__name__)

driver = 'SQL Server'
server = 'DESKTOP-GG7MN0N'
db1 = 'testdb1'
tcon = 'yes'

conn = pyodbc.connect(driver='{SQL Server}', host=server, database=db1,
                      trusted_connection=tcon)

cursor = conn.cursor()

@app.route("/", methods=['GET'])
def base():
    conn = pyodbc.connect(driver='{SQL Server}', host=server, database=db1,
                      trusted_connection=tcon)
    query = """select title, year, genres, L_Rating, No_of_Reviews from (
                select distinct a.*, ((c.Avg_Rating * c.User_Count) + 6) / (c.User_Count+2) as L_Rating, 
                c.User_Count as No_of_Reviews from movies a
                left join ratings b on (a.movieId = b.movieId)
                left join 
                (select movieId, count(userId) User_Count, avg(rating) Avg_Rating from ratings group by 
                movieId ) c on (a.movieId = c.movieId) ) as c order by L_Rating desc """
    data = pd.read_sql(query, conn)
    data = data.to_json(orient ='records')
    conn.close()
    return data

@app.route("/search_by_title", methods = ['POST'])
def search_by_title():
    conn = pyodbc.connect(driver='{SQL Server}', host=server, database=db1,
                      trusted_connection=tcon)
    request_data = request.get_json()
    title = str(request_data["title"])
    query = """ select title, year, genres, L_Rating, No_of_Reviews from (
                select distinct a.*, ((c.Avg_Rating * c.User_Count) + 6) / (c.User_Count+2) as L_Rating, 
                c.User_Count as No_of_Reviews from movies a
                left join ratings b on (a.movieId = b.movieId)
                left join 
                (select movieId, count(userId) User_Count, avg(rating) Avg_Rating from ratings group by 
                movieId ) c on (a.movieId = c.movieId) ) as c where title like '%""" +title+"""%' 
                order by L_Rating desc """ 
    data = pd.read_sql(query, conn)
    data = data.to_json(orient ='records')
    conn.close()
    return data

@app.route("/filter_by_genres", methods = ['POST'])
def filter_by_genres():
    conn = pyodbc.connect(driver='{SQL Server}', host=server, database=db1,
                      trusted_connection=tcon)
    request_data = request.get_json()
    genres = request_data["genres"]
    query = """select distinct a.*, ((c.Avg_Rating * c.User_Count) + 6) / fake as L_Rating,
            User_Count from movies a left join ratings b on (a.movieId = b.movieId) left join
            (select movieId, count(userId) User_Count, count(userId) +2 as fake, avg(rating) Avg_Rating 
            from ratings group by movieId ) c on (a.movieId = c.movieId) where """ + genres + """
            order by L_Rating  desc """
    
    data = pd.read_sql(query, conn)
    data = data.to_json(orient ='records')
    conn.close()
    return data

@app.route("/similar_users", methods = ['POST'])
def similar_users():
    conn = pyodbc.connect(driver='{SQL Server}', host=server, database=db1,
                      trusted_connection=tcon)
    request_data = request.get_json()
    #print(request_data)
    rating = str(request_data["rating"])
    movieId = str(request_data["movieId"])
    genres = str(request_data["genres"])
    query = """ select count(userId) as count from movies a 
                left join ratings b on (a.movieId = b.movieId) where genres ='""" + genres + """'
                and rating =""" + rating +""" and a.movieId =""" + movieId + """ group by a.movieId, genres, rating  """
    data = pd.read_sql(query, conn)
    data = data.to_json(orient ='records')
    conn.close()
    return data
    

#stmt = "select distinct a.*, ((c.Avg_Rating * c.User_Count) + 6) / fake as L_Rating, User_Count from movies a left join ratings b on (a.movieId = b.movieId) left join (select movieId, count(userId) User_Count, count(userId) +2 as fake, avg(rating) Avg_Rating from ratings group by movieId ) c on (a.movieId = c.movieId) where genres like '%Romance%' or genres like '%Drama%' order by L_Rating  desc "



app.run(host='127.0.0.1', port=7000)
