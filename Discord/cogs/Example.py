import discord
import pickle
from discord.ext import commands

class Example(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online')
        guilds = self.client.guilds
        print([g.name for g in guilds])


    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'https://www.google.com')

    @commands.command()
    async def pickleme(self, ctx):
        with open('pickle','wb') as f:
            pickle.dump(ctx, f)
        return 0

def setup(c):
    c.add_cog(Example(c)) 