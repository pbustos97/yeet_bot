import time
import webbrowser
import asyncio
import random
import pickle
import os
import sys
import discord
from discord.ext import commands
sys.path.insert(0, 'D:/Daniel/Documents/Discord/bot_ids')

import yeet_bot_id
from yeet_bot_id import yeet_token

client = discord.Client()
bot_prefix = '!'

if not discord.opus.is_loaded():
    # the 'opus' library here is opus.dll on windows
    # or libopus.so on linux in the current directory
    # you should replace this with the location the
    # opus library is located in and with the proper filename.
    # note that on windows this DLL is automatically provided for you
    discord.opus.load_opus('opus')

class VoiceEntry:
    def __init__(self, message, player):
        self.requester = message.author
        self.channel = message.channel
        self.player = player

    def __str__(self):
        fmt = '*{0.title}* uploaded by {0.uploader} and requested by {1.display_name}'
        duration = self.player.duration
        if duration:
            fmt = fmt + ' [length: {0[0]}m {0[1]}s]'.format(divmod(duration, 60))
        return fmt.format(self.player, self.requester)

    
class VoiceState:
    def __init__(self, bot):
        self.current = None
        self.voice = None
        self.bot = bot
        self.play_next_song = asyncio.Event()
        self.songs = asyncio.Queue()
        self.skip_votes = set() # a set of user_ids that voted
        self.audio_player = self.bot.loop.create_task(self.audio_player_task())

    def is_playing(self):
        if self.voice is None or self.current is None:
            return False

        player = self.current.player
        return not player.is_done()

    @property
    def player(self):
        return self.current.player

    def skip(self):
        self.skip_votes.clear()
        if self.is_playing():
            self.player.stop()

    def toggle_next(self):
        self.bot.loop.call_soon_threadsafe(self.play_next_song.set)

    async def audio_player_task(self):
        while True:
            self.play_next_song.clear()
            self.current = await self.songs.get()
            await self.bot.send_message(self.current.channel, 'Now playing ' + str(self.current))
            self.current.player.start()
            await self.play_next_song.wait()

class Music:
    """Voice related commands.
    Works in multiple servers at once.
    """
    def __init__(self, bot):
        self.bot = bot
        self.voice_states = {}

    def get_voice_state(self, server):
        state = self.voice_states.get(server.id)
        if state is None:
            state = VoiceState(self.bot)
            self.voice_states[server.id] = state

        return state

    async def create_voice_client(self, channel):
        voice = await self.bot.join_voice_channel(channel)
        state = self.get_voice_state(channel.server)
        state.voice = voice

    def __unload(self):
        for state in self.voice_states.values():
            try:
                state.audio_player.cancel()
                if state.voice:
                    self.bot.loop.create_task(state.voice.disconnect())
            except:
                pass

    @commands.command(pass_context=True, no_pm=True)
    async def join(self, ctx, *, channel : discord.Channel):
        """Joins a voice channel."""
        try:
            await self.create_voice_client(channel)
        except discord.ClientException:
            await self.bot.say('Already in a voice channel...')
        except discord.InvalidArgument:
            await self.bot.say('This is not a voice channel...')
        else:
            await self.bot.say('Ready to play audio in ' + channel.name)

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
    elif message.content.startswith('stfu'):
        await client.send_message(message.channel, 'ok')
    elif message.content.startswith('patriots'):
        await client.send_message(message.channel, 'play video')

@commands.command(pass_context=True, no_pm=True)
async def kaz(self,ctx,channel: discord.Channel):
    voice = await bot.join_voice_channel(channel)
    player = voice.create_ffmpeg_player('kaz.mp3')
    player.start()


@client.event
async def onReady():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('--------')
    
client.run(yeet_token)