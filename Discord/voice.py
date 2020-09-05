import discord
from discord.ext import commands
from discord.utils import get

import youtube_dl
import os, dotenv

dotenv.load_dotenv()
token = os.getenv('TOKEN')

bot = commands.Bot(command_prefix=['.'])

@bot.event
async def on_ready():
  print(f"Logged in as {bot.user.name}")


@bot.commands(pass_context=True, aliases=['j','joi'])
async def join(ctx):
  global voice
  channel = ctx.message.author.voice.channel
  voice = get(bot.voice_clients, guild=ctx.guild)

  if voice and voice.is_connected():
    await voice.move_to(channel)
  else:
    voice = await channel.connect()

@bot.commands(pass_context=True, aliases=['l','lea'])
async def leave(ctx):
  channel = ctx.message.author.voice.channel
  voice = get(bot.voice_clients, guild = ctx.guild)
  if voice and voice.is_connected()
    await voice.disconnect()
    print(f'The bot has left {channel}!')
    await ctx.send(f'Left {channel}')
  else:
    print('Bot was told to leave channel but was not in one')
    await ctx.send('Not in a voice channel')

@bot.command(pass_context=True, aliases=['p','pla'])
async def play(ctx, url:str):
  song_there = os.path.isfile('song.mp3')
  try:
    if song_there:
      os.remove('song.mp3')
      print('Removed old song file')
  except PermissionError:
    print("Trying to delete song file, but it's being played")
    await ctx.send('ERROR: Music playing')
    return
  
  await ctx.send('Getting everything ready now')

if __name__ == "__main__":
    bot.run(token)