import discord
from discord.ext import commands

class Game(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def game(self, ctx):
      print('Playing game')
      await self.client.change_presence(activity=discord.Game('Fall Guys'))

    @commands.command()
    async def nogame(self, ctx):
      print('Clearing game')
      await self.client.change_presence(activity=None)


    @commands.command()
    async def red(self, ctx):
      print('Going red')
      await self.client.change_presence(status=discord.Status.dnd)

    @commands.command()
    async def yellow(self, ctx):
      print('Going yellow')
      await self.client.change_presence(status=discord.Status.idle)
      
    # @commands.command()
    # async def stream(self, ctx):
    #   await self.client.change_presence(activity=discord.Streaming)
    
    @commands.command()
    async def clear(self, ctx):
      print('Clearing status')
      await self.client.change_presence(status=discord.Status.online)

    @commands.command()
    async def afk(self, ctx):
      print('afk')
      await self.client.change_presence(afk=True)

    # @commands.command()
    # async def kick(self, ctx, member : discord.Member, *, reason = None):
    #     await member.kick(reason=reason)

    # @commands.command()
    # async def ban(self, ctx, member : discord.Member, *, reason = None):
    #     await member.ban(reason=reason)

def setup(client):
    client.add_cog(Game(client)) 