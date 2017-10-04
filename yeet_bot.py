import sys
sys.path.insert(0, 'D:/Daniel/Documents/Discord/bot_ids')

import yeet_bot_id
from yeet_bot_id import yeet_token
import time
import discord
import asyncio
import random
import pickle
import os

client = discord.Client()
bot_prefix = '!'

@client.event
async def onReady():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('--------')

@client.event
async def on_message(message):
    if message.content.startswith('!shutup'):
        await client.send_message(message.channel, '@SVINT#4084 shut up.')
    elif message.content.startswith('yah'):
        await client.send_message(message.channel, 'yeet')
    elif message.content.startswith('!ting'):
        await client.send_message(message.channel, 'the ting go skrrra! pa pa ka ka ka!')
    elif message.content.startswith('hol up'):
        await client.send_message(message.channel, 'we dem boyz')
        time.sleep(1)
        await client.send_message(message.channel, 'we makin noise')
client.run(yeet_token)