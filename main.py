import discord
import os

client= discord.Client()

@client.event

async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event

async def on_message(message):
  if message.author== client.user:
    return

  if message.content.startswith('hello' or 'hi'):
    await message.channel.send("Hello ! I'm Innovo Bot. If you have any questions about our server , I'd be glad to help you")  
  
  client.run(os.getenv('TOKEN'))