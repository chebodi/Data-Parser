from flask import Flask, jsonify, request
import appapi

app = Flask(__name__)
app.config['DEBUG'] = True
#import requests
#from flask_restful import Api, Resource, reqparse


# import json

@app.route('/weather/<city_name>', methods=['GET'])
def weather(city_name):
    type = request.args.get('type')
    if (type==None):
        return (jsonify(appapi.getSevenDays(city_name)))
    elif(type=='10'):
        return (jsonify(appapi.getTenDays(city_name)))
    else:
        print('error')

@app.route('/weather/cities', methods=['GET'])
def weather_cities():
    return (jsonify(appapi.getAllCities()))

@app.route('/weather/<city_name>/today', methods=['GET'])
def weather_cities(city_name):
    return (jsonify(appapi.getToday(city_name)))

if __name__ == '__main__':
    app.run(debug=True)
















'''
@app.route('/weather/<city_name>/10', methods=['GET'])
def weather_ten_days(city_name):
    return (jsonify(appapi.getTenDays(city_name)))
'''