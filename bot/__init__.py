from pyrogram.types import Message
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, CallbackQuery

bot=Client(":memory:",api_id=Config.API_ID,api_hash=Config.API_HASH,bot_token=Config.BOT_TOKEN)
