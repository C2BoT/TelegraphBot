from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant 

# Start Message

force_channel = "us7a5"

@Client.on_message(filters.command("start"))
async def start_cmd(bot, msg):
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


    await msg.reply_text("Sent message")
