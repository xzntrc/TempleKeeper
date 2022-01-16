import json
import sys
import discord
from discord.ext import commands
import os
f = open('config.json')
token = json.load(f)["token"]
f.close()
if token == "YOUR TOKEN GOES HERE":
    print("You have not changed your token. Please set it in config.json")
    sys.exit()

bot = commands.Bot(command_prefix = '[') # Change

@bot.event
async def on_ready():
    print("Bot Ready.")

@bot.command()
async def ping(ctx):
    await ctx.send(f'Ping is {round(bot.latency * 1000)}ms')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(token)
