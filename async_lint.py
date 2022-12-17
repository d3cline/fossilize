import aiohttp
import asyncio
import json
import requests 

# Your home instance URL
INSTANCE_URL="https://opalstack.social"

TOTAL_CANT = 0
TOTAL_CAN = 0


def grab_instance_domains():
  return requests.get(url=f'{INSTANCE_URL}/api/v1/instance/peers').json()

async def mastodon_info(session, domain):
    try:
        async with session.get(f'https://{domain}/api/v2/instance') as response:
            print(domain, 'info')
            response = await response.json(content_type=None)
            if 'domain' in response: 
                if domain == response['domain']:
                    return  {'body': response, 'domain': domain, 'is_mastodon': True}
                else:
                    return  {'body': response, 'domain': domain, 'is_mastodon': False}
            else:
                return  {'body': response, 'domain': domain, 'is_mastodon': False}
    except Exception as ex:
        return {'body': ex, 'domain': domain, 'is_mastodon': False}

async def fetch(session, domain):
    try:
        async with session.get(f'https://{domain}/api/v1/instance/peers') as response:
            print(domain, 'fetch')
            response = await response.json(content_type=None)
            return  {'body': response, 'domain': domain}
    except Exception as ex:
        return {'body': ex, 'domain': domain}

async def main():
    domains = grab_instance_domains()
    tasks_remote_peers = []
    tasks_info = []
    async with aiohttp.ClientSession(
        connector=aiohttp.TCPConnector(), 
        timeout=aiohttp.ClientTimeout(
            total=None, 
            connect=None, 
            sock_connect=5, 
            sock_read=5
            )
        ) as session:
        for domain in domains:
            tasks_info.append(mastodon_info(session, domain))
        remote_infos = await asyncio.gather(*tasks_info)


    async with aiohttp.ClientSession(
        connector=aiohttp.TCPConnector(), 
        timeout=aiohttp.ClientTimeout(
            total=None, 
            connect=None, 
            sock_connect=5, 
            sock_read=5
            )
        ) as session:
        for info in remote_infos:
            if 'is_mastodon' in info and info['is_mastodon'] == True :
                tasks_remote_peers.append(fetch(session, info["domain"]))
            else:
                print(info)
        remote_peers = await asyncio.gather(*tasks_remote_peers)
    
    print(remote_peers, remote_infos)
        #for remote_peer in remote_peers:
        #    if 'opalstack.social' in remote_peer['body']:
        #        print(f"✅ is present on {remote_peer['domain']} Users: {i['usage']['users']['active_month']}")
        #    else:
        #        print(f"❌ is not present on {remote_peer['domain']} Users: {i['usage']['users']['active_month']}")


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass


