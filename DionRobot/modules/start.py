from DionRobot import dion

from telethon import events, Button


START_TEXT = """
**ʜᴇʏ [{}](tg://user?id={})!**

**ᴛʜɪs ɪs ɢᴏᴋᴜ 🐉**

**ɪ'ᴍ ᴍᴏsᴛ ᴘᴏᴡᴇʀғᴜʟ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ + ᴍᴜsɪᴄ ʙᴏᴛ ᴡɪᴛʜ ᴀᴡsᴏᴍᴇ ᴀɴᴅ ᴜsᴇғᴜʟ ғᴇᴀᴛᴜʀᴇs ࿈**
"""


START_BTN = [
                [
                    Button.url("⦁ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ⦁", "https://t.me/Goku_Godxbot?startgroup")
                ],
                [
                    Button.url("⦁ sᴜᴘᴘᴏʀᴛ ⦁", "https://t.me/Tso_Chats"),
                    Button.url("⦁ ᴜᴘᴅᴀᴛᴇs ⦁", "https://t.me/Godx_Bots")
                ],
                [
                    Button.inline("⦁ ʜᴇʟᴘ ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅs ⦁", data="help")
                ]
            ]


@dion.on(events.NewMessage(pattern="^[?!/]start ?(.*)"))
async def start(event):

    if event.is_private:
       await event.reply(START_TEXT.format(event.sender.first_name, event.sender_id), buttons=START_BTN
       )
       return

    if event.is_group:
       await event.reply("**ʜᴇʏ ɪ'ᴍ ɢᴏᴋᴜ ᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ᴍᴇ**",
        buttons=
        [
            [
                Button.url("⦁ ᴜᴘᴅᴀᴛᴇs ⦁", "https://t.me/Godx_Bots"),
                Button.url("⦁ sᴜᴘᴘᴏʀᴛ ⦁", "https://t.me/Tso_chats")
            ]
        ]
       )
       return


@dion.on(events.callbackquery.CallbackQuery(data="home"))
async def hstart(event):
     await event.edit(START_TEXT.format(event.sender.first_name, event.sender_id), buttons=START_BTN)
