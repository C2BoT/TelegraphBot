from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
[ ](https://telegra.ph/file/5d44fc68de9464aca53b3.mp4)
𝑯𝑬𝒀 {}
𝑾𝑬𝑳𝑪𝑶𝑴𝑬 𝑻𝑶 {}

𝑰 𝑪𝑨𝑵 𝑼𝑷𝑳𝑶𝑨𝑫 𝑴𝑬𝑫𝑰𝑨 𝑻𝑶 telegra.ph 𝑨𝑵𝑫 𝑮𝑰𝑽𝑬 𝒀𝑶𝑼 𝑩𝑨𝑪𝑲 𝑻𝑯𝑬 𝑳𝑰𝑵𝑲 𝑾𝑰𝑻𝑯 𝑬𝑨𝑺𝑬 𝑻𝑬𝒀 𝑺𝑬𝑵𝑫𝑰𝑵𝑮 𝑴𝑼𝑳𝑻𝑰𝑷𝑳𝑬 𝑴𝑬𝑫𝑰𝑨 𝑨𝑵𝑫 𝑰𝑻 𝑺𝑻𝑰𝑳𝑳 𝑾𝑶𝑵'𝑻 𝑺𝑻𝑶𝑷 𝑴𝑬
𝑰 𝑪𝑨𝑵 𝑨𝑳𝑺𝑶 𝑩𝑬 𝑼𝑺𝑬𝑫 𝑰𝑵 𝑮𝑹𝑶𝑼𝑷𝑺 

𝑻𝑶 𝑺𝑬𝑬 𝑺𝑼𝑷𝑷𝑶𝑹𝑻𝑬𝑫 𝑴𝑬𝑫𝑰𝑨 𝑻𝒀𝑷𝑬𝑺 𝑻𝑨𝑷 𝑻𝑯𝑬 𝑹𝑬𝑳𝑨𝑻𝑬𝑫 𝑩𝑼𝑻𝑻𝑶𝑵 𝑩𝑬𝑳𝑶𝑾
𝑼𝑺𝑬 𝑻𝑯𝑬 𝑶𝑻𝑯𝑬𝑹 𝑩𝑼𝑻𝑹𝑶𝑵𝑺 𝑻𝑶 𝑲𝑵𝑶𝑾 𝑴𝑶𝑹𝑬 𝑨𝑩𝑶𝑼𝑻 𝑴𝑬 𝑨𝑵𝑫 𝑴𝒀 𝑼𝑺𝑨𝑮𝑬
    """

    # Help Message
    HELP = """
**𝑹𝑬𝑨𝑫 𝑩𝑬𝑳𝑶𝑾 𝑻𝑶 𝑲𝑵𝑶𝑾 𝑯𝑶𝑾 𝑻𝑶 𝑼𝑺𝑬 𝑴𝑬**

𝑺𝑬𝑬 𝑺𝑼𝑷𝑷𝑶𝑹𝑻𝑬𝑫 𝑴𝑬𝑫𝑰𝑨 𝑻𝒀𝑷𝑬𝑺 𝑩𝒀 𝑪𝑳𝑰𝑪𝑲𝑰𝑵𝑮 𝑻𝑯𝑨𝑻 𝑹𝑬𝑳𝑬𝑫 𝑩𝑼𝑻𝑻𝑶𝑵 𝑩𝑬𝑳𝑶𝑾

**𝑯𝑶𝑾 𝑻𝑶 𝑼𝑺𝑬 𝑴𝑬 𝑯𝑬𝑹𝑬**
𝑱𝑼𝑺𝑻 𝑺𝑬𝑵𝑫 𝑻𝑯𝑬 𝑴𝑬𝑫𝑰𝑨 𝑨𝑵𝑫 𝑳𝑬𝑨𝑽𝑬 𝑹𝑬𝑺𝑻 𝑶𝑵 𝑴𝑬 

**𝑯𝑶𝑾 𝑻𝑶 𝑼𝑺𝑬 𝑰𝑵 𝑮𝑹𝑶𝑼𝑷**
𝑨𝑫𝑫 𝑻𝑶 𝑴𝑬 𝑻𝑯𝑬 𝑮𝑹𝑶𝑼𝑷
𝑻𝑯𝑬𝑵 𝑹𝑬𝑷𝑳𝒀 𝑻𝑶 𝑨 𝑴𝑬𝑫𝑰𝑨 𝑾𝑰𝑻𝑯 /telegraph 𝑻𝑶 𝑮𝑬𝑻 𝑻𝑯𝑬 telegra.ph 𝑳𝑰𝑵𝑲
𝒀𝑶𝑼 𝑪𝑨𝑵 𝑨𝑳𝑬𝑹𝑵𝑨𝑻𝑰𝑽𝑬𝑳𝒀 𝑨𝑳𝑺𝑶 𝑼𝑺𝑬  "𝑻" 𝑶𝑹 "𝑻𝑮" 𝑨𝑺 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺 𝑨𝑵𝑫 "!" 𝑨𝑺 𝑷𝑹𝑬𝑭𝑰𝑿 𝑻𝑶 𝑫𝑶 𝑻𝑯𝑬 𝑺𝑨𝑴𝑬
𝑻𝑯𝑨𝑻 𝑰𝑺

/t   ,   /tg   ,   /telegraph

𝑳𝑭 𝒀𝑶𝑼 𝑨𝑫𝑫 𝑰𝑵 𝒀𝑶𝑼𝑹 𝑮𝑹𝑶𝑼𝑷 𝒀𝑶𝑼𝑹 𝑮𝑹𝑶𝑼𝑷 𝑼𝑺𝑬𝑹𝑺 𝑾𝑶𝑵'𝑻 𝑵𝑬𝑬𝑫 𝑻𝑶 𝑱𝑶𝑰𝑵 𝑶𝑼𝑹 𝑪𝑯𝑨𝑵𝑵𝑬𝑳

𝑵𝑶𝑻𝑬 : 𝑳𝑭 𝑻𝑯𝑬 𝑩𝑶𝑻 𝑫𝑶𝑬𝑺𝑵'𝑻 𝑹𝑬𝑺𝑷𝑶𝑵𝑫 𝑰𝑵 𝑻𝑯𝑬 𝑬𝑿𝑷𝑬𝑪𝑻𝑬𝑫 𝑾𝑨𝒀, 𝑴𝑨𝑲𝑬 𝑻𝑯𝑬 𝑩𝑶𝑻 𝑨𝑫𝑴𝑰𝑵 𝑺𝑶 𝑻𝑯𝑨𝑻 𝑩𝑶𝑻 𝑮𝑬𝑻𝑺 𝑼𝑷𝑫𝑨𝑻𝑬𝑺 𝑭𝑶𝑹 𝑺𝑼𝑹𝑬 𝑻𝑬𝑳𝑬𝑮𝑹𝑨𝑴 𝑰𝑺 𝑾𝑬𝑰𝑹𝑫
𝑴𝑶𝑹𝑬 𝑭𝑬𝑨𝑻𝑼𝑹𝑬𝑺 𝑰𝑵 𝑫𝑬𝑽𝑬𝑳𝑶𝑷𝑴𝑬𝑵𝑻 𝑲𝑬𝑬𝑷 𝑻𝑹𝑨𝑪𝑲 𝑩𝒀 𝑱𝑶𝑰𝑵𝑮 @us7a5
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
