import discord
from discord.ext import commands, Bot
import os, dotenv

dotenv.load_dotenv()
token = os.getenv('TOKEN')

class Client(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

client = Client()
client.add_cog