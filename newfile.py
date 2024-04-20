import random
import nest_asyncio
import asyncio
from telethon import TelegramClient, events, Button
from telethon.sessions import StringSession

nest_asyncio.apply()

api_id = 24200854
api_hash = '0d9f35c4d7b1c75d7ad5efad606b0ca2'
session_string = '1BVtsOGQBuz51MTJ70uEN2OWtO3_THWbg8BXPJlRxdkt2SdHvcN2cBUi3EQTUj_5nzAjoIjvO-Ibn-FeMlcTyYNK7p5mutBt4ifVWkJQFNur38IMJ9_ZOelDQdBD_lNhuSd5_S6XpE_lJs6BYbS62avTj43PEI5MeKO9mO6wLJXYMMOS9-rMsv5BCDSjMkLXLowgohz5v7gITPMgjABkH5OZCZTeTaUSY0-cNK0sBSM8pRNJEhF5ymeHgFVKkJM4Zz2MV4AB3frNgioEpODZ_bC4MshT7eAwYCP5EwbIGK3iAaDmfxq4oOhhWfID5_ToHC78aAZYtwPI66lof4bBli04AQySyW5A='
bot_token = '7182410667:AAHMyoWRP_ahMLi_oTh5pVxY43TR5psryf0'
username = 'pop_talk'
bot_username = 'Naruto_X_Boruto_Bot'
cd = random.uniform(0.3, 0.5)
session = StringSession(session_string)
client = TelegramClient(session, api_id, api_hash, timeout=10)
bot = TelegramClient('bot_session106', api_id, api_hash)

task_is_running = False

explore_btns = [Button.inline("Disable (Recommended) \u2705", b"disable_auto_explore")], [Button.inline("Enable (Not recommended) \u26A0", b"enable_auto_explore")]
explore_msg = "**Should I enable auto explore? \n\n➤ If auto explore is enabled it will send /explore automatically after defeating a Shinobi in explores. \n\n➤ If auto explore is disabled, it will only do auto battle. After defeating a Shinobi, you will need to manually send the explore command.**"

@bot.on(events.NewMessage(chats=username, from_users=username))
async def _bot(event):
    global task_is_running
    if "Start" in event.raw_text:
        if task_is_running:
            await bot.send_message(username, "**Already Started**")
        else:
            await bot.send_message(username, explore_msg, buttons=explore_btns)
            
    if "Stop" in event.raw_text:
        if not task_is_running:
            await bot.send_message(username, "**Already Stopped \U0001f44d**")
        else:
            task_is_running = False
            await bot.send_message(username, "**Stopped \U0001f44d**")
            await client.disconnect()

@bot.on(events.CallbackQuery(data=b"start_task"))
async def start_task(event):
    global task_is_running
    if task_is_running:
        await event.answer("Already Started", alert=False)
    else:
        await event.edit(explore_msg, buttons=explore_btns)

@bot.on(events.CallbackQuery(data=b"stop_task"))
async def start_task(event):
    global task_is_running
    if not task_is_running:
        await event.answer("Already Stopped", alert=False)
    else:
        task_is_running = False
        await event.edit("**Stopped \U0001f44d**", link_preview=False)
        await client.disconnect()

@bot.on(events.CallbackQuery(data=b"enable_auto_explore"))
async def enable_auto_explore(event):
    global task_is_running, send_auto_explore
    if task_is_running:
        await event.answer("Already Started", alert=False)
    else:
        task_is_running = True
        send_auto_explore = True
        button = Button.inline("S T O P  \u274c", b"stop_task")
        await event.edit("**Auto explore enabled \u26A0 \nStarted auto EXPLORE and BATTLE**", buttons=button)
        await client.start()
        await client.send_message(bot_username, '/explore')

@bot.on(events.CallbackQuery(data=b"disable_auto_explore"))
async def disable_auto_explore(event):
    global task_is_running, send_auto_explore
    if task_is_running:
        await event.answer("Already Started", alert=False)
    else:
        task_is_running = True
        send_auto_explore = False
        button = Button.inline("S T O P  \u274c", b"stop_task")
        await event.edit("**Auto explore disabled \u2705 \nStarted auto BATTLE only**", buttons=button)
        await client.start()
        await client.send_message(bot_username, '/explore')

@client.on(events.NewMessage(chats=bot_username, from_users=bot_username))
async def handle_message(event):
    if not task_is_running:
        return

    message = event.message
    if "challenged" in message.text.lower() and message.reply_markup:
        for row in message.reply_markup.rows:
            for button in row.buttons:
                if button.text.startswith("Battle"):
                    await asyncio.sleep(cd)
                    await message.click(0)
                    return

    if message.reply_markup:
        for row in message.reply_markup.rows:
            for button in row.buttons:
                if button.text == "Chakra_Blade":
                    await asyncio.sleep(cd)
                    await message.click(0)
                    
                if button.text == "Kunai":
                    await asyncio.sleep(cd)
                    await message.click(0)
                    return


                if button.text == "Katoringu":
                    await asyncio.sleep(cd)
                    await message.click(0)
                    return

                if button.text == "Gunbai":
                    await asyncio.sleep(cd)
                    await message.click(0)
                    return

                if button.text == "Knife":
                    await asyncio.sleep(cd)
                    await message.click(0)
                    return
@client.on(events.NewMessage(chats=bot_username, from_users=bot_username)) 
async def gambit_message(event): 
    if "Death's Gambit" in event.raw_text: 
        async for message in client.iter_messages(event.chat_id, limit=1):  
            if message.reply_markup and message.reply_markup.rows: 
                found_data = None 
                for row in message.reply_markup.rows: 
                    for button in row.buttons: 
                        if button.data and len(button.data) == 33: 
                            found_data = button.data 
                            break 
                    if found_data: 
                        break 
 
                if found_data: 
                    await asyncio.sleep(random.random() + 1) 
                    await event.click(data=found_data) 
 
                 
@client.on(events.MessageEdited(chats=bot_username, from_users=bot_username)) 
async def handle_edited_message(event): 
    if not task_is_running: 
        return

    if "BLACK MARKET" in message.text and send_auto_explore:
        await asyncio.sleep(42)
        await client.send_message(bot_username, '/explore')
        return

    if any(word in message.text for word in ["You found Chakra Fragment", "dummy word"]) and send_auto_explore:
        await asyncio.sleep(2)
        await client.send_message(bot_username, '/explore')
        return

@client.on(events.MessageEdited(chats=bot_username, from_users=bot_username))
async def handle_edited_message(event):
    if not task_is_running:
        return

    edited_message = event.message
    if "You have defeated" in edited_message.text:
        await asyncio.sleep(cd)
        if send_auto_explore:
            await client.send_message(bot_username, '/explore')
    elif edited_message.reply_markup:
        for row in edited_message.reply_markup.rows:
            for button in row.buttons:
               
                if button.text == "Chakra_Blade":

                    await asyncio.sleep(cd)

                    await message.click(0)
                if button.text == "Katoringu":
                    await asyncio.sleep(cd)
                    await message.click(0)
                    return


                if button.text == "Kunai":
                    await asyncio.sleep(cd)
                    await message.click(0)
                    return

                if button.text == "Gunbai":
                    await asyncio.sleep(cd)
                    await message.click(0)
                    return

                if button.text == "Knife":
                    await asyncio.sleep(cd)
                    await message.click(0)
                    return
async def main():
    print("program started successfully")
    await client.start()
    await bot.start(bot_token=bot_token)
    await bot.send_message(username, "**\u26A0 Warning don't run in background. they're watching all exploring accounts continuesly, while exploring they will send a message randomly in bot to verify that you're auto user or player, and response that message ASAP. \n\n\u26D4 So Keep open bot chat and watch all messages from bot while this script is running to avoid getting BANNED.**")
    button = Button.inline("S T A R T", b"start_task")
    await bot.send_message(username, "**Client is ready \u2705 \n\n\U0001f916 Bot: @Naruto_X_Boruto_Bot \n\u2699 Info: Auto Explore & Battle**", buttons=button)

    await client.run_until_disconnected()
    await bot.run_until_disconnected()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
