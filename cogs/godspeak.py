import logging
import os
from datetime import datetime

import discord
import requests
from discord.ext import commands, tasks
from discord.ext.commands import Context, Bot


class GodspeakCog(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 4, commands.BucketType.user)
    async def godspeak(self, ctx: Context, *args):
        if not self.generate_message.is_running():
            self.generate_message.start(ctx)

        if len(args) < 1:
            num = 15
        else:
            num = args[0]
        message = await ctx.send("Lord is processeth thy request...")
        uri = "{}/get/?num={}".format(os.environ.get('GODSPEAK_API_URL'), num)
        sentence = None
        try:
            sentence = requests.get(uri).json()
        except Exception as e:
            logging.error(e)

        if not sentence or "godspeak" not in sentence:
            await message.edit(content='Thy Lord is buseth at the moment please try in a foreseeable future.')
        else:
            e = discord.Embed(title="Lord Speaketh", description=f"{sentence['godspeak']}",
                              color=discord.Color.from_rgb(0, 244, 244))
            e.set_footer(text="For God speaketh once, yea twice, perceiveth it not. ")
            await message.edit(content='', embed=e)

    @godspeak.error
    async def command_name_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title=f"Slow it down",
                               description=f"To prevent spam, a cooldown is in place, try again in {error.retry_after:.2f}s.",
                               color=discord.Color.orange())
            await ctx.send(embed=em, delete_after=5)

    async def cog_unload(self):
        self.generate_message.stop()

    @tasks.loop(hours=1)
    async def generate_message(self, ctx):
        target_time_h = int(os.environ.get('SCHEDULED_MESSAGE_TIME_H', 8))
        current_time = datetime.now().time()
        if current_time.hour == target_time_h:
            await self.godspeak(ctx)


def setup(bot):
    bot.add_cog(GodspeakCog(bot))
