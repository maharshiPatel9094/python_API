import requests
import os
from dotenv import load_dotenv

# load env variables
load_dotenv()

# accessenv variables 
token = os.getenv("TOKEN")
username = os.getenv("USERNAME")


# required parameters of the API 
user_params = {
    "token": token,
    "username": username,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes", 
}

graph_prams = {
    "id" : "graph1",
    "name" : "Cycling graph",
    "unit" : "Km",
    "type" : "float",
    "color" : "ajisai",
}

# advance authentication using HTTP Headers 
headers = {
    "X-USER-TOKEN": token,
}


pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{username}/graphs"

# created a user
response = requests.post(pixela_endpoint,json=user_params)
print(response.text)

# create a graph defination 
# response = requests.post(graph_endpoint,json=graph_prams,headers=headers)
# print(response.text)