import aiohttp
import asyncio
import time


async def main():
    headers = {'Cache-Control': 'no-cache', 'Connection': 'keep-alive'}
    for i in range(200):
        time.sleep(1)
        async with aiohttp.request('GET','http://8.131.82.49:82/admin/uploads/20201219_6081563259568567892.jpg',
                                    headers=headers) as response:
            print("Status:", response.status)
            print("Content-type:", response.headers)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
