import aiohttp
import asyncio
from grab import grab_inside

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    urls = grab_inside()
    tasks = []
    async with aiohttp.ClientSession() as session:
        for url in urls:
            tasks.append(fetch(session, f'https://{url}'))
        htmls = await asyncio.gather(*tasks)
        for html in htmls:
            print(html[:100])

if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
