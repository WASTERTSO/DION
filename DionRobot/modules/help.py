from telethon import events, Button
from DionRobot import dion

btn =[
    [Button.inline("⦁ ᴀᴅᴍɪɴ ⦁", data="admin"), Button.inline("⦁ ʟᴏᴄᴋs ⦁", data="locks")],
    [Button.inline("⦁ ᴘᴜʀɢᴇs ⦁", data="purges"), Button.inline("⦁ ᴜsᴇʀɪɴғᴏ ⦁", data="misc")],
    [Button.inline("⦁ ᴢᴏᴍʙɪᴇs ⦁", data="zombies"), Button.inline("Back", data="home")]]


HELP_TEXT = """
**ɢᴏᴋᴜ ʜᴇʟᴘ ᴍᴇɴᴜ:**

/start ⤷ ᴛᴏ sᴛᴀʀᴛ ᴍᴇ ;)
/help ⤷ ᴛᴏ ɢᴇᴛ ᴀᴠᴀɪʟᴀʙʟᴇ ʜᴇʟᴘ ᴍᴇɴᴜ 

__ʀᴇᴘᴏʀᴛ ʙᴜɢs ᴀᴛ__ @TSO_CHATS
ᴀʟʟ ᴄᴍᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ </> ᴏʀ <!>
"""


@dion.on(events.NewMessage(pattern="[!?/]help ?(.*)"))
async def help(event):
    if event.is_group:
       await event.reply("ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ ɪɴ ᴘᴍ ғᴏʀ ʜᴇʟᴘ", 
       buttons=[
       [Button.url("⦁ ʜᴇʟᴘ ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅs ⦁", "https://t.me/Goku_Godxbot?start=help")]])
       return

    await event.reply(HELP_TEXT, buttons=btn)

@dion.on(events.NewMessage(pattern="^/start help"))
async def shelp(event):
    if event.is_group:
       await event.reply("ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ ɪɴ ᴘᴍ ғᴏʀ ʜᴇʟᴘ", 
       buttons=[
       [Button.url("⦁ ʜᴇʟᴘ ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅs ⦁", "https://t.me/Goku_Godxbot?start=help")]])
       return

    await event.reply(HELP_TEXT, buttons=btn)


@dion.on(events.callbackquery.CallbackQuery(data="help"))
async def chelp(event):
     await event.edit(HELP_TEXT, buttons=btn)
