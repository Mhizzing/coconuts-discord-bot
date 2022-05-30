import discord
from discord.ext import commands
from replit import db

class Schedules(commands.Cog):
  def __init__(self, bot):
  self.bot = bot

  @commands.command()
  async def create_message(self, ctx: commands.Context, message_text=None):
    db[f'{ctx.author.id}_message'] = str(message_text)
    await ctx.send(f'Your message has been saved, {ctx.author.name}.')
    
  @commands.command()
  async def show_message(self, ctx: commands.Context, user: discord.User = None):
    if user:
      user_id = user.id
    else:
      user_id = ctx.author.id

    message = db[f'{user_id}_message']

    if message:
      await ctx.send(f'Here is your message:\n>>>{message}')
    else:
      await ctx.send('It appears that user has not saved a message.')
      