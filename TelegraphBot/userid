from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup


# id user
@Client.on_message(filters.private & filters.incoming & filters.command("id"))
async def id(bot, msg):
    await bot.send_message(
        msg.chat.id,
        Data.STARTT,
        reply_markup=InlineKeyboardMarkup(Data.idyes_buttons),
        reply_to_message_id=msg.message_id
    )
