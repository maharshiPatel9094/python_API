import os
import requests
from dotenv import load_dotenv
from flight_search import FlightSearch  # Import the FlightSearch class

# Load environment variables
load_dotenv()

# Sheety API endpoint
SHEETY_ENDPOINT = "https://api.sheety.co/04635aeb0e71e1bfd4d64ec47e4fa49f/flightDeals/prices"

class DataManager:
    def __init__(self):
        self.user = os.environ["SHEETY_USERNAME"]
        self.password = os.environ["SHEETY_PASSWORD"]
        self.SheetData = {}
        
    def get_sheetData(self):
        """Fetch sheet data from Sheety API."""
        response = requests.get(url=SHEETY_ENDPOINT)
        data = response.json()
        self.SheetData = data["prices"]
        return self.SheetData
    
    def update_destination_codes(self):
        for city in self.SheetData:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)
