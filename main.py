import requests
import os
from twilio.rest import Client

OWN_endpoint = "https://api.openweathermap.org/data/2.5/forecast"

api_key = "6aa46c448493de3f62ccb25b532ce073"
account_sid = "AC7da5be457a459024ed243c2e44cc7ed0"
auth_token = "53ec5a2229f173072cf9160b0f0b3168"

parameters = {
    "lat" : "-2.529450",
    "lon" : "-44.296951",
    "appid" : api_key,
    "cnt" : 4,
}

response = requests.get(OWN_endpoint,params=parameters)
response.raise_for_status()
weather_data = response.json()

# print(weather_data)
# for i in range (4):
#     id = weather_data["list"][i]["weather"][0]["id"]
#     if id < 700 :
        
#         print("Bring an umbrella")
        
will_rain = False      
for hour_data in weather_data["list"]:
    condition_code =hour_data["weather"][0]["id"]
    if condition_code < 700 :
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    body="its going to rain today remember to bring an umbrella ☂️",
    from_="+12315997776",
    to="+919359109047",
    )
    print(message.status)
    