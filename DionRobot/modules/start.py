from DionRobot import dion

from telethon import events, Button


START_TEXT = """
**Hi {}**
**Dion Robot is a powerful group management bot built to help you manage your group!**

**Click the below button for getting help menu!**
"""

@dion.on(events.NewMessage(pattern="^[?!/]start$"))
async def start(event):

    if event.is_private:
       await event.reply(START_TEXT.format(event.sender.first_name), 
        buttons=
        [
            [
                Button.url("Add me to your group", "https://t.me/DionRobot?startgroup")
            ]
            [
                Button.url("Repo", "https://github.com/SeorangDion/ManagerBot"),
                Button.url("Updates", "https://t.me/DionProjects")
            ]
            [
                Button.inline("Help And Commands", data="help")
            ]
        ]
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