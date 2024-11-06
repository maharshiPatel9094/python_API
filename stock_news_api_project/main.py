import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client


# load env var
load_dotenv()

api_key = os.getenv("API_KEY")
news_api_key = os.getenv("NEWS_API_KEY")
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")

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
diffrence = float(yesterday_close_price) - float(day_before_yesterday_closing_price)
# print(diffrence)
up_down = None
if diffrence > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

#Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
# if we use day before closing price it will give us the percentage diffrence.
diffrence_percentage = round((diffrence/float(yesterday_close_price)) *  100)
print(diffrence_percentage)

#If percentage is greater than 5 then print("Get News").
#Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
if abs(diffrence_percentage) > 5:
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
    # print(first_three_articles)


#to send a separate message with each article's title and description to your phone number. 

#Create a new list of the first 3 article's headline and description using list comprehension.
article_list = [f"{STOCK_NAME}: {up_down}{diffrence_percentage}% Headline: {article['title']}. \nBrief: {article['description']}" for article in first_three_articles]
print(article_list)

#Send each article as a separate message via Twilio. 
client = Client(account_sid, auth_token)


for article in article_list:
    message = client.messages.create(
        body= article,
        from_='+12183166216',
        to='+14375571728'
        )

