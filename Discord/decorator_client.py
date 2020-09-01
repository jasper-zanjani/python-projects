import asyncio
import dotenv
import os
import discord
import random
import requests
from discord.ext.commands import Bot


dotenv.load_dotenv()
token = os.getenv('TOKEN')

client = Bot(command_prefix=["?", "!"])

@client.command(name='8ball', description='Answers a yes/no question', brief='Answers from beyond', aliases=['eight_ball','eightball','8-ball'])
async def eight_ball(ctx):
    possible_responses = ':smiley: Once upon a midnight dreary, :grin: While I pondered weak and weary, :laughing: Over many a quaint and curious volume of forgotten lore, :joy: While I nodded nearly napping, :rofl: Suddenly there came a rapping, :heart_eyes: As of someone gently tapping, :relieved: Tapping at my chamber door.'.split(", ")
    await ctx.send(f'{random.choice(possible_responses)}, {ctx.message.author.mention}')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="Fall Guys"))

@client.command()
async def bitcoin(ctx):
    url='https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    response = requests.get(url)
    value = response.json()['bpi']['USD']['rate']
    await ctx.send(f'Bitcoin price is: {value}')


# async def list_servers():
#     await decorator_client.wait_until_ready()
#     while not decorator_client.is_closed:
#         print('Current servers:')
#         for server in decorator_client.servers:
#             print(server.name)
#         await asyncio.sleep(6)

# decorator_client.loop.create_task(list_servers())
client.run(token)
