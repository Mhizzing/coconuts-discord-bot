import os
import discord
from modules import *
from discord.ext import commands


intents = discord.Intents.all()
bot = commands.Bot(command_prefix='$', intents=intents)

bot.author_id = mhizzing_discord_id

bot.add_cog(Utilities(bot))
bot.add_cog(Schedules(bot))

@bot.event
async def on_ready():
  print('I\'m working! :D')


bot_token = os.environ['TOKEN']
bot.run(bot_token)