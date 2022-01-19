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

bot = commands.Bot(command_prefix=get_prefix, case_insensitive=True, help_command=None)

@bot.command()
async def help(ctx):
    embed=discord.Embed(title="TempleKeeper Help", description="Here you can find a list of commands for the TempleKeeper bot!", color=0x99c1f1)
    embed.set_author(name="Eccentrici386", url="https://github.com/Eccentrici/TempleKeeper")
    embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/tGXj9gSrokoiSgb1532aPBZ5pD02LabEPqT4JGqSC3c/https/c.tenor.com/WIqvnT_7Vj8AAAAi/terry-a-davis-terry-davis.gif")
    embed.add_field(name="Godspeak", value="Allows you to speak to God! \n Usage: `$godspeak {num}` (default 32).", inline=False)
    embed.add_field(name="Rand", value="Generates random numbers. \n Run `$rand` for more info.", inline=False)
    embed.add_field(name="Credit", value="View the documentation for more help [here](https://eccentrici.gitbook.io/tos/). \n Add to your own server [here](https://discord.com/oauth2/authorize?client_id=932193544695873566&permissions=137439308864&scope=bot).\n Test it out in the [TempleOS Discord Server](https://discord.gg/templeos)", inline=False)
    embed.set_footer(text="Even he shall build the temple of the Lord; and he shall bear the glory...")
    await ctx.send(embed=embed)

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
    await bot.change_presence(activity=discord.Game(name="chess with God"))
@bot.command()
async def ping(ctx):
    await ctx.send(f'Ping is {round(bot.latency * 1000)}ms')

@bot.command()
async def bob(ctx):
    await ctx.send(f"BOT WILL BE OFFLINE FOR THE NEXT ~12 HOURS. CURRENTLY SWTICHING TO A DEDICATED VPS.")
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(token)
