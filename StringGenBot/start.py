from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""Halo {msg.from_user.mention},
━━━━━━━━━━━━━━━━━━━━━━━━
{me2}di buat untuk Membantu anda Untuk Mengambil
String Session Telegram dengan Mudah dan AMAN!
━━━━━━━━━━━━━━━━━━━━━━━━
ᴍᴀᴅᴇ ᴡɪᴛʜ ʙʏ : [ᴀᴍᴀɴɢ](tg://user?id={OWNER_ID}) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛᴇ sᴛʀɪɴɢ", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("ᴅᴏɴᴀsɪ", url="https://t.me/amwangstore/52"),
                    InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/amangsupportgrup")
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
