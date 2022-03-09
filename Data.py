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
**** 

𝑭𝑹𝑨𝑴𝑬𝑾𝑶𝑹𝑲 [𝑷𝒀𝑹𝑶𝑮𝑹𝑨𝑴](docs.pyrogram.org)

𝑳𝑨𝑵𝑮𝑼𝑨𝑮𝑬 [𝑷𝒀𝑻𝑯𝑶𝑵](www.python.org)

𝑵𝑬𝑾 𝒀𝑶𝑹𝑲 💚🐺 [𝑵𝑬𝑾 𝒀𝑶𝑹𝑲](https://t.me/us7a5)
    """

    SUPPORTED_MEDIA_TYPES = """
💚 **𝑺𝑼𝑷𝑷𝑶𝑹𝑻𝑬𝑫 𝑴𝑬𝑫𝑰𝑨 𝑻𝒀𝑷𝑬𝑺** 💚

① 𝑻𝑴𝑨𝑮𝑬
② 𝑺𝑻𝑰𝑪𝑲𝑬𝑹
③ 𝑮𝑰𝑭𝑮 𝑶𝑹 𝑨𝑵𝑰𝑴𝑨𝑻𝑰𝑶𝑵
④ 𝑽𝑰𝑫𝑬𝑶
⑤ 𝑽𝑰𝑫𝑬𝑶 𝑵𝑶𝑻𝑬 
⑥ 𝑫𝑶𝑪𝑼𝑴𝑬𝑵𝑻 (𝑽𝑰𝑫𝑬𝑶/𝑷𝑯𝑶𝑻𝑶/𝑮𝑰𝑭)


𝑵𝑶𝑻𝑬 ꨄ 𝑻𝑬𝑳𝑬𝑮𝑹𝑨𝑷𝑯 𝑯𝑨𝑺 𝑨 𝑺𝑰𝒁𝑬 𝑳𝑰𝑴𝑰𝑻 𝑶𝑭 ⑤ 𝑴𝑩
    """




    # Home Button
    home_buttons = [
        [InlineKeyboardButton("🖤🥀 𝑵𝑬𝑾 𝒀𝑶𝑹𝑲 🖤🥀", url="https://t.me/us7a5")],
        [InlineKeyboardButton("💛💫 𝑺𝑼𝑷𝑷𝑶𝑹𝑻𝑬𝑫 𝑴𝑬𝑫𝑰𝑨 𝑻𝒀𝑷𝑬𝑺 💛💫", callback_data="supported_media_types")],
        [InlineKeyboardButton("𝑪𝑳𝑶𝑺𝑬 🔐", callback_data="close")],
        [InlineKeyboardButton(text="🏠 𝑹𝑬𝑻𝑼𝑹𝑵 𝑯𝑶𝑴𝑬 🏠", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("🖤🥀 𝑵𝑬𝑾 𝒀𝑶𝑹𝑲 🖤🥀", url="https://t.me/us7a5")
        ],
        [InlineKeyboardButton("💛💫 𝑺𝑼𝑷𝑷𝑶𝑹𝑻𝑬𝑫 𝑴𝑬𝑫𝑰𝑨 𝑻𝒀𝑷𝑬𝑺 💛💫", callback_data="supported_media_types")],
        [
            InlineKeyboardButton("𝑯𝑶𝑾 𝑻𝑶 𝑼𝑺𝑬 ❔", callback_data="help"),
            InlineKeyboardButton("📥 𝑨𝑩𝑶𝑼𝑻 📥", callback_data="about")
        ],
        [InlineKeyboardButton("𝑪𝑳𝑶𝑺𝑬 🔐", callback_data="close")]
    ]

    # Supported Media Buttons
    supported_media_buttons = [
        [InlineKeyboardButton("🖤🥀 𝑵𝑬𝑾 𝒀𝑶𝑹𝑲 🖤🥀", url="https://t.me/us7a5/")],
        [InlineKeyboardButton("𝑪𝑳𝑶𝑺𝑬 🔐", callback_data="close")],
        [InlineKeyboardButton(text="🏠 𝑹𝑬𝑻𝑼𝑹𝑵 𝑯𝑶𝑴𝑬 🏠", callback_data="home")]
    ]
