import discord
import sys
from discord.ext import commands
intents=discord.Intents.all()
bot = commands.Bot(command_prefix = "ctkp!", intents=intents)
Token = sys.argv[0]

@bot.event
async def on_ready():
    print("準備完了")
    target = bot.get_guild(sys.argv[1])
    async for entry in target.bans(limit=sys.argv[2]):
        print(entry.user)
        await target.unban(entry.user)


bot.run(Token)
