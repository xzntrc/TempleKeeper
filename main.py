import json
import sys
import discord
from discord.ext import commands
import os
import requests
import urllib.request
import linecache as lc
# GETTING TOKEN
## PLACE YOUR TOKEN IN CONFIG.JSON
f = open('config.json')
token = json.load(f)["token"]
f.close()
if token == "YOUR TOKEN GOES HERE":
    print("You have not changed your token. Please set it in config.json")
    sys.exit()

os.system('cls' if os.name == 'nt' else 'clear')

def get_prefix(client, message):

    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
        return prefixes[str(message.guild.id)]

bot = commands.Bot(command_prefix=get_prefix, case_insensitive=True)


@bot.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    prefixes[str(guild.id)] = '>'
    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@bot.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    prefixes.pop(str(guild.id))
    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@bot.command(aliases=['changeprefix', 'prefixset', 'prefixchange'])
@commands.has_permissions(administrator=True)
async def setprefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

    await ctx.send(f'Successfully changed the prefix to: **``{prefix}``**')


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
