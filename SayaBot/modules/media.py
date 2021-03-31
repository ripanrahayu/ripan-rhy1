from SayaBot.modules.disable import DisableAbleCommandHandler
from SayaBot import dispatcher

from telegram.ext import CallbackContext, Filters, CommandHandler

__help__ = """
*Available commands:*\n
*Movie information:*
 • `/imdb <movie name>`: does a movie search in Imdb site\n
*Lyrics:*
 • `/lyrics <song name>`: does a lyric search for a given song name\n
*Image reverse:*
 • `/reverse`: does a *reverse image search* of the media which it was replied to\n
*Text to speech:*
 • `/tts <text>`: convert text to speech\n
*Song:*
 • `/song <song or video name>`: download songs from youtube in standard quality
*Video:*
 • `/video <song or video name>`: download videos from youtube in standard quality
"""

__mod_name__ = "Media"
__command_list__ = ["reverse", "tts", "song", "video"]
