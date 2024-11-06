import requests
import os
from dotenv import load_dotenv


# load env var
load_dotenv()

api_key = os.getenv("API_KEY")
news_api_key = os.getenv("NEWS_API_KEY")

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

parameters = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK_NAME,
    "apikey" : api_key,
}

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"



#Get yesterday's closing stock price. 
response = requests.get(STOCK_ENDPOINT,params=parameters)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
# converted dict into list as it is easy to access
data_list = [value for (key,value) in data.items()]
# print(data_list[0])
yesterday_data = data_list[0]
yesterday_close_price = yesterday_data["4. close"]
print(yesterday_close_price)

#Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

#Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
diffrence = abs(float(yesterday_close_price) - float(day_before_yesterday_closing_price))
print(diffrence)

#Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
# if we use day before closing price it will give us the percentage diffrence.
diffrence_percentage = (diffrence/float(yesterday_close_price)) *  100
print(diffrence_percentage)

#If percentage is greater than 5 then print("Get News").
#Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
if diffrence_percentage > 1:
    news_params = {
        "apiKey" : news_api_key,
        "qInTitle" : COMPANY_NAME,
        
    }
    response = requests.get(NEWS_ENDPOINT,params=news_params)
    response.raise_for_status()
    data = response.json()["articles"]
    # print(data)
#Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    first_three_articles = data[:3]
    print(first_three_articles)



    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

