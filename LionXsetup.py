#!/usr/bin/env python3
# (c) https://t.me/TelethonChat/37677
# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html.

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

print(
    """ Go To my.telegram.org
    Login/SignUp Using Phone Number
    Get The API_ID and API_HASH
    Paste Here......


𝗟𝗨𝗫𝗖𝗟𝗨𝗕 𝗢𝗡 𝗧𝗢𝗣 ✌︎✌︎✌︎..."""
)
𝐀𝐏𝐏_𝐈𝐃 = int(input("Enter API_ID Here : "))
𝐀𝐏𝐈_𝐇𝐀𝐒𝐇 = input("Enter API_HASH Here : ")

with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
    print(client.session.save())
    client.send_message("me", client.session.save())
