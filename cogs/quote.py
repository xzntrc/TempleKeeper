import discord
from discord.ext import commands
import quantumrandom
import math
import urllib.request

class quoteCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def quote(self, ctx, *args):
        output = urllib.request.urlopen(f"https://www.random.org/integers/?num=1&min=0&max=27&col=1&base=10&format=plain&rnd=new")
        numbers = []
        for word in output.read().split():
            if word.isdigit():
                numbers.append(int(word))

        f = open("qoutes.txt", "r")
        d = f.read()
        quote = d.split("\n")
        f.close() 
        speak = [] 
        for i in range(len(numbers)):
            speak.append(quote[numbers[i]])

        speaketh = ' '.join(speak)

        await ctx.send(f"{speaketh}")
  
        
def setup(bot):
    bot.add_cog(quoteCog(bot))
