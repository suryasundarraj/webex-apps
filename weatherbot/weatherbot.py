from webex_bot.webex_bot import WebexBot
import os 
import requests
from webex_bot.models.command import Command

# fill api token
# api_token = ""

bot = WebexBot(os.getenv("WEBEX_TEAMS_ACCESS_TOKEN"), approved_domains=["cisco.com"])


class WeatherByZIP(Command):
    def __init__(self):
        super().__init__(
            command_keyword="weather",
            help_message="Get current weather conditions by ZIP code.",
            card=None,
        )

    def execute(self, message, attachment_actions, activity):
        #return f"Got the message: {message}"
	# Message may include spaces. Strip whitespace:
    	zip_code = message.strip()
    	print(zip_code)
    	# Define our URL, with requested ZIP code & API Key
    	url = "http://api.openweathermap.org/data/2.5/weather?"
    	url += f"q={zip_code}&units=standard&appid=52c38e07c248b1f0e21946722944b5dc"
    	print(url)
    	# Query weather
    	response = requests.get(url)
    	print(response)
    	weather = response.json()

    	# Pull out desired info
    	city = weather['name']
    	conditions = weather['weather'][0]['description']
    	temperature = weather['main']['temp']
    	humidity = weather['main']['humidity']
    	wind = weather['wind']['speed']

    	response_message = f"In {city}, it's currently {temperature}F with {conditions}. "
    	response_message += f"Wind speed is {wind}mph. Humidity is {humidity}%"
    	print(zip_code)
    	return response_message

bot.add_command(WeatherByZIP())
bot.run()

