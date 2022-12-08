import aiohttp
import asyncio
from grab import grab_inside
from tld import get_tld
from storage import put_object, list_rdap
import json

async def fetch(session, url):
    try:
        async with session.get(url) as response:
            print(url)
            return await response.json(content_type=None)
    except Exception as ex:
        return {"error": f"{url} failed rdap lookup", "exception": str(ex)}

async def main():
    cached_rdaps = []
    for obj in list_rdap():
        cached_rdaps.append(obj.object_name.split('/')[1])
    urls = grab_inside()
    print(len(urls))

    for i in cached_rdaps:
        try:
            urls.remove(i)
        except ValueError:
            pass

    print(len(urls))
    tasks = []
    conn = aiohttp.TCPConnector(limit_per_host=10)
    async with aiohttp.ClientSession(connector=conn) as session:
        for url in urls:
            try: res = get_tld(url, as_object=True, fix_protocol=True)
            except: res = {"error": f"{url} failed tld lookup"}
            if isinstance(res, dict): print(url)
            else: tasks.append(fetch(session, f'https://www.rdap.net/domain/{res.fld.encode().decode("idna")}'))
        bodies = await asyncio.gather(*tasks)
        for body in bodies:
            if body and "ldhName" in body.keys():
                put_object(f'rdap/{body["ldhName"].encode("idna").decode().lower()}', json.dumps(body))
            else:
                print(body)

if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass