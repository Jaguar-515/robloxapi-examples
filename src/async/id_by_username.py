#async version
import robloxapi, asyncio

client = robloxapi.client()

async def run():
    id = await client.User.id_by_username('roblox')
    print(id)

loop = asyncio.get_event_loop()
loop.run_until_complete(run())
loop.close()
