import discord
import datetime
import file_read
import random
import asyncio

# Specify the target voice channel ID
TARGET_CHANNEL_ID = 1153272591495200821

names = {
        (4, 4): (datetime.time(16, 0), random.choice(file_read.open_file("./support files/names.json")[3])),
        (9, 17): (None, random.choice(file_read.open_file("./support files/names.json")[0])),
        (17, 24): (datetime.time(0, 0), random.choice(file_read.open_file("./support files/names.json")[1])),
        (0, 9): (None, random.choice(file_read.open_file("./support files/names.json")[2]))
    }

def get_current_hour():
    return datetime.datetime.now().hour

def is_hour_in_range(hour, start, end):
    return start <= hour < end

async def change_channel_name(bot):
    current_hour = get_current_hour()
    
    
    try:
        new_name = None
        for hours, (end_time, name) in names.items():
            if is_hour_in_range(current_hour, *hours) and (end_time is None or datetime.datetime.now().time() >= end_time):
                new_name = name
                break

        if new_name:
            channel = bot.get_channel(TARGET_CHANNEL_ID)
            await channel.edit(name=new_name)
            print(f"Channel name changed to '{new_name}'")
            print(f"Current time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    except discord.Forbidden:
        print("I don't have the necessary permissions to change the channel name.")
    except Exception as e:
        print(f"An error occurred: {e}")

async def check_and_change_channel_name(bot):
    while True:
        current_hour = get_current_hour()
        should_change_name = True

        # Check if the current hour is within the defined times in the names dictionary
        for hours, (end_time, _) in names.items():
            if is_hour_in_range(current_hour, *hours) and (end_time is None or datetime.datetime.now().time() >= end_time):
                should_change_name = False
                break

        if should_change_name:
            await change_channel_name(bot)

        await asyncio.sleep(60)  # Check every minute


