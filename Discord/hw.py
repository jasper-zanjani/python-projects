import os, dotenv, random
import discord
from discord.ext import commands

dotenv.load_dotenv()
token=os.getenv('TOKEN')

client= commands.Bot(command_prefix='? ! .'.split(' '))

# Most basic possible hello-world

# @client.command()
# async def hello(ctx):
#   await ctx.send(f'Hello world!')

# Enriched hello-world using `Embed`

@client.command()
async def hello(ctx):
    user = ctx.message.author.name
    emoji = random.choice([':grin:', ':smiling_face_with_3_hearts:', ':smirk:'])
    embed=discord.Embed(title=f"Hello {user}!", description=f"Thank you for the attention {emoji}",color=discord.Color.magenta())
    await ctx.send(embed=embed)

client.run(token)