from chat import message_generation
from file_read import open_file

async def handle_message(message):
    response = message_generation(message)
    await message.channel.send(response)


async def handle_command(message):
    open_file("./support files/names.json")
    await message.channel.send("response")