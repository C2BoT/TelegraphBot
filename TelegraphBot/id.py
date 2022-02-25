from Data import Data
from pyrogram import Client, filters


@Client.on_message(filters.private & filters.command(["id"]))
async def id(bot, update):
    text = IDUSER.format(update.from_user.id)
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup,
        Data.IDUSER,
        quote=True
        
    )


IDUSER = """
= = = = = = = = = = = = = = = =
⌯ 𝚄𝚂𝙴𝚁 𝙸𝙳 💛💫 {}
[𝙽𝙴𝚆 𝚈𝙾𝚁𝙺](https://t.me/us7a5)
= = = = = = = = = = = = = = = = 
"""
