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
from yeet_bot_id import botRater

bot = commands.Bot(command_prefix=commands.when_mentioned_or('$'), description='Meme bot')

# Returns a response choosing a sequence of strings or a random response
def caller(message, author):
    msg = message.content.split()
    msg = msg[1:]
    if len(msg) > 1 and (' or ' in message.content or ';' in message.content):
        string = ''
        if ' or ' in message.content:
            string = message.content.split(" or ")
        if ';' in message.content:
            string = message.content.split(";")
        string[0] = string[0].replace(botCaller, " ")
        size = len(string)
        size -= 1
        rando = random.randint(0, size)
        response = '{0.author.mention} ' + string[rando]
        return response.format(message)
    else:
        rando = random.randint(0, len(response8Ball) - 1)
        response = '{0.author.mention} ' + response8Ball[rando]
        return response.format(message)

# Returns a random number from 0 to 10 (default) or 0 to n (user input)
def rngCaller(message, author):
    rando = 0
    msg = message.content.split()
    if len(msg) > 1:
        if msg[1].isdigit():
            rando = random.randint(0, int(msg[1]))
    else:
        rando = random.randint(0,10)
    response = '{0.author.mention} ' + str(rando)
    return response.format(message)

# Returns random reaction string if URL detected
def httpCaller(message, author):
    response = ''
    rando = random.randint(0, len(linkResponse))
    if (rando >= 0 and rando < len(linkResponse)):
        response = linkResponse[rando]
    return response.format(message)

# Returns string from preset dictionary
def spamCaller(message, author):
    msg = message.content.split()
    response = botDict.get(msg[0])
    return response.format(message)

async def dispatch(function, message):
    msg = ''

    # Try block necessary in case input function string does not exist in DISPATCH dictionary
    try:
        func = DISPATCH[function]
    except:
        func = function

    author = message.author
    if function in botDict:
        msg = spamCaller(message, author)
    elif func == caller:
        msg = func(message, author)
    elif func == rngCaller:
        msg = func(message, author)
    elif ('http' in message.content or 'www' in message.content) and ('.com' in message.content or '.org' in message.content or '.net' in message.content or '.be' in message.content or '.tv' in message.content):
        msg = httpCaller(message, author)
    await message.channel.send(msg)

DISPATCH = {
    botCaller:      caller,
    botRater:       rngCaller,
}

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    msg = message.content.split()
    function = msg[0]
    await dispatch(function, message)

@bot.event
async def on_ready():
    print('Logged in as:\n{0} (ID: {0.id})'.format(bot.user))

bot.run(yeet_txt_token)
