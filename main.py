import discord
import os
import requests
import json
import random
from replit import db

client = discord.Client()

sad_words = ["sad", "depressed", "unhappy", "fucked", "miserable", "fucking", "sucked"]

starter_encouragements = ["Cheer Up!", "Hang in there!", "Have faith in God!", "We'll win!", "Fight till death!",
                          "Don't lose to losers"]


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    data = json.loads(response.text)
    quote = data[0]['q'] + " -" + data[0]['a']
    return quote


def update_encouragements(eng):
    if "encouragements" in db.keys():
        encouragements = db['encouragements']
        encouragements.append(eng)
        db["encouragements"] = encouragements

    else:
        db["encouragements"] = [eng]


def delete_encouragements(index):
    encouragements = db["encouragements"]
    if len(encouragements) > index:
        del (encouragements[index])
        db["encouragements"] = encouragements


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content
    if message.content.startswith('hello'):
        await message.channel.send(
            "Hello ! I'm Innovo Bot. If you have any questions about our server , I'd be glad to help you")
    elif message.content.startswith('hi'):
        await message.channel.send("How's it going ! I'm Innovo Bot. I'd be glad to help you with your requests")
    elif message.content.startswith('$vscode'):
        await message.channel.send(
            "Visual Studio Code is a code editor redefined and optimized for building and debugging modern web and cloud applications. Visual Studio Code is free and opern source. It's the industry standard IDE/Code Editor for Web Development")
    elif message.content.startswith('$pycharm'):
        await message.channel.send(
            "Pycharm is 'The Python IDE for Professional Developers'. It's the industry standard for Python  Developers")
    elif message.content.startswith('$help'):
        await message.channel.send(
            "We'll help you as soon as we can. But you should google to find solutions or ask on stack overflow/reddit or any other dev community first. Open a ticket for us to help you by typing '- ticket'")
    elif message.content.startswith('$thx'):
        await message.channel.send("Your welcome! It is my pleasure to help you")
    elif message.content.startswith('$bye'):
        await message.channel.send("Bye Bye! Hope to meet you soon again !")

    options = starter_encouragements
    if "encouragement" in db.keys():
        options += db["encouragements"]
    elif message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)
    elif message.content.startswith('$boss'):
        await message.channel.send("Mubashir and Madhav are my bosses. They're awesome. They are tech artists")
    elif message.content.startswith('$owners'):
        await message.channel.send("dingus45191(tycoon1) and Angelo")
    elif message.content.startswith('$who-owners'):
        await message.channel.send("dingus45191(tycoon1) is Mohammed Mubashir Hasan and Angelo is Madhav Anand")
    elif message.content.startswith('$contact-owners'):
        await message.channel.send(
            "You can reach Mubashir at mubashirhasan716@gmail.com and Madhav at madhav1004@icloud.com")
    elif message.content.startswith('$contact'):
        await message.channel.send("You can contact us at innovoinc.dev@gmail.com or in our official discord server.")
    elif message.content.startswith('$contribute-bot'):
        await message.channel.send(
            "I am officially hosted on repl.it. Here's the link https://repl.it/@Mubashir45191/InnovoBot.")


    elif any(word in msg for word in sad_words):
        await message.channel.send(random.choice(options))
    elif message.content.startswith('$neweng'):
        eng = msg.split("$neweng ", 1)[1]
        update_encouragements(eng)
        await message.channel.send('New encouraging message added.')
    elif message.content.startswith('$listeng'):
        encouragements = db["encouragements"]
        await message.channel.send(encouragements)

    elif message.content.startswith('$deleng'):
        encouragements = []
        if "encouragements" in db.keys():
            index = msg.split("$deleng", 1)[1]
            delete_encouragements(index)
            encouragements = db['encouragements']
            await message.send('Message deleted')

client.run(os.getenv('TOKEN'))