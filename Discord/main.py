import discord
from discord.ext import commands
import dotenv
import os

dotenv.load_dotenv()
token = os.getenv('TOKEN')

client = commands.Bot(command_prefix='.')


# client.load_extension('cogs.Status')
# client.load_extension('cogs.Admin')
client.load_extension('cogs.Guild')
# client.load_extension('cogs.Example')
# client.load_extension('cogs.Embed')
client.load_extension('cogs.DM')

if __name__ == "__main__":
    client.run(token)