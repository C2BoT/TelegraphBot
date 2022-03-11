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
    text = STARTT_TEXT.format(query.from_user.first_name, query.from_user.last_name, query.from_user.username, query.from_user.id, query.from_user.mention, query.from_user.dc_id, query.from_user.language_code, query.from_user.status)
    reply_markup = STARTT_CLOSE
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup,
        quote=True
    )


STARTT_TEXT = """
= = = = = = = = = = = = = = = =
❤️🇺🇸 𝐅𝐢𝐫𝐬𝐭 𝐍𝐚𝐦𝐞 : <b>{}</b>
🇺🇸❤️ 𝐒𝐞𝐜𝐨𝐧𝐝 𝐍𝐚𝐦𝐞 : <b>{}</b>
❤️🇺🇸 𝐔𝐬𝐞𝐫𝐍𝐚𝐦𝐞 : <b>@{}</b>
🇺🇸❤️ 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐈𝐃 : <code>{}</code>
❤️🇺🇸 𝐏𝐫𝐨𝐟𝐢𝐥𝐞 𝐋𝐢𝐧𝐤 : <b>{}</b>
🇺🇸❤️ 𝐃𝐂 : <b>{}</b>
❤️🇺🇸 𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞 : <b>{}</b>
🇺🇸❤️ 𝐒𝐭𝐚𝐭𝐮𝐬 : <b>{}</b>
= = = = = = = = = = = = = = = = 
"""

STARTT_CLOSE = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton("𝙲𝙻𝙾𝚂𝙴 🔐", callback_data="close")
        ]]
    )
