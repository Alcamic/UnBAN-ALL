import discord
from discord.ext import commands
intents=discord.Intents.all()
bot = commands.Bot(command_prefix = "ctkp!", intents=intents)
Token = ''

@bot.event
async def on_ready():
    print("準備完了")
    target = bot.get_guild(867341022937612288)
    async for entry in target.bans(limit=20000):
        print(entry.user)
        await target.unban(entry.user)


bot.run(Token)
