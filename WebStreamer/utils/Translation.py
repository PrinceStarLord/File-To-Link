# This file is a part of FileStreamBot
from WebStreamer.vars import Var
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery


class Language(object):
    class en(object):
        START_TEXT = """
<b>👋 Hᴇʏ {}</b>\n
<b>I'm Telegram Files Streaming Bot As Well Direct Links Generator</b>\n
<b>Cʟɪᴄᴋ ᴏɴ Hᴇʟᴘ ᴛᴏ ɢᴇᴛ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ</b>\n
<b><u>𝗪𝗔𝗥𝗡𝗜𝗡𝗚 🚸</u></b>\n
<b>🔞 Pᴏʀɴ ᴄᴏɴᴛᴇɴᴛꜱ ʟᴇᴀᴅꜱ ᴛᴏ ᴘᴇʀᴍᴀɴᴇɴᴛ ʙᴀɴ ʏᴏᴜ.</b>\n\n"""

        HELP_TEXT = """
<b>» Sᴇɴᴅ ᴍᴇ ᴀɴʏ ꜰɪʟᴇ (ᴏʀ) ᴍᴇᴅɪᴀ ꜰʀᴏᴍ ᴛᴇʟᴇɢʀᴀᴍ.</b>
<b>» I ᴡɪʟʟ ᴘʀᴏᴠɪᴅᴇ ᴇxᴛᴇʀɴᴀʟ ᴅɪʀᴇᴄᴛ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ !.</b>
<b>» ᴅᴏᴡɴʟᴏᴀᴅ Lɪɴᴋ Wɪᴛʜ Fᴀsᴛᴇsᴛ Sᴘᴇᴇᴅ</b>\n
<u>🔸 𝗪𝗔𝗥𝗡𝗜𝗡𝗚 🚸</u>
<b>🔞 Pʀᴏɴ ᴄᴏɴᴛᴇɴᴛꜱ ʟᴇᴀᴅꜱ ᴛᴏ ᴘᴇʀᴍᴀɴᴇɴᴛ ʙᴀɴ ʏᴏᴜ.</b>\n
<b>Cᴏɴᴛᴀᴄᴛ ᴅᴇᴠᴇʟᴏᴘᴇʀ (ᴏʀ) ʀᴇᴘᴏʀᴛ ʙᴜɢꜱ</i></b><b>: <a href='https://t.me/{}'>[ ᴄʟɪᴄᴋ ʜᴇʀᴇ ]</a></b>"""

        ABOUT_TEXT = """
<b>⚜ Mʏ ɴᴀᴍᴇ : File To Link V2</b>\n
<b>🔸Vᴇʀꜱɪᴏɴ : 2.2</b>\n
<b>🔹Lᴀꜱᴛ ᴜᴘᴅᴀᴛᴇᴅ : [29-Aug-2023 ] 09:57 AM</b>
"""

        stream_msg_text ="""
<i><u>𝗬𝗼𝘂𝗿 𝗟𝗶𝗻𝗸 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲𝗱 !</u></i>\n
<b>📂 Fɪʟᴇ ɴᴀᴍᴇ :</b> <i>{}</i>\n
<b>📦 Fɪʟᴇ ꜱɪᴢᴇ :</b> <i>{}</i>\n
<b>📥 Dᴏᴡɴʟᴏᴀᴅ :</b> <i>{}</i>\n
<b>🖥 Wᴀᴛᴄʜ :</b> <i>{}</i>\n\n
<b>🔸<u>Nᴏᴛᴇ</u> : Aʟʟ Cʀᴇᴀᴛᴇᴅ Lɪɴᴋꜱ Wɪʟʟ Exᴘɪʀᴇ Aꜰᴛᴇʀ 24 Hᴏᴜʀꜱ</b>"""

        ban_text="__Sᴏʀʀʏ Sɪʀ, Yᴏᴜ Aʀᴇ Bᴀɴɴᴇᴅ Tᴏ Usᴇ Mᴇ.__\n\n**[Cᴏɴᴛᴀᴄᴛ Dᴇᴠᴇʟᴏᴘᴇʀ](t.me/M2linksCommunity) Tʜᴇʏ Wɪʟʟ Hᴇʟᴘ Yᴏᴜ**"

# ------------------------------------------------------------------------------

class BUTTON(object):
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Hᴇʟᴘ', callback_data='help'),
        InlineKeyboardButton('Aʙᴏᴜᴛ', callback_data='about'),
        InlineKeyboardButton('Cʟᴏsᴇ', callback_data='close')
        ],
        [InlineKeyboardButton("Uᴘᴅᴀᴛᴇꜱ Cʜᴀɴɴᴇʟ", url=f'https://t.me/{Var.UPDATES_CHANNEL}')]
        ]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Hᴏᴍᴇ', callback_data='home'),
        InlineKeyboardButton('Aʙᴏᴜᴛ', callback_data='about'),
        InlineKeyboardButton('Cʟᴏsᴇ', callback_data='close')
        ],
        [InlineKeyboardButton("Uᴘᴅᴀᴛᴇꜱ Cʜᴀɴɴᴇʟ", url=f'https://t.me/{Var.UPDATES_CHANNEL}')]
        ]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Hᴏᴍᴇ', callback_data='home'),
        InlineKeyboardButton('Hᴇʟᴘ', callback_data='help'),
        InlineKeyboardButton('Cʟᴏsᴇ', callback_data='close')
        ],
        [InlineKeyboardButton("Uᴘᴅᴀᴛᴇꜱ Cʜᴀɴɴᴇʟ", url=f'https://t.me/{Var.UPDATES_CHANNEL}')]
        ]
    )
