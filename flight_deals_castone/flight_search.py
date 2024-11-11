import os
from dotenv import load_dotenv
import requests

# load env variables 
load_dotenv()

# endpoints
IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"


class FlightSearch:
    def __init__(self):
        self.api_key = os.environ["AMADEUS_API_KEY"]
        self.api_secret = os.environ["AMADEUS_API_SECRET"]
        self.token = self.get_new_token()
        
    def get_new_token(self):
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }  
        body = {
            'grant_type': 'client_credentials',
            'client_id': self.api_key,
            'client_secret': self.api_secret
        }
        
        response = requests.post(url = TOKEN_ENDPOINT,headers=header,data=body)
        # print(f"Your token is {response.json()['access_token']}")
        # print(f"Your token expires in {response.json()['expires_in']} seconds")
        return response.json()['access_token']
        
        
    def get_destination_code(self,city_name):
        # print(f"Using this token to getb the destination {self.token}")
        headers = {"Authorization": f"Bearer {self.token}"}
        parameter = {
            "keyword": city_name,
            "max": "2",
            "include": "AIRPORTS",
        }
        response = requests.get(
            url=IATA_ENDPOINT,
            headers=headers,
            params=parameter
        )
        
        # print(f"Status code {response.status_code}. Airport IATA: {response.text}")
        try:
            city_data = response.json()["data"]
            if city_data:
                # Return the first valid IATA code, or the first airport code if available
                for city in city_data:
                    if 'iataCode' in city and city['iataCode']:
                        return city['iataCode']
                return city_data[0].get('iataCode', 'N/A')  # Fallback if no code is found
            else:
                print(f"No city data found for {city_name}.")
                return 'N/A'
        except (IndexError, KeyError):
            print(f"Error: No IATA code found for {city_name}.")
            return 'Not Found'


    
# run the flight search class
#  test the class
# if __name__ == "__main__":
#     flight_search = FlightSearch()