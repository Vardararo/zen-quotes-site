'''A simple web application that presents random quotes from famous people
along with beautiful landscape images'''

from datetime import datetime
import os
from flask import Flask, render_template
import requests
from dotenv import load_dotenv


load_dotenv(".env")

# Pulling movie data from The Movie Database using the TMDB API
ACCESS_KEY = os.environ.get("Unsplash_API_Key")

ZEN_API = "https://zenquotes.io/api/random"
UNSPLASH_API = "https://api.unsplash.com/"

year = datetime.now().year

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    '''API calls required to get the quotes and the images from respective sources'''

    # Zen Quotes API call
    quote_response = requests.get(ZEN_API, timeout=10)
    quote_data = quote_response.json()

    author = quote_data[0]["a"]
    quote = quote_data[0]["q"]

    # Unsplash API call
    header = {
        "Accept-Version": "v1",
        "Authorization": f"Client-ID {ACCESS_KEY}"
    }
    params = {
        "query": "landscape",
        "orientation": "landscape"
    }
    image_response = requests.get(
        f"{UNSPLASH_API}/photos/random", headers=header, params=params, timeout=10)
    image_data = image_response.json()

    img_author = image_data["user"]["name"]
    img_author_link = image_data["user"]["links"]["html"]
    img_link = image_data["urls"]["full"]

    return render_template("index.html", copyright_year=year, quote=quote, author=author,
                           img_author=img_author, img_link=img_link, link=img_author_link)


if __name__ == '__main__':
    app.run(debug=True)

# End-of-file (EOF)
