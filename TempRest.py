# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 17:02:48 2016

@author: harshad
"""

from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse
import Adafruit_DHT


app = Flask(__name__)

api = Api(app)

sensor = Adafruit_DHT.DHT22
pin = 'P8_11'


class GetTemperature(Resource):
    def post(self):
        try: 
            # Parse the arguments
            #parser = reqparse.RequestParser()
           # parser.add_argument('id', type=str)
            humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
            data='Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity)


          

            
"""           
           items_list=[];
            for item in data:
                i = {
                    'Id':item[0],
                    'Item':item[1]
                }
                items_list.append(i)
"""                

            return {'StatusCode':'200','Temp':data}

        except Exception as e:
            return {'error': str(e)}


api.add_resource(GetTemperature, '/GetTemperature')

if __name__ == '__main__':
    app.run(debug=True)