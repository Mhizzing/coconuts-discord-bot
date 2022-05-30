import discord
from discord.ext import commands
from replit import db

class CommsCog(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(aliases = ['message', 'create_msg'], help = 'Saves a message under your username.')
  async def create_message(self, ctx: commands.Context, *, arg):
    print(arg)
    db[f'message_{ctx.author.id}'] = str(arg)
    await ctx.send(f'Your message has been saved, {ctx.author.name}.')
    
  @commands.command(aliases = ['show_msg'], help = 'Input another user\'s username or @ to see their message.')
  async def show_message(self, ctx: commands.Context, user: discord.User = None):
    if user == None:
      user = ctx.author

    if f'message_{user.id}' in db:
      message = db[f'message_{user.id}']

      embed = discord.Embed(
        title="Message of " + user.name,
      description=message,
      color=discord.Color.blue())
        
      await ctx.send(embed=embed)

    else:
      await ctx.send('It appears that user has no saved message.')

  @commands.command()
  async def show_all_messages(self, ctx: commands.Context):
    msg_keys = db.prefix('message_')
    
    all_msgs = ''
    
    for key in msg_keys:
      msg_formatted = f'{db[key]}\n'
      all_msgs.append(msg_formatted)

    embed = discord.Embed(
      title="All Messages",
      description=all_msgs.rstrip('\n')
    )

    await ctx.send(embed=embed)
        
      

def setup(bot):
  bot.add_cog(CommsCog(bot))