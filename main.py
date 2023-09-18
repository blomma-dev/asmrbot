# Import the required modules
import discord
import os
import random
from discord.ext import commands 
from dotenv import load_dotenv
# Create a Discord client instance and set the command prefix
intents = discord.Intents.all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!', intents=intents)
# Set the confirmation message when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
# Set the commands for your bot
@bot.command()
async def greet(ctx):
    response = 'Hello, I am your discord bot'
    await ctx.send(response)
@bot.command()
async def list_command(ctx):
    response = 'You can use the following commands: \n !greet \n !list_command \n !functions'
    await ctx.send(response)
@bot.command()
async def functions(ctx):
    response = 'I am a simple Discord chatbot! I will reply to your command!'
    await ctx.send(response)

@bot.event
async def on_message(message):
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    if message.content == '99!':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)






# Retrieve token from the .env file
load_dotenv()
bot.run(os.getenv('TOKEN'))