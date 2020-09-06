from discord.ext import commands
from discord.utils import get
import discord

class DM(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def dmme(self, ctx):
    user = ctx.author
    await user.send('Hey handsome', tts=True)
  
  @commands.command()
  async def dmowner(self, ctx):
    user_id = ctx.guild.owner_id
    user = self.client.get_user(user_id)
    print(user_id)
    await user.send(f'This guy {ctx.author.name} is creeping me out... Betta handle dat!', tts=True)

def setup(client):
  client.add_cog(DM(client))