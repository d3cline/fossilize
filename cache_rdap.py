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
    server_list = grab_inside()
    remove_list = list_rdap()
    fld_list = []

    for domain in server_list:
        try:  fld_list.append(get_tld(domain, as_object=True, fix_protocol=True).fld.encode().decode("idna"))
        except: print( {"error": f"{domain} failed tld lookup"} )

    for i in remove_list:
        try:
            fld_list.remove(i)
        except ValueError:
            pass

    tasks = []
    conn = aiohttp.TCPConnector(limit_per_host=10)
    async with aiohttp.ClientSession(connector=conn) as session:
        for domain in fld_list:
            tasks.append(fetch(session, f'https://www.rdap.net/domain/{domain}'))

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