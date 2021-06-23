# -*- coding: utf-8 -*-
"""shape ai project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pscg6snDDVfx4FjmQXNGJxmCcoK5Zutz
"""

x= open("shapeai1.txt ",'a')

import requests
#import os
from datetime import datetime

api_key = '2510edf7bb22bcf16e84a1165916e98c'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("-------------------------------------------------------------",file=x)
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time),file=x)
print ("-------------------------------------------------------------",file=x)

print ("Current temperature is: {:.2f} deg C".format(temp_city),file=x)
print ("Current weather desc  :",weather_desc,file=x)
print ("Current Humidity      :",hmdt, '%',file=x)
print ("Current wind speed    :",wind_spd ,'kmph',file=x)

x.close()

#Enter the city name:( example: kerala , trivandrum)