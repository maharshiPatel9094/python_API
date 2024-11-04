# endpoints in API -> address of Url
# api request -> 

import requests
from datetime import datetime

# ----------API PARAMETERS 
# sunrise and sunset 

# if the api has parameters inside it they will describe it like what it should take 
# parameters can be required or optional
# optional parameters have some default value 
# key nme must be same as the api doc say 

MY_LAT = 51.507351
MY_LONG = -0.127758

parameters = {
    "lat" : MY_LAT,
    "lng" : MY_LONG,
    "formated" : 0,
}


response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status() 
data = response.json
print(data)
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

time_now = datetime.now()
print(time_now.hour)





# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# # print(response)
# # to raise a request error
# response.raise_for_status()
# data = response.json()
# latitude = data["iss_position"]["latitude"]
# longitude = data["iss_position"]["longitude"]
# print(data)

# response object has lot of things inside this object




# response code
# 1xx -> hold on 
# 2xx -> success
# 3xx -> go away
# 4xx -> u screwed up
# 5xx -> i screwed up