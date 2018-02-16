#!/usr/bin/python
import sys
import asyncio
import discord
import random
import time
from discord.ext import commands
import yeet_bot_id
from yeet_bot_id import yeet_txt_token

bot = commands.Bot(command_prefix=commands.when_mentioned_or('$'), description='Meme bot')

@bot.event
async def on_message(message):
    if message.content.startswith('shutup'):
        await bot.send_message(message.channel, 'No you shut up, {0.author.mention}'.format(message))
    elif message.content.startswith('yah'):
        await bot.send_message(message.channel, 'yeet')
    elif message.content.startswith('!ting'):
        await bot.send_message(message.channel, 'the ting go skrrra! pa pa ka ka ka!')
    elif message.content.startswith('hol up'):
        await bot.send_message(message.channel, 'we dem boyz')
    elif message.content.startswith('stfu'):
        await bot.send_message(message.channel, 'ok')
    elif message.content.startswith('8ball'):
        rando = random.randint(0,5)
        if ' or ' in message.content:
            string = message.content.split(" or ")
            string[0] = string[0].replace("8ball", " ")
            size = len(string)
            size -= 1
            rando = random.randint(0,size)
            await bot.send_message(message.channel, string[rando])
        elif(rando == 1):
            await bot.send_message(message.channel, '{0.author.mention} no'.format(message))
        elif(rando == 0):
            await bot.send_message(message.channel, '{0.author.mention} yes'.format(message))
        elif(rando == 2):
            await bot.send_message(message.channel, '{0.author.mention} maybe'.format(message))
        elif(rando == 3):
            await bot.send_message(message.channel, '{0.author.mention} fuk u'.format(message))
        elif(rando == 4):
            await bot.send_message(message.channel, '{0.author.mention} never'.format(message))
        elif(rando == 5):
            await bot.send_message(message.channel, '{0.author.mention} always'.format(message))
    elif ('http' in message.content or 'www' in message.content) and ('.com' in message.content or '.org' in message.content or '.net' in message.content or '.be' in message.content):
        rando = random.randint(0,3)
        if (rando == 0):
            await bot.send_message(message.channel, 'You sent something <:weenie:313002452045660172>'.format(message))
        elif (rando == 1):
            await bot.send_message(message.channel, 'I aint clickin that sus ass link <:christucker:375486748018343938>'.format(message))
        elif (rando == 2):
            await bot.send_message(message.channel, 'I hope it\'s a giveaway <:dram:313002361847152640>'.format(message))
        elif (rando == 3):
            await bot.send_message(message.channel, 'Lit!'.format(message))
@bot.event
async def on_ready():
    print('Logged in as:\n{0} (ID: {0.id})'.format(bot.user))

bot.run(yeet_txt_token)