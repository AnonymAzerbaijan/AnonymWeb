#made by @AnonymAzerbaijan

import asyncio
from telethon import TelegramClient, functions
from datetime import datetime

api_id =  # Öz API ID-nizi yazın
api_hash = ""  # Öz API hash-inizi yazın

async def update_last_name_with_time():
    async with TelegramClient("session_name", api_id, api_hash) as client:
        last_time = datetime.now().strftime("%H:%M")
        while True:
            current_time = datetime.now().strftime("%H:%M")
            
            if current_time != last_time:
                me = await client.get_me()
                new_last_name = f"{current_time}"

                if me.last_name != new_last_name:
                    await client(functions.account.UpdateProfileRequest(last_name=new_last_name))
                    print(f"Saat yeniləndi: {new_last_name}")
                
                last_time = current_time

            await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(update_last_name_with_time())