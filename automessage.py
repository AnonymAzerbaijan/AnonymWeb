#made by @AnonymAzerbaijan

import asyncio
from telethon import TelegramClient

api_id = 
api_hash = ''

chat_usernames = ["@qrup1", "@qrup2"]

message = ""

async def send_messages():
    async with TelegramClient('session_name', api_id, api_hash) as client:
        while True:
            for username in chat_usernames:
                try:
                    await client.send_message(username, message)
                    print(f"Mesaj göndərildi: {username}")
                    await asyncio.sleep(2)
                except Exception as e:
                    print(f"Xəta baş verdi: {username}, Xəta: {e}")
            print("Bütün qruplara mesaj göndərildi. 5 dəqiqə gözlənilir...")
            await asyncio.sleep(300)
            
asyncio.run(send_messages())