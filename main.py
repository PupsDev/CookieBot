<<<<<<< HEAD
print("Hello")
=======
import discord
import os
API_KEY = os.environ.get('DISCORD_API_KEY')

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(API_KEY)
>>>>>>> 0a3cecc2074dfd3cf521f0262242cc1e89ab089f
