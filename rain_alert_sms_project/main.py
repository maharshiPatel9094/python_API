import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os


# load env variables 
load_dotenv()

account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")
api_key = os.getenv("API_KEY")


api_endpoint = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "lat": 46.087818,
    "lon": -64.778229,
    "appid": api_key,
    "cnt" : 4,
}
will_rain = False

response = requests.get(url=api_endpoint,params=parameters)
response.raise_for_status()
data = response.json()
# print(data["list"][0]["weather"][0]["id"])
for hour_data in data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
        
if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    body="It's going to rain today. Remember to bring an ☂️",
    from_='+12183166216',
    to='+14375571728'
    )

print(message.status)