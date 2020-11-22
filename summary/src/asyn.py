import asyncio
import aiohttp
import time
from config import *

async def get_url():
    async with aiohttp.request("GET",URL) as r:
        pass

print(time.time())
tasks = []
for i in range(NUM):
    tasks.append(get_url())
event_loop = asyncio.get_event_loop()
results = event_loop.run_until_complete(asyncio.gather(*tasks))
print(time.time())