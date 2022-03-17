import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "P9832GBTJQQF2L6K"
NEWS_API_KEY = "cb447aa2cba2439198b7b2fcca05b1ba"
TWILIO_SID = "your_sid"
TWILIO_AUTH_TOKEN = "your_token"

# STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries.
#  e.g. [new_value for (key, value) in dictionary.items()]
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response_stock = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_data = response_stock.json()["Time Series (Daily)"]
data_list = [value for (key, value) in stock_data.items()]

yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
# yesterday_opening_price = yesterday_data["1. open"]

# Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing = day_before_yesterday_data["4. close"]

# Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.
#  Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = round(float(day_before_yesterday_closing) - float(yesterday_closing_price), 2)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

# Work out the percentage difference in price between closing price yesterday and closing price the day
#  before yesterday.
change_percent = round(difference / float(yesterday_closing_price) * 100, 2)

# If TODO4 percentage is greater than 5 then print("Get News").
if abs(change_percent) > 5:
    # Use the News API to get articles related to the COMPANY_NAME.
    news_params = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY
    }
    response_news = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = response_news.json()["articles"]

    # Use Python slice operator to create a list that contains the first 3 articles. Hint:
    # https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_articles = articles[:3]

    # STEP 3: Use twilio.com/docs/sms/quickstart/python
    # to send a separate message with each article's title and description to your phone number.

    # Create a new list of the first 3 articles headline and description using list comprehension.
    formatted_articles = [
        f"{STOCK_NAME}: {up_down}{change_percent}% \nHeadline: {article['title']}. \nBrief: {article['description']}"
        for article in three_articles]

    # Send each article as a separate message via Twilio.
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="+123456789",
            to="your_number_here"
        )

    # Optional: Format the message like this:
    """TSLA: 🔺2% Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. Brief: We at Insider Monkey 
    have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F 
    filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus 
    market crash. or "TSLA: 🔻5% Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. Brief: We at 
    Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by 
    the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of 
    the coronavirus market crash. """
