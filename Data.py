from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
[ ](https://telegra.ph/file/5d44fc68de9464aca53b3.mp4)
π·π΄π {}

ππ΄π»π²πΎπΌπ΄ ππΎ {}


πΈπ°πΌ ππ΄π»π΄πΆππ°πΌ ππΎ Β«ππ΄π»π΄πΆππ°πΌ.πΏπ·Β»

πΈπΌπ°πΆπ΄ ππΏπ»πΎπ°π³π΄π π±πΎπ.


ππ΄πΎπ³ πΌπ΄ π°π½π π»πΌπ°πΆπ΄ π» ππΈπ»π» ππΏπ»πΎπ°π³ ππΎ 

Β«ππ΄π»π΄πΆππ°πΌ.πΏπ·Β» π°π½π³ πΆπΈππ΄ ππΎπ π»πΈπ½πΊ.
    """


    # About Message
    ABOUT = """

π΅ππ°πΌπ΄ππΎππΊ [πΏπππΎπΆππ°πΌ](docs.pyrogram.org)

π»π°π½πΆππ°πΆπ΄ [πΏπππ·πΎπ½](www.python.org)

π½π΄π ππΎππΊ β€οΈπ [π½π΄π ππΎππΊ](https://t.me/us7a5)

"""


    # Home Button
    home_buttons = [
        [InlineKeyboardButton("π€π₯ π½π΄π ππΎππΊ π€π₯", url="https://t.me/us7a5")],
        [InlineKeyboardButton("π²π»πΎππ΄ π", callback_data="close")],
        [InlineKeyboardButton(text="π  ππ΄ππππ½ π·πΎπΌπ΄ π ", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("π€π₯ π½π΄π ππΎππΊ π€π₯", url="https://t.me/us7a5")
        ],
        [
            InlineKeyboardButton("π π°π±πΎππ π", callback_data="about")
        ],
        [InlineKeyboardButton("π²π»πΎππ΄ π", callback_data="close")]
    ]

    # Supported Media Buttons
    supported_media_buttons = [
        [InlineKeyboardButton("π€π₯ π½π΄π ππΎππΊ π€π₯", url="https://t.me/us7a5/")],
        [InlineKeyboardButton("π²π»πΎππ΄ π", callback_data="close")],
        [InlineKeyboardButton(text="π  ππ΄ππππ½ π·πΎπΌπ΄ π ", callback_data="home")]
    ]
