import os

from flask import Flask, redirect
from dotenv import load_dotenv
from discord import Intents, Client, message


# Create your Flask instance
app = Flask(__name__)

# Load Discord Token as a variable to run client (below)
load_dotenv()
disc_token = os.getenv('DISCORD_TOKEN')

# Set up Discord Intents (your instance of a Client is your connection to Discord)
intents = Intents.default()
intents.message_content = True 
client = Client(intents=intents)

# When bot starts - redirect to Eve character log-in
@client.event
async def on_ready():
    print(f'{client.user} is now running!')
    # return redirect("https://login.eveonline.com/v2/oauth/authorize/?response_type=code&redirect_uri=https%3A%2F%2Flocalhost%2Fcallback%2F&client_id=76a771a276594ca08ef1fb23fda28b23&scope=esi-calendar.read_calendar_events.v1 esi-corporations.read_structures.v1 esi-corporations.read_starbases.v1&state=RS15yx3Otz")

# When bot hears *ANY* message - we want to make sure we ignore messages from the bot itself
@client.event
async def on_message():
    if message.author == client.user:
        return
    
    
client.run(disc_token)