from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to {}

I can upload media to telegra.ph and give you back the link with ease. Try sending multiple media, and it still won't stop me.
I can also be used in groups !!

To see `Supported Media Types` tap the related button below.
Use the other buttons to know more about me and my usage.

By @StarkBots
    """

    # Help Message
    HELP = """
**READ BELOW TO KNOW HOW TO USE ME.**

See `Supported Media Types` by clicking that related button below.

**How to use me here?**
Just send the media and leave rest on me. 

**How to use in group?**
Add to me the group.
Then reply to a media with /telegraph to get the telegra.ph link.
You can alternatively also use "t" or "tg" as commands and "!" as prefix to do the same.
That is,
!t   ,   !tg   ,   !telegraph 
/t   ,   /tg   ,   /telegraph
[If you add in your group, your group users won't need to join our channel.]

__Note__ : If the bot doesn't respond in the expected way, make the bot admin so that bot gets updates for sure. Telegram is weird.

More features in development. Keep track by joining @StarkBots.
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

⓵ 𝑻𝑴𝑨𝑮𝑬
② 𝑺𝑻𝑰𝑪𝑲𝑬𝑹
③ 𝑮𝑰𝑭𝑮 𝑶𝑹 𝑨𝑵𝑰𝑴𝑨𝑻𝑰𝑶𝑵
④ 𝑽𝑰𝑫𝑬𝑶
⑤ 𝑽𝑰𝑫𝑬𝑶 𝑵𝑶𝑻𝑬 ⧙ 𝑫𝑶𝑪𝑼𝑴𝑬𝑵𝑻 (𝑽𝑰𝑫𝑬𝑶/𝑷𝑯𝑶𝑻𝑶/𝑮𝑰𝑭)


𝑵𝑶𝑻𝑬 ꨄ 𝑻𝑬𝑳𝑬𝑮𝑹𝑨𝑷𝑯 𝑯𝑨𝑺 𝑨 𝑺𝑰𝒁𝑬 𝑳𝑰𝑴𝑰𝑻 𝑶𝑭 ⑤ 𝑴𝑩
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("✨ 𝑵𝑬𝑾 𝒀𝑶𝑹𝑲 ✨", url="https://t.me/us7a5")],
        [InlineKeyboardButton("🎇 𝑺𝑼𝑷𝑷𝑶𝑹𝑻𝑬𝑫 𝑴𝑬𝑫𝑰𝑨 𝑻𝒀𝑷𝑬𝑺 🎇", callback_data="supported_media_types")],
        [InlineKeyboardButton("𝑪𝑳𝑶𝑺𝑬 🔐", callback_data="close")],
        [InlineKeyboardButton(text="🏠 𝑹𝑬𝑻𝑼𝑹𝑵 𝑯𝑶𝑴𝑬 🏠", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("✨ 𝑵𝑬𝑾 𝒀𝑶𝑹𝑲 ✨", url="https://t.me/us7a5")
        ],
        [InlineKeyboardButton("🎇  𝑺𝑼𝑷𝑷𝑶𝑹𝑻𝑬𝑫 𝑴𝑬𝑫𝑰𝑨 𝑻𝒀𝑷𝑬𝑺 🎇", callback_data="supported_media_types")],
        [
            InlineKeyboardButton("𝑯𝑶𝑾 𝑻𝑶 𝑼𝑺𝑬 ❔", callback_data="help"),
            InlineKeyboardButton("📥 𝑨𝑩𝑶𝑼𝑻 📥", callback_data="about")
        ],
        [InlineKeyboardButton("𝑪𝑳𝑶𝑺𝑬 🔐", callback_data="close")]
    ]

    # Supported Media Buttons
    supported_media_buttons = [
        [InlineKeyboardButton("✨ 𝑵𝑬𝑾 𝒀𝑶𝑹𝑲 ✨", url="https://t.me/us7a5/")],
        [InlineKeyboardButton("𝑪𝑳𝑶𝑺𝑬 🔐", callback_data="close")],
        [InlineKeyboardButton(text="🏠 𝑹𝑬𝑻𝑼𝑹𝑵 𝑯𝑶𝑴𝑬 🏠", callback_data="home")]
    ]
