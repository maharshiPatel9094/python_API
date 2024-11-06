# Stock News Alert with Twilio

This project retrieves stock price data for Tesla Inc (TSLA) from the Alpha Vantage API, calculates the percentage difference between the closing prices of the last two trading days, and if the difference exceeds 5%, it sends news articles about Tesla Inc to your phone using the News API and Twilio for SMS notifications.

## Features

- Fetches the daily stock data for Tesla Inc (TSLA) using the Alpha Vantage API.
- Calculates the percentage difference between yesterday's closing price and the day before yesterday's closing price.
- If the price difference exceeds 5%, retrieves the latest news articles about Tesla from the News API.
- Sends SMS notifications for the top 3 articles using Twilio.

## Requirements

1. **Python 3.7+**  
2. **Libraries**  
   - `requests` for making API calls.
   - `twilio` for sending SMS messages.
   - `python-dotenv` for managing environment variables.

You can install the necessary libraries by running:

## API KEYS and Twilio setup
To run the application, you need the following:

1. Alpha Vantage API Key: For fetching stock price data.
2. News API Key: For fetching news articles.
3. Twilio Account SID and Auth Token: For sending SMS messages.

- These keys should be added to your environment variables, which will be loaded via a .env file.

## Future Improvements
- Add error handling for API requests to manage timeouts or missing data.
- Allow the user to configure the stock symbol or the threshold for the percentage difference (e.g., change from 5% to a configurable value).
- Improve message formatting (e.g., use Markdown for rich text formatting in SMS messages).

