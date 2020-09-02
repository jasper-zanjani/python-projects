from discord.ext import  commands
import discord

class Guild(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def guildinfo(self, ctx, guild: discord.Guild = None ):
    guild = ctx.guild if not guild else guild
    embed = discord.Embed(title=f'Information about guild {guild}',
                          description="Description here",
                          timestamp= ctx.message.created_at,
                          color=discord.Color.green(),
                          # thumbnail=guild.icon_url)
                          )
    embed.set_thumbnail(url=guild.icon_url)
    await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Guild(client)) 