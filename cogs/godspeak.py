import os

import discord
import requests
from discord.ext import commands


class godspeakCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 4, commands.BucketType.user)
    async def godspeak(self, ctx, *args):
        if len(args) < 1:
            num = 32
        else:
            num = args[0]

        uri = "{}/get/?num={}".format(os.environ.get('GODSPEAK_API_URL'), num)
        sentence = requests.get(uri).json()
        e = discord.Embed(title="Lord Speaketh", description=f"{sentence['godspeak']}",
                          color=discord.Color.from_rgb(0, 244, 244))
        e.set_footer(text="For God speaketh once, yea twice, perceiveth it not. ")
        await ctx.send(embed=e)

    @godspeak.error
    async def command_name_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title=f"Slow it down",
                               description=f"To prevent spam, a cooldown is in place, try again in {error.retry_after:.2f}s.",
                               color=discord.Color.orange())
            await ctx.send(embed=em, delete_after=5)


def setup(bot):
    bot.add_cog(godspeakCog(bot))
