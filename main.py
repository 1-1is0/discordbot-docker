# bot.py
import os
import random

import discord
# from dotenv import load_dotenv
# from dotenv import load_dotenv

# load_dotenv()
# load_dotenv()
TOKEN = os.getenv('TOKEN')


client = discord.Client()

@client.event
async def on_ready():

    print("Wizard cat waking up")
    # this won't work on windows or sometings other than bash
    print("\x1B[3m> Wizard cat\x1B[23m: Alohomora")
    game = discord.Game("Riddikulus")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    # if message.author == client.user:
    # return
    print("Wizard cat receive a message from guild", message.guild)
    

    if message.content in ['wiz rand', 'wiz wiz', 'wiz']:
        if message.guild:
            guild = message.guild
            real_members = [member.name for member in guild.members if 
                member.bot == False and member.status is discord.Status.online]
            # response = message
            random.shuffle(real_members)
            response = "Go ahead \n-" + "\n- ".join(real_members)
            print(response)
        else:
            response = "This command only works in guild"
        await message.channel.send(response)

    elif message.content == 'wiz backup':
        members = ["Name 1", "Name 2", "Name 3", "Name 4", "Name 5"]
        random.shuffle(members)
        response = "Go ahead \n-" + "\n- ".join(members)
        await message.channel.send("")

    elif message.content.lower() == 'avada kedavra':
        await message.channel.send("F TO YOU!")

    elif message.content.lower() in ['tink', 'think', 'wiz tink', 'wiz think']:
        await message.channel.send("Don't EVER TINK")

    elif message.content == "wiz help":
        await message.channel.send(
"""
```
wiz help
    show this page.
wiz wiz
    let your wizard cat tell you a random list of users (non-bot) in this server.
```""")


@client.event
async def on_guild_join(guild):
    print(guild.channels)
    print([i.type for i in guild.channels])
    text_channel = [channel for channel in guild.channels if channel.type is discord.ChannelType.text]

    print(text_channel)
    await text_channel[0].send("Avada Kedavra, MEOW")

print("THE TOKEN IS", TOKEN)
client.run(TOKEN)
