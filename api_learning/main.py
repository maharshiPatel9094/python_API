# endpoints in API -> address of Url
# api request -> 

import requests


response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response)
# to raise a request error
response.raise_for_status()
data = response.json()
latitude = data["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]
print(data)

# response object has lot of things inside this object



# response code
# 1xx -> hold on 
# 2xx -> success
# 3xx -> go away
# 4xx -> u screwed up
# 5xx -> i screwed up