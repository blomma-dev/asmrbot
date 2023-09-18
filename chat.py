import random
def message_generation(message):
    brooklyn_99_quotes = [
            'I\'m the human form of the 💯 emoji.',
            'Bingpot!',
            (
                'Cool. Cool cool cool cool cool cool cool, '
                'no doubt no doubt no doubt no doubt.'
            ),
            'qväck kväck! - swedish ducks',
        ]
 
    # Check if the message contains the phrase "beep boop"
    if 'beep boop' not in message.content.lower():
        # If not, respond with quote
        response = random.choice(brooklyn_99_quotes)
        return response
    else:
        response = "beep boop"
        return response
