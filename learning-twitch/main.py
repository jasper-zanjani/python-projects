import dotenv
import os
from twitchio.ext import commands

dotenv.load_dotenv()
token = os.getenv('TOKEN')
client_id = os.getenv('CLIENT_ID')

bot = commands.Bot(
  irc_token = token,
  client_id=client_id,
  prefix=',',
  nick=''
)

@bot.command()
async def hello(self, ctx):
  await ctx.send(f'Hello {ctx.author.name}!')

bot.run()
