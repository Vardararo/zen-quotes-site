from flask import Flask, render_template, redirect, url_for, request
#from flask_bootstrap import Bootstrap5
import requests
from datetime import datetime

year = datetime.now().year

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    quote_response = requests.get("https://zenquotes.io/api/random")
    quote_data = quote_response.json()
    
    author = quote_data[0]["a"]
    quote = quote_data[0]["q"]
    
    return render_template("index.html", copyright_year = year, quote = quote, author = author)


if __name__ == '__main__':
    app.run(debug=True)