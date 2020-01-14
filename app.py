import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask (__name__)

app.config["MONGO_DBNAME"] = 'travel_diary'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)



@app.route('/')
@app.route('/get_chapters')
def get_chapters():
    return render_template("chapters.html", chapters= mongo.db.chapters.find())
    
@app.route('/add_chapter')
def add_chapter():
    return render_template("addchapter.html", countries = mongo.db.countries.find())

@app.route('/insert_chapter', methods=['POST'])
def insert_chapter():
    chapters = mongo.db.chapters
    chapters.insert_one(request.form.to_dict())
    return redirect(url_for('get_chapters'))

@app.route('/add_country')
def add_country():
    return render_template('addcountry.html')

    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            