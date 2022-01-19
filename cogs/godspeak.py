import discord
from discord.ext import commands
import math
import urllib.request
class godspeakCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def godspeak(self, ctx, num):
        output = urllib.request.urlopen(f"https://www.random.org/integers/?num={int(num)}&min=1&max=7569&col=1&base=10&format=plain&rnd=new")
        numbers = []
        for word in output.read().split():
            if word.isdigit():
                numbers.append(int(word))

        f = open("vocab.txt", "r")
        d = f.read()
        vocabList = d.split("\n")
        f.close() 
        godswords = [] 
        for i in range(len(numbers)):
            godswords.append(vocabList[numbers[i]])
        
        speaketh = ' '.join(godswords)
        e = discord.Embed(title="Lord Speaketh", description=f"{speaketh}", color=discord.Color.from_rgb(0,244,244))
        e.set_footer(text="Christ will be a priest upon His throne forever.")
        await ctx.send(embed=e)
                    
def setup(bot):
    bot.add_cog(godspeakCog(bot))
