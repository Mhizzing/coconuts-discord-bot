import os
import discord
from discord.ext import commands


intents = discord.Intents.all()
bot = commands.Bot(command_prefix='$', intents=intents)

author_id = os.environ['mhizzing_discord_id']
bot.author_id = author_id

extension_list = ['cogs.utility', 'cogs.communication'] 

if __name__ == '__main__':
  for extension in extension_list:
    bot.load_extension(extension)

@bot.event
async def on_ready():
  print('I\'m working! :D')
  await bot.change_presence(status=discord.Status.online, activity=discord.Game("with my master"))


bot_token = os.environ['TOKEN']
bot.run(bot_token)