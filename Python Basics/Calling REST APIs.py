"""
Python -: Request Module -: pip install requests
import requests

Example -: Open Weather APIs

Step1: Subscribe them, and get the API_KEY
Step2: import requests module
Step3: API Call -: http://api.openweathermap.org/data/2.5/forecast?id=<cityId>&APPID={API_KEY}





"""
import requests

# print(dir(requests))
API_KEY = "ABCDERF!@#$"
CITY_ID = "ANNSHDJ"

API_CALL = f"http://api.openweathermap.org/data/2.5/forecast?id={CITY_ID}&APPID={API_KEY}"

req = requests.get(API_CALL)
print(req.status_code)
print(req.json())

data = req.json()


