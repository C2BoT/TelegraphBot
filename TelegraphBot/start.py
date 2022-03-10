from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# Start Message
@Client.on_message(filters.private & filters.incoming & filters.command("start"))
async def start(bot, msg):
	user = await bot.get_me()
	mention = user["mention"]
	await bot.send_message(
		msg.chat.id,
		Data.START.format(msg.from_user.mention, mention),
		reply_markup=InlineKeyboardMarkup(Data.buttons),
		reply_to_message_id=msg.message_id
	)

@Client.on_message(filters.private & filters.command(["id"]))
async def id(bot, update):
    text = STARTT_TEXT.format(update.from_user.id)
    reply_markup = STARTT_BUTTONS
    reply_markup = STARTT_CLOSE
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup,
        quote=True
    )


STARTT_TEXT = """
= = = = = = = = = = = = = = = =
⌯ 𝚄𝚂𝙴𝚁 𝙸𝙳 💛💫 {}

[𝙽𝙴𝚆 𝚈𝙾𝚁𝙺](https://t.me/us7a5)
= = = = = = = = = = = = = = = = 
"""

STARTT_CLOSE = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton("𝙲𝙻𝙾𝚂𝙴 🔐", callback_data="close")
        ]]

STARTT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('💛💫 𝙹𝙾𝙸𝙽 𝚄𝙿𝙳𝙰𝚃𝙴𝚂 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 💛💫', url='https://telegram.me/us7a5')
        ]]
    )
