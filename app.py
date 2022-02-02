import pyodbc
import pandas as pd
import json
import sqlalchemy as sa
from flask import Flask, abort, send_file, request, render_template


limitNumFromPy=7 #limit number variable
similarUserGenreHiddenFromPy="" #genre variable in similar users
similarUserRatingHiddenFromPy="" #rating in similar users
similarUserMovieIdHiddenFromPy="" #movie id in similar users
recommend=""  #recommend variable
similarUserCount="" #similar user count



genreList=[{'val':"Action","flag":False},{"val":"Adventure","flag":False},{"val":"Animation","flag":True}, {'val':"Children","flag":False},
{'val':"Comedy","flag":False}, {'val':"Crime","flag":False}, {'val':"Documentary","flag":False}, {'val':"Drama","flag":False},
{'val':"Fantasy","flag":False}, {'val':"Film-Noir","flag":False}, {'val':"Horror","flag":False}, {'val':"IMAX","flag":False},
{'val':"Musical","flag":False}, {'val':"Mystery","flag":False}, {'val':"Romance","flag":False},
{'val':"Sci-Fi","flag":False}, {'val':"Thriller","flag":False}, {'val':"War","flag":False}, {'val':"Western","flag":False}]

genreListSimilarUser=[{'val':"Action","flag":False},{"val":"Adventure","flag":False},{"val":"Animation","flag":True}, {'val':"Children","flag":False},
{'val':"Comedy","flag":False}, {'val':"Crime","flag":False}, {'val':"Documentary","flag":False}, {'val':"Drama","flag":False},
{'val':"Fantasy","flag":False}, {'val':"Film-Noir","flag":False}, {'val':"Horror","flag":False}, {'val':"IMAX","flag":False},
{'val':"Musical","flag":False}, {'val':"Mystery","flag":False}, {'val':"Romance","flag":False},
{'val':"Sci-Fi","flag":False}, {'val':"Thriller","flag":False}, {'val':"War","flag":False}, {'val':"Western","flag":False}]

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
    query = """select  top 20 title, year, genres, isnull ( cast (((c.Avg_Rating * c.User_Count) + 6) / (c.User_Count+2) as decimal (10,3)), 0) as L_Rating, 
                isnull(c.User_Count, 0) as No_of_Reviews from movies a
                left join 
                (select movieId, count(userId) User_Count, avg(rating) Avg_Rating from ratings group by 
                movieId ) c on (a.movieId = c.movieId) order by L_Rating desc, No_of_Reviews desc """
    data = pd.read_sql(query, conn)
    data = json.loads(data.to_json(orient ='records'))
    conn.close()
    return render_template('frontPage.html', table_contentFromPy = data, genreList=genreList, limitNumFromPy=limitNumFromPy,similarUserGenreHiddenFromPy=similarUserGenreHiddenFromPy,similarUserRatingHiddenFromPy=similarUserRatingHiddenFromPy,similarUserMovieIdHiddenFromPy=similarUserMovieIdHiddenFromPy,recommend=recommend,similarUserCount=similarUserCount, genreListSimilarUser = genreListSimilarUser) 

@app.route("/search_by_title", methods = ['POST'])
def search_by_title():
    conn = pyodbc.connect(driver='{SQL Server}', host=server, database=db1,
                      trusted_connection=tcon)
    title = str(request.form.get("title"))
    query = """ select  title, year, genres, isnull ( cast (((c.Avg_Rating * c.User_Count) + 6) / (c.User_Count+2) as decimal (10,3)), 0) as L_Rating, 
                isnull(c.User_Count, 0) as No_of_Reviews from movies a
                left join 
                (select movieId, count(userId) User_Count, avg(rating) Avg_Rating from ratings group by 
                movieId ) c on (a.movieId = c.movieId) where replace("""+title+""", ' ','') like '%""" +title+"""%'   order by L_Rating desc, No_of_Reviews desc """ 
    data = pd.read_sql(query, conn)
    data = json.loads(data.to_json(orient ='records'))
    conn.close()
    return data



@app.route("/search_filter_by_genres", methods = ['POST'])
def search_filter_by_genres():
    flag= request.form.get("buttonFlag")
    if flag=="filter":
        data = filter_by_genres(request.form.get("genreString"), request.form.get("recordLimit"))
        return render_template('frontPage.html', table_contentFromPy = data, genreList=genreList, limitNumFromPy=limitNumFromPy,similarUserGenreHiddenFromPy=similarUserGenreHiddenFromPy,similarUserRatingHiddenFromPy=similarUserRatingHiddenFromPy,similarUserMovieIdHiddenFromPy=similarUserMovieIdHiddenFromPy,recommend=recommend,similarUserCount=similarUserCount, genreListSimilarUser = genreListSimilarUser) 
    else:
        data = similar_users(str(request.form.get("similarUserMovieId")), (request.form.get("similarUserGenreHidden")),
                                                str(request.form.get("similarUserRatingHidden")))
        print(data)
        return render_template('frontPage.html', table_contentFromPy = data, genreList=genreList, limitNumFromPy=limitNumFromPy,similarUserGenreHiddenFromPy=similarUserGenreHiddenFromPy,similarUserRatingHiddenFromPy=similarUserRatingHiddenFromPy,similarUserMovieIdHiddenFromPy=similarUserMovieIdHiddenFromPy,recommend=recommend,similarUserCount=data[0]["count"], genreListSimilarUser = genreListSimilarUser) 
    



#@app.route("/filter_by_genres", methods = ['POST'])
def filter_by_genres(genres, limitNumFromPy):
    conn = pyodbc.connect(driver='{SQL Server}', host=server, database=db1,
                      trusted_connection=tcon)
    request_data = request.get_json()
    genres = str(genres)
    limitNumFromPy = str(limitNumFromPy)
    query = """select  top """ +limitNumFromPy+""" title, year, genres, isnull ( cast (((c.Avg_Rating * c.User_Count) + 6) / (c.User_Count+2) as decimal (10,3)), 0) as L_Rating, 
                isnull(c.User_Count, 0) as No_of_Reviews from movies a
                left join 
                (select movieId, count(userId) User_Count, avg(rating) Avg_Rating from ratings group by 
                movieId ) c on (a.movieId = c.movieId) where """ + genres + """   
				order by L_Rating desc, No_of_Reviews desc """
    
    data = pd.read_sql(query, conn)
    data = json.loads(data.to_json(orient ='records'))
    conn.close()
    return data

#@app.route("/similar_users", methods = ['POST'])
def similar_users(similarUserMovieId,similarUserGenreHidden, similarUserRatingHidden ):
    conn = pyodbc.connect(driver='{SQL Server}', host=server, database=db1,
                      trusted_connection=tcon)
    rating = str(similarUserRatingHidden)
    movieId = str(similarUserMovieId)
    genres = str(similarUserGenreHidden)
    print(genres)
    #print(similarUserMovieId,similarUserGenreHidden, similarUserRatingHidden)
    query = """ select count(userId) as count from movies a 
                left join ratings b on (a.movieId = b.movieId) where genres =""" + genres + """
                and rating =""" + rating +""" and a.movieId =""" + movieId + """ group by a.movieId, genres, rating  """
    data = pd.read_sql(query, conn)
    data = json.loads(data.to_json(orient ='records'))
    conn.close()
    return data



    



app.run(host='127.0.0.1', port=7000)
