# 873e03c42fff4c54b9884802242806 &aqi=yes

import win32com.client as wincom
import requests
import json

city=input("Enter a city you want to know: ")

url=f"http://api.weatherapi.com/v1/current.json?key=873e03c42fff4c54b9884802242806&q={city}"

r=requests.get(url)
#print(r.text)
x=json.loads(r.text)
y=x["current"]["temp_c"]
print(y)
speak = wincom.Dispatch("SAPI.SpVoice")

speak.Speak(f"the weather in {city} is {y} degree celcius")