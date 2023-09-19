
# Prompt the user for the token
token = input("Enter your Discord bot token: ")

# Create or open the .env file in write mode and write the token to it
with open('.env', 'w') as env_file:
    env_file.write(f'TOKEN="{token}"')

print(".env file has been created with your token.")
