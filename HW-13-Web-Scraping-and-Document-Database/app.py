from flask import Flask, render_template, jsonify, redirect
import pymongo
import scrape_mars

# Create an instance of our Flask app.
app = Flask(__name__)

# Create connection variable
conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
db = client.mars_db


@app.route("/")
def home():
    info = db.mars_d.find_one()
    return render_template("index.html", info=info)
  

@app.route("/scrape")
def scrape():
    db.mars_d.drop()
    mars=scrape_mars.scrape()
    db.mars_d.insert_one(mars)
    # Redirect back to home page
    return redirect("http://localhost:5000/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
