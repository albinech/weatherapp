from flask import Flask, url_for, render_template, request
import requests
import pprint
import _sqlite3
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
# db = SQLAlchemy(app)
#
#
# class City(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50))



@app.route('/', methods=['GET','POST'])
def index():
    url = 'http://api.openweathermap.org/data/2.5/forecast?id={}&appid=32e8f4d6978d4230f29e7f4ca779f572'

    cities = [611717, 7667581, 7667580, 613607]

    weather_data = []
    for city in cities:
        r = requests.get(url.format(city)).json()
        weather = {
            'City': r['city']['name'],
            'Temp_0000': round((r['list'][0]['main']['temp']) - 273.15, 2),
            'Temp_0006': round((r['list'][2]['main']['temp']) - 273.15, 2),
            'Temp_0012': round((r['list'][4]['main']['temp']) - 273.15, 2),
            'Temp_0018': round((r['list'][6]['main']['temp']) - 273.15, 2),
            'Desc': r['list'][0]['main'],
            'Icon1': r['list'][0]['weather'][0]['icon'],
            # same keys in json "weater" key access only first element in dict.
            # 'Icon2': r['list'][0]['weather'][0]['icon'],
            # 'Icon3': r['list'][0]['weather'][0]['icon'],
            # 'Icon4': r['list'][0]['weather'][0]['icon']
        }
        weather_data.append(weather)
        pprint.pprint(r)
    pprint.pprint(weather_data)
    return render_template('weather.html', weather_data=weather_data)
# city=weather['City'], temp=weather['Temp'], desc=weather['Desc'],
# icon=weather['Icon']
