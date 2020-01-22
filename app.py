import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import json

app = Flask (__name__)

app.config["MONGO_DBNAME"] = 'travel_diary'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)



@app.route('/')
@app.route('/get_chapters')
def get_chapters():
    placeholder = "https://via.placeholder.com/200x299.png?text=No+image+found";
    return render_template("chapters.html", chapters= mongo.db.chapters.find(), placeholder=placeholder)
    
@app.route('/add_chapter')
def add_chapter():
    return render_template("addchapter.html", countries = mongo.db.countries.find())

@app.route('/insert_chapter', methods=['POST'])
def insert_chapter():
    chapters = mongo.db.chapters
    chapters.insert_one(request.form.to_dict())
    return redirect(url_for('get_chapters'))

@app.route('/edit_chapter/<chapter_id>')
def edit_chapter(chapter_id):
    the_chapter = mongo.db.chapters.find_one({"_id": ObjectId(chapter_id)})
    the_countries = mongo.db.countries.find()
    return render_template('editchapter.html', chapter = the_chapter, countries= the_countries)    

@app.route('/update_chapter/<chapter_id>', methods=['POST'])
def update_chapter(chapter_id):
    chapters = mongo.db.chapters
    chapters.update({'_id': ObjectId(chapter_id)},
    {
        'title':request.form.get('title'),
        'country_name':request.form.get('country_name'),
        'city_name':request.form.get('city_name'),
        'story': request.form.get('story'),
        'start_date': request.form.get('start_date'),       
        'end_date': request.form.get('end_date'),
        'main_photo':request.form.get('main_photo')   
    })
    return redirect(url_for('get_chapters'))
    
@app.route('/delete_chapter/<chapter_id>')
def delete_chapter(chapter_id):
    mongo.db.chapters.remove({'_id': ObjectId(chapter_id)})
    return redirect(url_for('get_chapters'))

@app.route('/get_countries')
def get_countries():
    return render_template('countries.html', countries = mongo.db.countries.find())
    
@app.route('/edit_country/<country_id>')
def edit_country(country_id):
    return render_template('editcountry.html', country=mongo.db.countries.find_one({'_id': ObjectId(country_id)}))
    
@app.route('/update_country/<country_id>', methods=["POST"])
def update_country(country_id):
    mongo.db.countries.update(
        {'_id':ObjectId(country_id)},
        {'country_name': request.form.get('country_name')})
    return redirect(url_for('get_countries'))

@app.route('/delete_country/<country_id>')
def delete_country(country_id):
    mongo.db.countries.remove({'_id': ObjectId(country_id)})
    return redirect(url_for('get_countries'))

@app.route('/insert_country', methods=["POST"])
def insert_country():
    country_doc = {'country_name': request.form.get('country_name')}
    mongo.db.countries.insert_one(country_doc)
    return redirect(url_for('get_countries'))


@app.route('/add_country')
def add_country():
    return render_template('addcountry.html')


@app.route('/get_locations')
def get_locations():
    return render_template('locations.html', chapters =mongo.db.chapters.find())
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            