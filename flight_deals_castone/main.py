from data_manager import DataManager


# object
data_manager = DataManager()
sheet_data = data_manager.get_sheetData()
# print(sheet_data)

# check if iatacode contains any c=value or not 
#  If not, then the IATA Codes column is empty in the Google Sheet.
#  In this case, pass each city name in sheet_data one-by-one
#  to the FlightSearch class to get the corresponding IATA code
#  for that city using the Flight Search API.
#  You should use the code you get back to update the sheet_data dictionary.
if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(f"sheet_data:\n {sheet_data}")
    
    data_manager.SheetData = sheet_data
    data_manager.update_destination_code()