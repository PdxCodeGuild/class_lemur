# Class Lemur Day Course
# Mini-Capstone, The Wiggins Bot
# Scott Cormack
# Python 3.9.6

import os
import discord
import logging
from discord.ext import commands
from keep_alive import keep_alive

# Error logging
logger = logging.getLogger('Discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename = 'err.log', encoding = 'utf-8', mode = 'a')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

TOKEN = os.environ['WIGGINS_SECRET_TOKEN']

# Create a Discord bot and establish commonly used variables.
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix = '!', intents = intents, case_insensitive = True)

# Prompts terminal when bot is logged in and ready
@bot.event
async def on_ready():
    print(f'The Wiggins Bot has connected to the Discord backend.')


# Function to handle when new members join a Discord    
@bot.event
async def on_member_join(member):
    if member.bot:
        return
    for channel in member.guild.channels:
        if str(channel) == 'general':
            embed = discord.Embed(title = f'I see you, {member.name}.', description = 'You will now be known as Wiggins.\nWelcome Wiggins.')
            embed.set_thumbnail(url = member.avatar_url)
            await channel.send(embed = embed)
    await member.edit(nick = 'Wiggins')

# Function to handle bot responses to particular messages in chat
@bot.event
async def on_message(message):
    blurb = 'Trigger message successful!'
    await bot.process_commands(message)
    if message.content == 'test':
        await message.channel.send(blurb)
    
# Bot Commands
@bot.command(name = 'test')
async def test(ctx):
    blurb = 'Test'
    await ctx.send(blurb)

@bot.command(name = 'annoy')
async def annoy(ctx):
  ...

keep_alive()
bot.run(TOKEN)