from flask import Flask, render_template, redirect, url_for, request
#from flask_bootstrap import Bootstrap5
import requests
from datetime import datetime

year = datetime.now().year

app = Flask(__name__)

@app.route("/")
def home():
    quote_response = requests.get("https://zenquotes.io/api/random")
    qoute_data = quote_response.json()
    
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)