from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
[ ](https://telegra.ph/file/5d44fc68de9464aca53b3.mp4)
𝙷𝙴𝚈 {}

𝚆𝙴𝙻𝙲𝙾𝙼𝙴 𝚃𝙾 {}


𝙸𝙰𝙼 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝚃𝙾 «𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼.𝙿𝙷»

𝙸𝙼𝙰𝙶𝙴 𝚄𝙿𝙻𝙾𝙰𝙳𝙴𝚁 𝙱𝙾𝚃.


𝚂𝙴𝙾𝙳 𝙼𝙴 𝙰𝙽𝚈 𝙻𝙼𝙰𝙶𝙴 𝙻 𝚆𝙸𝙻𝙻 𝚄𝙿𝙻𝙾𝙰𝙳 𝚃𝙾 

«𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼.𝙿𝙷» 𝙰𝙽𝙳 𝙶𝙸𝚅𝙴 𝚈𝙾𝚄 𝙻𝙸𝙽𝙺.
    """


    # About Message
    ABOUT = """

𝙵𝚁𝙰𝙼𝙴𝚆𝙾𝚁𝙺 [𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼](docs.pyrogram.org)

𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴 [𝙿𝚈𝚃𝙷𝙾𝙽](www.python.org)

𝙽𝙴𝚆 𝚈𝙾𝚁𝙺 ❤️🍓 [𝙽𝙴𝚆 𝚈𝙾𝚁𝙺](https://t.me/us7a5)

"""


    # Home Button
    home_buttons = [
        [InlineKeyboardButton("🖤🥀 𝙽𝙴𝚆 𝚈𝙾𝚁𝙺 🖤🥀", url="https://t.me/us7a5")],
        [InlineKeyboardButton("𝙲𝙻𝙾𝚂𝙴 🔐", callback_data="close")],
        [InlineKeyboardButton(text="🏠 𝚁𝙴𝚃𝚄𝚁𝙽 𝙷𝙾𝙼𝙴 🏠", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("🖤🥀 𝙽𝙴𝚆 𝚈𝙾𝚁𝙺 🖤🥀", url="https://t.me/us7a5")
        ],
        [
            InlineKeyboardButton("💜 𝙰𝙱𝙾𝚄𝚃 💜", callback_data="about")
        ],
        [InlineKeyboardButton("𝙲𝙻𝙾𝚂𝙴 🔐", callback_data="close")]
    ]

    # Supported Media Buttons
    supported_media_buttons = [
        [InlineKeyboardButton("🖤🥀 𝙽𝙴𝚆 𝚈𝙾𝚁𝙺 🖤🥀", url="https://t.me/us7a5/")],
        [InlineKeyboardButton("𝙲𝙻𝙾𝚂𝙴 🔐", callback_data="close")],
        [InlineKeyboardButton(text="🏠 𝚁𝙴𝚃𝚄𝚁𝙽 𝙷𝙾𝙼𝙴 🏠", callback_data="home")]
    ]
