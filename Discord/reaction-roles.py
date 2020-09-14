import os, dotenv, discord
from discord.ext import commands
from discord.utils import find, get

dotenv.load_dotenv()
token=os.getenv('TOKEN')

client = commands.Bot(command_prefix='.')

@client.event
async def on_raw_reaction_add(payload):
  if payload.message_id == 751854496748929065 and payload.emoji.name == u"\U0001F44D":
    # Original
    # guild = discord.utils.find(lambda g : g.id == payload.guild_id, client.guilds)
    # Simpler
    # guild = client.get_guild(payload.guild_id)

    # Alternative
    guild = get(client.guilds, id=payload.guild_id)

    
    role = get(guild.roles, name='Goombalee')

    # Original
    # member = find(lambda m : m.id == payload.user_id, guild.members)
    # Simpler
    member = get(guild.members, id=payload.user_id)
    await member.add_roles(role)


client.run(token)