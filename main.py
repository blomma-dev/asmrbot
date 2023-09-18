# Import the required modules
import discord
import os
import handler
import renamer

from discord.ext import commands, tasks
from dotenv import load_dotenv
import datetime
# Create a Discord client instance and set the command prefix
intents = discord.Intents.all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!', intents=intents)
# Set the confirmation message when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    task_loop.start()


@bot.command(name="G")
async def on_command(message):
    if message.author == bot.user:
        return
    await handler.handle_command(message)

@bot.command(name="N")
async def on_command(message):
    if message.author == bot.user:
        return
    await renamer.change_channel_name(message)

@tasks.loop(minutes=15)
async def task_loop():
    renamer.check_time()
    renamer.change_channel_name()

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    await handler.handle_message(message)

    # Allow other event handlers to process the message
    await bot.process_commands(message)


# Retrieve token from the .env file
load_dotenv()
bot.run(os.getenv('TOKEN'))