import discord
import os
import dotenv

dotenv.load_dotenv()
token = os.getenv('TOKEN')

class client(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!hello'):
            await message.channel.send(f'Hello {message.author.mention}')
        elif message.content.startswith('!bot'):
            await message.channel.send(f':wave:')

client = client()
client.run(token)

