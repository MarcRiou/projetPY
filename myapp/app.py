from flask import Flask, render_template
from Data.pictures import pictures as pictures_data
from Data.pictures import pictures
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html', pictures=pictures)

@app.route("/picture")
def HomePicture():
    return render_template('index.html', pictures=pictures)

@app.route("/picture/<pictures_id>")
def showPictures(pictures_id):
    id = int(pictures_id) 
    picture = None

    if 0 <= id < len(pictures_data):
        pictures = pictures_data[id]

    return render_template('picture.html', picture=pictures)