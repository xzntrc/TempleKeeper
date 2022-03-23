#!/usr/bin/env python3

import json
import discord
from discord.ext import commands
import os
import sentry_sdk
import logging

sentry_sdk.init(
    os.environ.get('SENTRY_DSN', ''),
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)


def get_prefix(_, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
        logging.debug(f"prefix:{prefixes[str(message.guild.id)]}")
        return prefixes[str(message.guild.id)]


bot = commands.Bot(command_prefix=get_prefix, case_insensitive=True, help_command=None)


@bot.command()
async def help(ctx):
    embed = discord.Embed(title="TempleKeeper Help",
                          description="Here you can find a list of commands for the TempleKeeper bot!", color=0x99c1f1)
    embed.set_author(name="Haro", url="https://github.com/Eccentrici/TempleKeeper")
    embed.set_thumbnail(
        url="https://images-ext-2.discordapp.net/external/tGXj9gSrokoiSgb1532aPBZ5pD02LabEPqT4JGqSC3c/https/c.tenor.com/WIqvnT_7Vj8AAAAi/terry-a-davis-terry-davis.gif")
    embed.add_field(name="Godspeak", value="Allows you to speak to God! \n Usage: `>godspeak {num}` (default 32).",
                    inline=False)
    embed.add_field(name="Rand", value="Generates random numbers. \n Run `>rand` for more info.", inline=False)
    embed.add_field(name="Credit",
                    value="View the documentation for more help [here](https://eccentrici.gitbook.io/tos/). \n Add to your own server [here](https://discord.com/oauth2/authorize?client_id=932193544695873566&permissions=137439308864&scope=bot).\n Test it out in the [TempleOS Discord Server](https://discord.gg/templeos)",
                    inline=False)
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
    logging.debug("Bot is ready")
    await bot.change_presence(activity=discord.Game(name="chess with God"))


@bot.command()
async def ping(ctx):
    await ctx.send(f'Ping is {round(bot.latency * 1000)}ms')


@bot.command()
async def showme(ctx):
    logging.debug("showmetheway")
    await ctx.send('The way')


@bot.event
async def on_message(message):
    user_id = os.environ.get('USER_ID', '955583532527411264')
    mention = f'<@&{user_id}>'
    if mention in message.content:
        logging.debug("Mention")
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        p = prefixes[str(message.guild.id)]
        e = discord.Embed(title="Server Prefx", description=f"My prefix is set to `{p}`",
                          color=discord.Color.from_rgb(0, 244, 244))
        e.set_footer(text=f"If you're an admin, you can change this with {p}setprefix [prefix].")
        await message.channel.send(embed=e, delete_after=5)
    await bot.process_commands(message)


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

if __name__ == "__main__":
    logging.debug("Bot run")
    bot.run(os.environ.get('DISCORD_TOKEN', ''))
