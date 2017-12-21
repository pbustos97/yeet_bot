#!/usr/bin/python
import sys
import asyncio
import discord
import random
from discord.ext import commands
import yeet_bot_id
from yeet_bot_id import yeet_txt_token

bot = commands.Bot(command_prefix=commands.when_mentioned_or('$'), description='Meme bot')
#bot.add_cog(Music(bot))

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
        time.sleep(1)
        await bot.send_message(message.channel, 'we makin noise')
    elif message.content.startswith('stfu'):
        await bot.send_message(message.channel, 'ok')
    elif message.content.startswith('trader'):
        await bot.send_message(message.channel, '{0.author.mention} is now a trader'.format(message))
    elif message.content.startswith('8ball'):
        rando = random.randint(0,3)
        if(rando == 1):
            await bot.send_message(message.channel, '{0.author.mention} no'.format(message))
        elif(rando == 0):
            await bot.send_message(message.channel, '{0.author.mention} yes'.format(message))
        elif(rando == 2):
            await bot.send_message(message.channel, '{0.author.mention} maybe'.format(message))
        elif(rando == 3):
            await bot.send_message(message.channel, '{0.author.mention} fuk u'.format(message))
    elif message.content.startswith('http') or message.content.startswith('www'):
        rando = random.randint(0,3)
        if (rando == 0):
            await bot.send_message(message.channel, '{0.author.mention} you sent something <:weenie:313002452045660172>'.format(message))
        elif (rando == 1):
            await bot.send_message(message.channel, '{0.author.mention} I aint clickin that sus ass link <:christucker:375486748018343938>'.format(message))
        elif (rando == 2):
            await bot.send_message(message.channel, '{0.author.mention} I hope it\'s porn <:dram:313002361847152640>'.format(message))
        elif (rando == 3):
            await bot.send_message(message.channel, '{0.author.mention} lit!'.format(message))
@bot.event
async def on_ready():
    print('Logged in as:\n{0} (ID: {0.id})'.format(bot.user))

bot.run(yeet_txt_token)