# Rain_alert

The goal of this project was to learn how to use API and setting up environment variables as well as retrieving them in the code script.

I used [openwheathermap.org](https://openweathermap.org) to receive the weather data for a particular geographic location 
using their API. The data is subsequently saved in JSON format. If there is a rain in the following 12 hours of the forecast, will_rain variable turns True. The API Authorization details are saved in the environment variable that was used in the script.

As for sending the text alert in case there is a rain, I used twilio.com which let me create a personal phone number 
to send text messages. I used my personal cellphone number to test the code. The os module was used to retrieve the environment variables. 

