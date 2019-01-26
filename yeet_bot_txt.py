#!/usr/bin/python
import sys
import asyncio
import discord
import random
import time
from discord.ext import commands
import yeet_bot_id
from yeet_bot_id import yeet_txt_token
from yeet_bot_id import response8Ball
from yeet_bot_id import botDict
from yeet_bot_id import linkResponse
from yeet_bot_id import botCaller

bot = commands.Bot(command_prefix=commands.when_mentioned_or('$'), description='Meme bot')

@bot.event
async def on_message(message):
    msg = message.content.split()
    if msg[0] in botDict:
        await bot.send_message(message.channel, botDict.get(msg[0]).format(message))
    elif message.content.startswith(botCaller):
        rando = random.randint(0,len(response8Ball)-1)
        if ' or ' in message.content:
            string = message.content.split(" or ")
            string[0] = string[0].replace(botCaller, " ")
            size = len(string)
            size -= 1
            rando = random.randint(0,size)
            await bot.send_message(message.channel, string[rando])
        else:
            response = '{0.author.mention} ' + response8Ball[rando]
            await bot.send_message(message.channel, response.format(message))
    elif ('http' in message.content or 'www' in message.content) and ('.com' in message.content or '.org' in message.content or '.net' in message.content or '.be' in message.content):
        rando = random.randint(0,len(linkResponse))
        if (rando >= 0 and rando < len(linkResponse)):
            await bot.send_message(message.channel, linkResponse[rando].format(message))

@bot.event
async def on_ready():
    print('Logged in as:\n{0} (ID: {0.id})'.format(bot.user))
    #await bot.change_presence(game=Game(name="Roblox"))

bot.run(yeet_txt_token)