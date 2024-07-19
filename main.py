from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
import requests
from datetime import datetime

year = datetime.now().year

app = Flask(__name__)

@app.route("/")
def home():
    pass


if __name__ == '__main__':
    app.run(debug=True)