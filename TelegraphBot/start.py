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
	user = await bot.get_me()
	mention = user["mention"]
	await bot.send_message(
		msg.chat.id,
		Data.START.format(msg.from_user.mention, mention),
		reply_markup=InlineKeyboardMarkup(Data.buttons),
		reply_to_message_id=msg.message_id
