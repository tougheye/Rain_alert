import requests
from twilio.rest import Client
import os


t_sid = os.environ.get("AUTH_SID")          # add your own Auth SID from twilio
t_token = os.environ.get("AUTH_TOKEN")      # add your own Auth token from twilio

print(t_token, t_sid)

"""

api_ep = "https://api.openweathermap.org/data/3.0/onecall"
parameters = {"appid" : os.environ.get("OWM_API_KEY"),
    "lat": 35.22709, "lon": -80.84313, 'exclude': "current,minutely,daily"}

response = requests.get(url=api_ep, params=parameters)
response.raise_for_status()

weather_data = response.json()
next_12_hrs = weather_data['hourly'][0:12]
next_12_codes = []

will_rain = False

for i in next_12_hrs:
    ids = i['weather'][0]['id']
    next_12_codes.append(ids)
    if ids < 700:
        will_rain = True
print(next_12_codes)

client = Client(t_sid, t_token)
if will_rain:
    message = client.messages \
            .create(
                    body="Bring an umbrella",
                    from_="+12566023852",
                    to=os.environ.get("MYCELL")
                    )
    print(message.sid)



