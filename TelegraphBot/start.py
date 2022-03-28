from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant 

# Start Message

force_channel = "us7a5"

@bot.on_message(filters.command("start"))
async def start(bot, msg):
    if force_channel:
        try:
            user = await bot.get_chat_member(force_channel, msg.from_user.id)
            if user.status == "kicked out":
                return
        except UserNotParticipant:
            await message.reply_text(
                text="𝙹𝙾𝙸𝙽 𝙼𝚈 𝚄𝙿𝙳𝙰𝚃𝙴 ➻ @us7a5",
                reply_markup=InlineKeyboardMarkup( [[
                 InlineKeyboardButton("𝗡𝗘𝗪 𝗬𝗢𝗥𝗞 ✈", url=f"https://t.me/us7a5")
                 ]]
                )
            )
            return
@Client.on_message(filters.private & filters.incoming & filters.command("start"))
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

⌯ [𝙽𝙴𝚆 𝚈𝙾𝚁𝙺](https://t.me/us7a5)
= = = = = = = = = = = = = = = = 
"""

STARTT_CLOSE = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton("𝙲𝙻𝙾𝚂𝙴 🔐", callback_data="close")
        ]]
    )
