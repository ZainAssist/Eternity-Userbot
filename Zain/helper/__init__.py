import os
import sys
from pyrogram import Client



def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "Zain"])

async def join(client):
    try:
        await client.join_chat("About_Zain")
    except BaseException:
        pass
