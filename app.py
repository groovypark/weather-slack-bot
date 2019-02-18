import schedule
import time
from time import localtime, strftime
import requests
import forecastio
import os

os.environ["TZ"] = 'Asia/Seoul'
URL = "https://hooks.slack.com/services/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"


def forecast():
    lat = 37.489671
    lng = 127.143398

    forecast = forecastio.load_forecast(
        '2442a3a355f1793b2ce0d25f38b7586f', lat, lng)
    byHour = forecast.hourly()
    return byHour.summary


def send_message():
    print(strftime("%a, %d %b %Y %H:%M:%S", localtime()))
    r = requests.post(url=URL, headers={'Content-Type': 'application/json'},
                      json={
        "channel": "#chatbot",
        "username": "forecast_bot",
        "text": forecast(),
        "icon_emoji": ":rainbow:"
    })
    print(r.text)


schedule.every().day.at("00:00").do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)
