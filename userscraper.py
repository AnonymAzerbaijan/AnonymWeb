#made by @AnonymAzerbaijan

from telethon import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.errors.rpcerrorlist import ChatAdminRequiredError, PeerFloodError
from telethon.tl.types import ChannelParticipantAdmin, ChannelParticipantCreator
import asyncio

api_id = int(input("API ID yazın: "))
api_hash = input("API Hash yazın: ")

client = TelegramClient('bot_session', api_id, api_hash)

async def main():
    source_group = await client.get_entity(input("Istifadəçı çəkəcəyiniz qrupun tagını yazın(link atmayın link atsaz id ve hashini yazdığınız hesab banlanacaq!!): "))
    target_group = await client.get_entity(input("Istifadəçı əlavə edəcəyiniz qrupun tagını yazın(link atmayın link atsaz id ve hashini yazdığınız hesab banlanacaq!!): "))
    num_users = int(input("Nə qədər istifadəçi çəkmək istəyirsiniz?: "))
    wait_time = int(input("Hər istifadəçi çəkdikdən sonra gözləmə vaxtı(sadəcə rəqəm yazın saniyə olaraq gedəcək!!): "))

    try:
        print("Hədəf qrupun istifadəçiləri yüklənir...")
        participants = await client.get_participants(source_group, filter=None)
    except ChatAdminRequiredError:
        print("Xəta: Hədəf qrupun istifadəçilərini görə bilmirsiniz lütfən istifadəçiləri açıq olan qrup seçin.")
        return

    non_admin_users = [
        user for user in participants
        if not isinstance(user.participant, (ChannelParticipantAdmin, ChannelParticipantCreator))
    ]

    added_count = 0

    for user in non_admin_users[:num_users]:
        try:
            print(f"İstifadəçi əlavə edilir: {user.id}")
            await client(InviteToChannelRequest(target_group, [user.id]))
            added_count += 1
            print(f"{added_count}. istifadəçi əlavə edildi. {wait_time} saniyə gözlənilir...")
            await asyncio.sleep(wait_time) 
        except PeerFloodError:
            print("Telegram limitinizi doldurdunuz. Bir az gözləyib yenidən yoxlayın.")
            break
        except Exception as e:
            print(f"istifadəçi əlavə edilərkən xəta: {e}")

    print(f"{added_count} istifadəçi qrupa əlavə edildi.")

with client:
    client.loop.run_until_complete(main())