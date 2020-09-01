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

client.run(token)
