from Zain import app, API_ID, API_HASH
from config import ALIVE_PIC
from pyrogram import filters
import os
import re
import asyncio
import time
from pyrogram import *
from pyrogram.types import * 

PHONE_NUMBER_TEXT = (
    " ✦ӇЄƳ..! MàƧƬЄƦ..!!👋!\n\n✦ Ɩ ƛM ƛ ƤƠƜЄƦƑƲԼ ⚜️ЄƬЄƦƝƖƬƳ ƲßЄƦƁƠƬ⚜️ ӇЄԼƤЄƦ?\n\n‣ Ɩ ƇƛƝ ӇЄԼƤ Ƴ9Ʋ ƬƠ ƳƠƲ ӇƠƧƬ ƳƠƲƦ ԼЄƑƬ ƇԼƖЄñƬƧ.\n\n‣ ӇЄԼƤЄƦ ✦: [⚜️ƇӇƛƝƝЄԼ](https://t.me/About_Zain) \n\n‣ ƬӇƖƧ ƖƧ ƧƤЄƇƖƛԼ ƑƠƦ ƓƛƝƊƲ ƤЄƠƤԼЄ'Ƨ(ԼƛȤƳ)\n\n‣ ƝƠƜ /clone {send your PyroGram ᴠ2 String Session}"
)

@app.on_message(filters.command("start"))
async def hello(client: app, message):
    buttons = [
           [
                InlineKeyboardButton("⚜️ƠƜƝЄƦ", url="t.me/The_Eternity_Soul"),
            ],
            [
                InlineKeyboardButton("🔰ƇӇƛƝƝЄԼ", url="t.me/About_Zain"),
            ],
            [
                InlineKeyboardButton("🌟ƧƲƤƤƠƦƬ", url="https://t.me/+Mod-Itq-TwBlNjY1"),
            ],
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await client.send_photo(message.chat.id, ALIVE_PIC, caption=PHONE_NUMBER_TEXT, reply_markup=reply_markup)

# © By About_Zain and gives credits.
@app.on_message(filters.command("clone"))
async def clone(bot: app, msg: Message):
    chat = msg.chat
    text = await msg.reply("Usage:\n\n /clone session")
    cmd = msg.command
    phone = msg.command[1]
    try:
        await text.edit("ᴡᴀɪᴛ ʙᴀʙʏ ғᴇᴡ sᴇᴄᴏɴᴅs...💌")
                   # change this Directry according to ur repo
        client = Client(name="Melody", api_id=API_ID, api_hash=API_HASH, session_string=phone, plugins=dict(root="Zain/modules"))
        await client.start()
        user = await client.get_me()
        await msg.reply(f" ᴊᴀ ᴘᴇʟ ᴅᴇ sᴀʙᴋᴏ ᴀʙ ȤƛƖƝ ᴋᴏ ʙᴀᴀᴘ ʙᴏʟ ᴋᴇ ᴊᴀɴᴀ 🥵 {user.first_name} 💨.")
    except Exception as e:
        await msg.reply(f"**ERROR:** `{str(e)}`\nPress /start to Start again.")
