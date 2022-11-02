import requests
from datetime import datetime, timedelta
import json

from flask import Flask, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy


API_KEY = '885ecc867a79badd4fb4eeab38215d4a'
### set delta to 2 hours, following point (4) in the readme (note this seems slightly at odds with point (3) which
### says 4 hours
delta = timedelta(hours=2)

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    time = db.Column(db.DateTime, nullable=False, default=datetime.now())
    temperature = db.Column(db.Integer, nullable=False)

with app.app_context():
    db.create_all()

def get_weather_data(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    response = requests.get(url).json()
    return response


@app.route('/', methods=['POST'])
def check_weather():

    # parse city from json
    content = request.json
    # try:
    city = content['city']
    # # todo: handle error where no 'city' key
    # except:
    #     return

    # check for city in db
    existing_city = City.query.filter_by(name=city).first()

    # if no city or query is > delta (2 hours) old
    if not existing_city or (existing_city.time > delta):
        # request data
        new_city_data = get_weather_data(city)
        # check response worked
        if new_city_data['cod'] == 200:

            # parse temp and convert to degrees
            temp = int(new_city_data['main']['temp']-237.15)
            time_checked = datetime.now()
            new_city_obj = City(name=city, time=time_checked, temperature=temp)
            db.session.add(new_city_obj)
            db.session.commit()

        # error with request - for now assume that's a user error in the request but should be more informative
        else:
            temp = f'Error with request, check city "{city}" exists'

    # city exists and was requests within last 2 hours:
    else:
        temp = existing_city.temperature

    return json.dumps({'temp':temp})

if __name__=='__main__':
    app.run()