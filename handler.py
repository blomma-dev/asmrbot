import random

async def handle_message(message):

    brooklyn_99_quotes = [
            'I\'m the human form of the 💯 emoji.',
            'Bingpot!',
            (
                'Cool. Cool cool cool cool cool cool cool, '
                'no doubt no doubt no doubt no doubt.'
            ),
            ('qväck kväck! - swedish ducks'),
        ]

    if message.content == '99!':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)
        
    # Check if the message contains the phrase "beep boop"
    if 'beep boop' not in message.content.lower():
        # If not, respond with quote
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)
