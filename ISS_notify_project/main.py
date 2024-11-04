from datetime import datetime
import requests
import smtplib
import time

MY_LAT = 46.088840
MY_LONG = -64.775930
MY_EMAIL = "YOUR_VALID_EMAIL"
MY_PASSWORD = "YOUR_ACCOUNT_PASSWORD"

# fun
def is_iss_visible():
    '''Check weather the ISS is in our range'''
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    # print(data)

    iss_latitude = float(data["iss_position"]["latitude"])
    print(iss_latitude)
    iss_longitude = float(data["iss_position"]["longitude"])
    print(iss_longitude)


    # comapare position
    # +5 and -5 is ok it will still be visible
    if (MY_LAT - 5) <= iss_latitude <= (MY_LAT + 5) and (MY_LONG - 5) <= iss_longitude <= (MY_LONG + 5):
        return True
    
    
def is_night():
    '''checks weather it is night or not'''
    parameters = {
        "lat" : MY_LAT,
        "lng" : MY_LONG,
        "formatted" : 0,
    }
    
    response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
    response.raise_for_status() 
    data = response.json
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        # its dark
        return True
    
# send email
while True:
    time.sleep(60)
    if is_iss_visible() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL,MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,to_addrs=MY_EMAIL,msg="Subject:LookUp\n\nThe ISS is above you in the sky.")