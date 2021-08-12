# Class Lemur Day Course
# Mini-Capstone, The Wiggins Bot
# Scott Cormack
# Python 3.9.6

import os
import discord
from dotenv import load_dotenv

# Pull secret token in from hidden file
load_dotenv()
TOKEN = os.getenv('WIGGINS_SECRET_TOKEN')
SERVER_ID = os.getenv('SERVER_ID')

# Create a Discord client and test connection
client = discord.Client()

@client.event
async def on_ready():
    for server in client.guilds:
        if server.name == SERVER_ID:
            break
    print(f'{client.user} has connected to Discord!')
    print(f'{client.user} is connected to the following server:\n'
          f'{server.name}(ID: {server.id})'
    )
    members = '\n - '.join([member.name for member in server.members])
    print(f'Server Members:\n - {members}')

client.run(TOKEN)