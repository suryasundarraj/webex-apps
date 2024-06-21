import os

from webex_bot.commands.echo import EchoCommand
from webex_bot.webex_bot import WebexBot

# (Optional) Proxy configuration
# Supports https or wss proxy, wss prioritized.
#proxies = {
#    'https': 'http://proxy.esl.example.com:80',
#    'wss': 'socks5://proxy.esl.example.com:1080'
#}

# Create a Bot Object
bot = WebexBot(teams_bot_token=os.getenv("WEBEX_TEAMS_ACCESS_TOKEN"),
               approved_rooms=['2493d0f0-2eda-11ef-8361-cda22404625a'],
               bot_name="TEST_BOT",
               include_demo_commands=True)

# Add new commands for the bot to listen out for.
bot.add_command(EchoCommand())

# Call `run` for the bot to wait for incoming messages.
bot.run()

