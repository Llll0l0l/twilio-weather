import requests, os
from twilio.rest import Client

MY_API_KEY = os.environ.get("OWM_API_KEY")
MY_LAT = os.environ.get("MY_LAT")
MY_LONG = os.environ.get("MY_LONG")

ACCOUNT_SID = os.environ.get("ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")

MY_NUM = os.environ.get("MY_NUM")

parameters = {
    'lat': MY_LAT,
    'lon': MY_LONG,
    'appid': MY_API_KEY,
}


response = requests.get(
    url="https://api.openweathermap.org/data/2.5/weather", params=parameters)
main = response.json()['weather'][0]['main']
desc = response.json()['weather'][0]['description']

msg = f'{main}\n{desc}'
client = Client(ACCOUNT_SID, AUTH_TOKEN)
sms = client.messages\
    .create(
        body=f'\n{msg}',
        from_='+19706457792',
        to=MY_NUM
    )

print(sms.status)