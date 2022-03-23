import logging
import random

import discord
from discord.ext import commands, tasks
from discord.ext.commands import Bot


class PresenceChangerCog(commands.Cog):
    def __init__(self, client: Bot):
        self.client = client
        if not self.random_presence.is_running():
            self.random_presence.start()
        self.random_presence.add_exception_type(AttributeError)

    def cog_unload(self):
        self.random_presence.cancel()

    @tasks.loop(minutes=15)
    async def random_presence(self):
        activities = [
            discord.Activity(type=discord.ActivityType.listening, name='Burzum - Dunkelheit'),
            discord.Activity(type=discord.ActivityType.listening, name='O-Zone - Dragostea Din Tei [Official Video]'),
            discord.Activity(type=discord.ActivityType.listening, name='Олег Кензов #Пацанская ✵'),
            discord.Activity(type=discord.ActivityType.listening, name='Джордж Груз - Бандит'),
            discord.Activity(type=discord.ActivityType.listening,
                             name='Бутырка - Золотые Хиты /Сборник видеоклипов/ 2014'),
            discord.Activity(type=discord.ActivityType.listening,
                             name='Partiboi69 b2b KETTAMA - House, Electro and Techno Set Live from the Stingzone'),
            discord.Activity(type=discord.ActivityType.listening,
                             name='TOMMY CASH - EUROZ DOLLAZ YENIZ (OFFICIAL VIDEO)'),
            discord.Activity(type=discord.ActivityType.listening,
                             name='MGŁA@Mgła-Exercises in Futility V -Darkside-Brutal Assault 2019 (Drum Cam)'),
            discord.Activity(type=discord.ActivityType.watching, name='A Serbian Film'),
            discord.Activity(type=discord.ActivityType.watching,
                             name='Borat! Cultural Learnings of America for Make Benefit Glorious Nation of Kazakhstan'),
            discord.Activity(type=discord.ActivityType.watching, name='Borat Subsequent Moviefilm'),
            discord.Activity(type=discord.ActivityType.watching, name='Сталкер'),
            discord.Activity(type=discord.ActivityType.watching, name='Ojing-eo geim E1'),
            discord.Activity(type=discord.ActivityType.watching, name='Ojing-eo geim E2'),
            discord.Activity(type=discord.ActivityType.watching, name='Ojing-eo geim E3'),
            discord.Activity(type=discord.ActivityType.watching, name='Ojing-eo geim E4'),
            discord.Activity(type=discord.ActivityType.watching, name='Ojing-eo geim E5'),
            discord.Activity(type=discord.ActivityType.watching, name='Ojing-eo geim E6'),
            discord.Activity(type=discord.ActivityType.watching, name='Ojing-eo geim E7'),
            discord.Activity(type=discord.ActivityType.watching, name='Ojing-eo geim E8'),
            discord.Activity(type=discord.ActivityType.watching, name='Ojing-eo geim E9'),
            discord.Activity(type=discord.ActivityType.watching, name='Ojing-eo geim E10'),
            discord.Activity(type=discord.ActivityType.watching, name='Dragon Ball E1'),
            discord.Activity(type=discord.ActivityType.watching, name='Dragon Ball E2'),
            discord.Activity(type=discord.ActivityType.watching, name='Dragon Ball E3'),
            discord.Activity(type=discord.ActivityType.watching, name='Dragon Ball E4'),
            discord.Activity(type=discord.ActivityType.watching, name='Dragon Ball E5'),
            discord.Activity(type=discord.ActivityType.watching, name='Dragon Ball E6'),
            discord.Activity(type=discord.ActivityType.streaming, name='Vlads life'),
            discord.Activity(type=discord.ActivityType.playing, name='Counter Strike: Global Offensive'),
            discord.Activity(type=discord.ActivityType.playing, name='Counter Strike: Global Offensive'),
            discord.Activity(type=discord.ActivityType.playing, name='Counter Strike: Global Offensive'),
            discord.Activity(type=discord.ActivityType.playing, name='Counter Strike: Global Offensive'),
            discord.Activity(type=discord.ActivityType.playing, name='Counter Strike: Global Offensive'),
            discord.Activity(type=discord.ActivityType.playing, name='Counter Strike: Global Offensive'),
            discord.Activity(type=discord.ActivityType.playing, name='Counter Strike: Global Offensive'),
            discord.Activity(type=discord.ActivityType.playing, name='Counter Strike: Global Offensive'),
            discord.Activity(type=discord.ActivityType.playing, name='Counter Strike: Global Offensive'),
        ]
        await self.client.change_presence(activity=random.choice(activities))
