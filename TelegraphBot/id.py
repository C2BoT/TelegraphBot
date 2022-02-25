from Data import Data
from pyrogram import Client, filters


@Client.on_message(filters.private & filters.command(["id"]))
async def id(bot, update):
    text = STARTT_TEXT.format(update.from_user.id)
    reply_markup = STARTT_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup,
        Data.IDUSER,
        quote=True
        
    )
