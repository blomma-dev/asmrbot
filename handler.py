import random
from chat import message_generation

async def handle_message(message):
    response = message_generation(message)
    await message.channel.send(response)
