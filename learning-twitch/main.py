import dotenv
import os
from twitchio.ext import commands

dotenv.load_dotenv()
token = os.getenv('TOKEN')
client_id = os.getenv('CLIENT_ID')

bot = commands.Bot(
  irc_token = token,
  client_id=client_id,
  prefix='.',
  nick='realbeardbae',
  initial_channels=['realbeardbae']

)

# @bot.command()
# async def hello(self, ctx):
#   await ctx.send(f'Hello {ctx.author.name}!')

# bot.run()

# Example from docs:
# class Bot(commands.Bot):
#  def __init__(self):
#    super().__init__(irc_token=token, client_id=client_id, nick='realbeardbae', prefix='!', initial_channels=['gmhikaru'])
#  async def event_ready(self):
#      print(f'Ready | {self.nick}')
#  async def event_message(self, message):
#      print(message.content)
#      await self.handle_commands(message)
#  @commands.command(name='test')
#  async def my_command(self, ctx):
#      await ctx.send(f'Hello {ctx.author.name}!')

# bot = commands.Bot(
#   irc_token='...',
#   api_token='test',
#   nick='mysterialpy',
#   prefix='!',
#   initial_channels=['mysterialpy']
# )

@bot.event
async def event_ready():
  print(f'Ready | {bot.nick}')

@bot.event
async def event_message(message):
  print(message.content)
  await bot.handle_commands(message)


@bot.command(name='test', aliases=['t'])
async def test_command(ctx):
    await ctx.send(f'Hello {ctx.author.name}')

bot.run()