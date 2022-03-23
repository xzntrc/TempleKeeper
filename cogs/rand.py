import discord
from discord.ext import commands
import quantumrandom
import math


class RandCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rand(self, ctx, *args):

        if not args:
            embed = discord.Embed(title="Missing Datatype",
                                  description="This command requires an additional datatype argument. Note that each datatype has it's own sub-arguments. \n Datatypes: \n • **Float** \n",
                                  color=discord.Color.orange())
            await ctx.send(embed=embed)
        elif args[0] == "float":
            if len(args) < 3:
                embed = discord.Embed(title="Undefined Fields",
                                      description="This command requires 3 arguments; ensure you are using the correct format:\n `>rand float {min} {max} [--round] [dp]` \n \n For more info, check this command's [documentation](https://eccentrici.gitbook.io/templekeeper/usage/random-numbers).",
                                      color=discord.Color.orange())
                embed.set_footer(text='In loving memory of Terry A. Davis.')
                await ctx.send(embed=embed)

            elif len(args) >= 3:

                if len(args) >= 4:
                    if len(args) == 4:
                        embed = discord.Embed(title="Data Invalid",
                                              description="You have not specified a decimal place (dp) to round to:.",
                                              color=discord.Color.orange())
                        embed.set_footer(text='In loving memory of Terry A. Davis.')
                        await ctx.send(embed=embed)
                    else:
                        rand = round(randint(args[1], args[2]), int(args[4]))
                        embed = discord.Embed(title=f"{rand}", color=discord.Color.from_rgb(0, 244, 244))
                        await ctx.send(embed=embed)
                else:
                    rand = randint(args[1], args[2])
                    embed = discord.Embed(title=f"{rand}", color=discord.Color.from_rgb(0, 244, 244))

        elif args[0] == "int":
            if len(args) < 3:

                embed = discord.Embed(title="Undefined Fields",
                                      description="This command requires 3 arguments Ensure you are using the correct format:\n `>rand int {min} {max}` \n \n For more info, check this command's [documentation](https://eccentrici.gitbook.io/templekeeper/usage/random-numbers).",
                                      color=discord.Color.orange())
                embed.set_footer(text='In loving memory of Terry A. Davis.')
                await ctx.send(embed=embed)
            else:
                rand = str(math.floor(randint(args[1], args[2])))
                embed = discord.Embed(title=f"{rand[:2]}", color=discord.Color.from_rgb(0, 244, 244))
                await ctx.send(embed=embed)


def randint(min, max):
    return quantumrandom.randint(int(min), int(max))


def setup(bot):
    bot.add_cog(RandCog(bot))
