import os
import requests 
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv


# load environment variables 
load_dotenv()

# sheety endpoint 
SHEETY_ENDPOINT = "https://api.sheety.co/04635aeb0e71e1bfd4d64ec47e4fa49f/flightDeals/prices"

class DataManager:
    def __init__(self):
        self.user = os.environ["SHEETY_USERNAME"]
        self.password = os.environ["SHEETY_PASSWORD"]
        # self.authorization = HTTPBasicAuth(self.user,self.password)
        self.SheetData = {}
        
    def get_sheetData(self):
        '''This function call the sheety API and gets the sheet data.'''
        response = requests.get(url=SHEETY_ENDPOINT)
        data = response.json()
        # getting our data in a list of prices
        self.SheetData = data["prices"]
        return self.SheetData
    
    def update_destination_code(self):
        '''This Function basically updates the IATA code for every city.'''
        for city in self.SheetData:
            new_data = {
                "price": {
                    "iataCode" : city["iataCode"]
                }
            }
            requests.put( 
                url=f"{SHEETY_ENDPOINT}/{city['id']}",
                json=new_data
            )