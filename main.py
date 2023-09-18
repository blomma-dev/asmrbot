# Import the required modules
import discord
import os

from discord.ext import commands
from handler import handle_message
from dotenv import load_dotenv

# Create a Discord client instance and set the command prefix
intents = discord.Intents.all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!', intents=intents)
# Set the confirmation message when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return


    await handle_message(message)

    
    # Allow other event handlers to process the message
    await bot.process_commands(message)


# Retrieve token from the .env file
load_dotenv()
bot.run(os.getenv('TOKEN'))