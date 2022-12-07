import aiohttp
import asyncio
from grab import grab_inside
from tld import get_tld
from storage import put_object
import json 

async def fetch(session, url):
    try:
        async with session.get(url) as response:
            print(url)
            return await response.json()
    except:
        return None

async def main():
    urls = grab_inside()
    tasks = []
    async with aiohttp.ClientSession() as session:
        for url in urls:
            try: res = get_tld(url, as_object=True, fix_protocol=True)
            except: res = None
            if res: tasks.append(fetch(session, f'https://www.rdap.net/domain/{res.fld}'))
        bodies = await asyncio.gather(*tasks)
        for body in bodies:
            if body and "ldhName" in body.keys():
                put_object(f'rdap/{body["ldhName"].lower()}', json.dumps(body))
            else:
                print(body)

if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
