from DionRobot import dion

from telethon import events, Button


START_TEXT = """
**ʜᴇʟʟᴏ [{}](tg://user?id={})!**

**ɪ'ᴍ sᴜᴋᴜɴᴀ ɢᴏᴅ ᴏғ ᴄᴜʀᴇs!**

**ɴᴏᴡ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ɪ'ᴍ ᴍᴀɴᴀɢᴇ ʏᴏᴜʀ ᴄᴜʀsᴇs!**
"""


START_BTN = [
                [
                    Button.url("ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ", "https://t.me/Sukuna_Godxbot?startgroup")
                ],
                [
                    Button.url("sᴜᴘᴘᴏʀᴛ", "https://github.com/SeorangDion/DionBot"),
                    Button.url("ᴜᴘᴅᴀᴛᴇs", "https://t.me/DionProjects")
                ],
                [
                    Button.inline("ᴄᴏᴍᴍᴀɴᴅs", data="help")
                ]
            ]


@dion.on(events.NewMessage(pattern="^[?!/]start ?(.*)"))
async def start(event):

    if event.is_private:
       await event.reply(START_TEXT.format(event.sender.first_name, event.sender_id), buttons=START_BTN
       )
       return

    if event.is_group:
       await event.reply("**ʜᴇʟʟᴏ, ɪ'ᴍ sᴜᴋᴜɴᴀ ɢᴏᴅ ᴏғ ᴄᴜʀsᴇs, ᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ᴍᴇ**",
        buttons=
        [
            [
                Button.url("ᴜᴘᴅᴀᴛᴇs", "https://t.me/Godx_Bots"),
                Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/Tso_chats")
            ]
        ]
       )
       return


@dion.on(events.callbackquery.CallbackQuery(data="home"))
async def hstart(event):
     await event.edit(START_TEXT.format(event.sender.first_name, event.sender_id), buttons=START_BTN)
