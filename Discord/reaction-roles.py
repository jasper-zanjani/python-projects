import os, dotenv, discord
from discord.ext import commands

dotenv.load_dotenv()
token=os.getenv('TOKEN')

client = commands.Bot(command_prefix='.')

@client.event
async def on_raw_reaction_add(payload):
  if payload.message_id == 751854496748929065 and payload.emoji.name == u"\U0001F44D":
    guild = discord.utils.find(lambda g : g.id == payload.guild_id, client.guilds)
    role = discord.utils.get(guild.roles, name='Goombalee')
    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
    await member.add_roles(role)


client.run(token)