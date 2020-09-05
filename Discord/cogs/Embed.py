from discord.ext import  commands
import discord

class Embed(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def video(self, ctx):
    embed=discord.Embed(
      title="Here's a vidya for ya",
      description="It's a surprise!",
      url="https://www.youtube.com/watch?v=pKkrCHnun0M"
    )
    embed.set_thumbnail(url="https://www.youtube.com/watch?v=pKkrCHnun0M")
    await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Embed(client)) 