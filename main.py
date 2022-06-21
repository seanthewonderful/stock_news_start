import requests
import pandas as pd

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
STOCK_API_KEY = '3NZV2MQX9PDA0X36'
STOCK_URL = 'https://www.alphavantage.co/query?'
query = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': 'TSLA',
    'apikey': '3NZV2MQX9PDA0X36'
}

r = requests.get(STOCK_URL, params=query)
r.raise_for_status()
data = r.json()["Time Series (Daily)"]

data_list = [value for (key, value) in data.items()]
yesterday_close = float(data_list[0]['4. close'])
yesterday_2x_close = float(data_list[1]['4. close'])

difference = abs(yesterday_close - yesterday_2x_close)
percent_diff = (difference / yesterday_close) * 100


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 2
NEWS_API_KEY = 'b6c2023fd9cf4013a0684fa0627e3c38'
NEWS_URL = 'https://newsapi.org/v2/top-headlines?'
news_query = {
    'q': 'Tesla',
    'sortBy': 'publishedAt',
    'apiKey': NEWS_API_KEY
}
news_r = requests.get(NEWS_URL, params=news_query)
news_data = news_r.json()['articles']
news_data_top3 = [
                [news_data[0]['title'], news_data[0]['description']], 
                [news_data[0]['title'], news_data[0]['description']], 
                [news_data[0]['title'], news_data[0]['description']]
                  ]

# if percent_diff >= 5:
#     print(news_data[0]['title'])
#     print(news_data[1]['title'])
#     print(news_data[2]['title'])


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
'''Twilio no longer free service - continuing final step with print statement'''

up_down = None
if (yesterday_close - yesterday_2x_close) > 0:
    up_down = '🔼'
else:
    up_down = '🔻'

if percent_diff >= 5:
    for ea in news_data_top3:
        print(f"""
              {STOCK}: {up_down}%
              Headline: {ea[0]}
              Brief: {ea[1]}
              """)
        
        
#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

