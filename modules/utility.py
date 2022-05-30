import discord
from discord.ext import commands

class Utilities(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self._last_member = None

  @commands.Cog.listener()
  async def  on_member_join(self, member):
    channel = member.guild.system_channel
    if channel is not None:
      await channel.send('Welcome {0.mention}'.format(member))
      
  @commands.command()
  async def ping(self, ctx: commands.Context):
    await ctx.send("Pong")
    
  @commands.command()
  async def hello(self, ctx: commands.Context, *, member: discord.Member = None, help="Says hello"):
    member = member or ctx.author
    if self._last_member is None or self._last_member.id != member.id:
      await ctx.send(f'Hello {member} :)')
    else:
      await ctx.send(f'Hello again {member}... :/')
    self._last_member = member

  @commands.command(help = "Get server details")
  async def whereami(self, ctx: commands.Context):
      owner=str(ctx.guild.owner)
      region = str(ctx.guild.region)
      guild_id = str(ctx.guild.id)
      memberCount = str(ctx.guild.member_count)
      icon = str(ctx.guild.icon_url)
      desc=ctx.guild.description
      
      embed = discord.Embed(
          title=ctx.guild.name + " Server Information",
          description=desc,
          color=discord.Color.blue()
      )
      embed.set_thumbnail(url=icon)
      embed.add_field(name="Owner", value=owner, inline=True)
      embed.add_field(name="Server ID", value=guild_id, inline=True)
      embed.add_field(name="Region", value=region, inline=True)
      embed.add_field(name="Member Count", value=memberCount, inline=True)
  
      await ctx.send(embed=embed)