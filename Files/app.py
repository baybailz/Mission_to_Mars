# imports
from flask import Flask, render_template, jsonify, redirect
import pymongo
import scrape_mars

#setting up flask 
app = Flask(__name__)

# mongo
client = pymongo.MongoClient()
db = client.mars_db
collection = db.mars_data

# routes
@app.route("/")
def index():
    mars = db.mars.find_one()
    return render_template("index.html", mars=mars)


@app.route("/scrape")
def scrape():
    mars = db.mars
    mars_data = scrape_mars.scrape()
    mars.update(
        {},
        mars_data,
        upsert=True
    )
    return redirect("http://localhost:5000/", code=302)


if __name__ == "__main__":
    app.run(debug=True)