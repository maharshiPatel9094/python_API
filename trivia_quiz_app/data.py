import requests

# parameters for the api
parameters = {
    "amount" : 10,
    "type" : "boolean",
}

# api call
response = requests.get(url="https://opentdb.com/api.php?",params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]