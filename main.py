import subprocess
import os
import base64
import logging
import asyncio, time
from telethon.tl import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.utils import get_display_name
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import FloodWaitError
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.channels import GetParticipantsRequest
from collections import deque
from telethon import functions
from telethon.errors.rpcerrorlist import (
    UserAlreadyParticipantError,
    UserNotMutualContactError,
    UserPrivacyRestrictedError,
)

from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.types import InputPeerUser
from config import *
mb.start()


@mb.on(events.NewMessage(outgoing=True, pattern='.check'))
async def greeting(event):
    await event.respond("The Source Is Working")
    

@mb.on(events.NewMessage(outgoing=True, pattern='.update'))
async def restart(event):
    await event.edit("**UPDATING BOT...\nPʟᴇᴀsᴇ ᴡᴀɪᴛ**")
    await asyncio.sleep(2)
    await event.edit("**Rᴇsᴛᴀʀᴛɪɴɢ ᴛʜᴇ Hᴇʀᴏᴋᴜ Cᴏɴɴᴇᴄᴛɪᴏɴ.....**")
    await asyncio.sleep(1)
    await event.edit("**Rᴇsᴛᴀʀᴛᴇᴅ ʏᴏᴜʀ ʙᴏᴛ sᴜᴄᴄᴇssғᴜʟʟʏ**\n✅✅")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit ()
 


#welcome LEGENDX
                                                                 
        
        
mb.run_until_disconnected()
