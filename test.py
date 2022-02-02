import pyodbc
import pandas as pd
import json
import sqlalchemy as sa
from flask import Flask, abort, send_file, request, render_template


driver = 'SQL Server'
server = 'DESKTOP-GG7MN0N'
db1 = 'testdb1'
tcon = 'yes'

conn = pyodbc.connect(driver='{SQL Server}', host=server, database=db1,
                      trusted_connection=tcon)

cursor = conn.cursor()


conn = pyodbc.connect(driver='{SQL Server}', host=server, database=db1,
                      trusted_connection=tcon)
query1 = """create or alter view recommendation as
select distinct b.userId, b.movieId from ratings b 
join 
(select userId, movieId, rating from ratings where userId = 7) c on c.movieId = b.movieId and 
c.rating = b.rating"""
cursor.execute(query1)

print("1")
query2 = """select distinct movieId from
(select distinct a.userId, a.movieId from ratings a join
(select distinct userId from recommendation ) b on a.userId = b.userId) c where not exists 
(select userId, movieId from recommendation d where c.userId = d.userId and 
c.movieId = d.movieId ) """
print("2")
cursor.execute(query2)
res = cursor.fetchall()
#data = pd.read_sql(query2, conn)
print(list(res))
#data = json.loads(data.to_json(orient ='records'))
#print(type(data))
conn.close()

#print(data)

