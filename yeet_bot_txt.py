#!/usr/bin/python
import sys
import asyncio
import discord
from discord.ext import commands
import yeet_bot_id
from yeet_bot_id import yeet_token

bot = commands.Bot(command_prefix=commands.when_mentioned_or('$'), description='Meme bot')
bot.add_cog(Music(bot))

@bot.event
async def on_message(message):
    if message.content.startswith('!shutup'):
        await bot.send_message(message.channel, '@SVINT#4084 shut up.')
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
    elif message.content.startswith('return0'):
        await sys.exit(0)

@bot.event
async def on_ready():
    print('Logged in as:\n{0} (ID: {0.id})'.format(bot.user))

bot.run(yeet_txt_token)