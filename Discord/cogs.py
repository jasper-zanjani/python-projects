import discord
from discord.ext import commands
import dotenv
import os
import glob

dotenv.load_dotenv()
token = os.getenv('TOKEN')


client = commands.Bot(command_prefix='.')

@client.command()
async def load(ctx, extension):
  client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
  client.unload_extension(f'cogs.{extension}')

# for f in os.listdir(''):
#   if f.endswith('.py'):
#     client.load_extension(f'cogs.{f[:-3]}')

cogs = [f[:-3] for f in glob.glob('./cogs/*.py')]
for c in cogs:
  client.load_extension(f'cogs.{c}')

client.run(token)