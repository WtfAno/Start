import asyncio

from pyrogram.types import Message
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, CallbackQuery
from .config import Config

bot=Client(":memory:",api_id=Config.API_ID,api_hash=Config.API_HASH,bot_token=Config.BOT_TOKEN)

START_PIC = 'https://graph.org/file/f7da95a365c0f89c85fb7.jpg'
START_MESSAGE = """**ᴛʜɪꜱ ʙᴏᴛ ᴄᴀɴ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ꜱᴀᴠᴇ ꜱᴇᴄʀᴇᴛ ᴘɪᴄꜱ ᴀɴᴅ ᴠɪᴅᴇᴏꜱ ꜱᴇɴᴛ ᴡɪᴛʜ ᴛɪᴍᴍᴇʀ** \n\n**ᴄʜᴇᴄᴋ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ ᴜꜱᴇ ᴛʜɪꜱ ʙᴏᴛ**\n\n**ᴛʜᴀɴᴋ ʏᴏᴜ!!!**"""
START_BUTTONS = [
    [
        InlineKeyboardButton('Eᴠᴏɴɪᴛʏ', url='https://t.me/Evonity'),
        InlineKeyboardButton('Sᴜᴘᴘᴏʀᴛ', url='https://t.me/EvonixZone')
    ],
]
@bot.on_message(filters.command('start') & filters.private)
async def start(bot, message):
  await message.reply_photo(
        photo = START_PIC,
        caption = START_MESSAGE,
        reply_markup = InlineKeyboardMarkup(START_BUTTONS)
    )
  
bot.run() 
