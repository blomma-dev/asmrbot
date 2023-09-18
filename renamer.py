import discord
import datetime
import file_read

# Specify the target voice channel ID and the new name
TARGET_CHANNEL_ID = 1153272591495200821  # Replace with your channel ID


def check_time():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current time: {now}")

async def change_channel_name(ctx):

    #if now.hour == 0 and now.minute == 0:  # Change the name at midnight
        try:
            new_name = file_read.open_file("./support files/names.json")
            channel = ctx.guild.get_channel(TARGET_CHANNEL_ID)  # Get the current channel
            await channel.edit(name=new_name)
            print(f"Channel name changed to '{new_name}'")
        except discord.Forbidden:
            print("I don't have the necessary permissions to change the channel name.")
        except Exception as e:
            print(f"An error occurred: {e}")

