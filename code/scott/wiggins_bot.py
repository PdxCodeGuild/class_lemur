# Class Lemur Day Course
# Mini-Capstone, The Wiggins Bot
# Scott Cormack
# Python 3.9.6

# Application ID: 875419839806713888
# Token: ODc1NDE5ODM5ODA2NzEzODg4.YRVQQg.WuUrKY9p7TdYXYIYeTWfa20n7rM

import os
import discord
from dotenv import load_dotenv

# Pull secret token in from hidden file
load_dotenv()
token = os.getenv('wiggins_secret_token')
server_id = os.getenv('server')

# Create a Discord client and test connection
client = discord.Client()

@client.event
async def on_ready():
    for server in client.guilds:
        if server.name == server_id:
            break
    print(f'{client.user} has connected to Discord!')
    print(f'{client.user} is connected to the following server:\n'
          f'{server.name}(ID: {server.id})'
    )
    members = '\n - '.join([member.name for member in server.members])
    print(f'Server Members:\n - {members}')

client.run(token)