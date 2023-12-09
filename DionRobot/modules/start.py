from DionRobot import dion

from telethon import events, Button


START_TEXT = """
**ʜᴇʟʟᴏ [{}](tg://user?id={})!**

**ɪ'ᴍ sᴜᴋᴜɴᴀ ɢᴏᴅ ᴏғ ᴄᴜʀᴇs!**

**ɴᴏᴡ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ɪ'ᴍ ᴍᴀɴᴀɢᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ!**
"""


START_BTN = [
                [
                    Button.url("Add me to your group", "https://t.me/DionRobot?startgroup")
                ],
                [
                    Button.url("Repo", "https://github.com/SeorangDion/DionBot"),
                    Button.url("Updates", "https://t.me/DionProjects")
                ],
                [
                    Button.inline("Help And Commands", data="help")
                ]
            ]


@dion.on(events.NewMessage(pattern="^[?!/]start ?(.*)"))
async def start(event):

    if event.is_private:
       await event.reply(START_TEXT.format(event.sender.first_name, event.sender_id), buttons=START_BTN
       )
       return

    if event.is_group:
       await event.reply("**Hi, I'm Dion Robot, Thanks for using me**",
        buttons=
        [
            [
                Button.url("Updates", "https://t.me/DionProjects"),
                Button.url("Support", "https://t.me/DionSupport")
            ]
        ]
       )
       return


@dion.on(events.callbackquery.CallbackQuery(data="home"))
async def hstart(event):
     await event.edit(START_TEXT.format(event.sender.first_name, event.sender_id), buttons=START_BTN)
