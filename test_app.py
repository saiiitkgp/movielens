import pandas as pd
from flask import Flask, abort, send_file, request, render_template

app = Flask(__name__)

@app.route("/")
def base():
    return render_template('frontPage.html')

app.run(host='127.0.0.1', port=7500)
