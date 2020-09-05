from discord.ext import  commands
import discord

class Guild(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def guildinfo(self, ctx):
    guild = ctx.guild
    embed = discord.Embed(title=f'Information about guild {guild}',
                          description="Description here",
                          timestamp= ctx.message.created_at,
                          color=discord.Color.green(),
                          # thumbnail=guild.icon_url)
                          )
    embed.set_thumbnail(url=guild.icon_url)
    await ctx.send(embed=embed)

  @commands.command()
  async def channels(self, ctx):
    channels = [c.name for c in ctx.guild.channels if type(c) is discord.TextChannel]
    # print(channels)
    embed = discord.Embed(title = f'{ctx.guild.name} channels', description = '**Channels:**\n- ' + "\n- ".join(channels))
    await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Guild(client)) 