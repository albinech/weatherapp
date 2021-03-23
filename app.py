from flask import Flask, url_for, render_template
import requests
import pprint
import _sqlite3
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///weather.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50))


@app.route('/')
def index():
    url = 'http://api.openweathermap.org/data/2.5/forecast?id={}&appid=32e8f4d6978d4230f29e7f4ca779f572'
    id = '7667580'
    city = 'gurjaani'
    r = requests.get(url.format(id)).json()
    pprint.pprint(r)

    weather = {
        'City': city,
        'Temp': round((r['list'][2]['main']['temp']) - 273.15, 2),
        'Desc': r['list'][0]['main'],
        'Icon': r['list'][1]['weather'][0]['icon']
    }
    print(weather['Desc'])
    return render_template('weather.html', weath=weather)
#city=weather['City'], temp=weather['Temp'], desc=weather['Desc'],
                           #icon=weather['Icon']
