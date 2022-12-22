import asyncio
import httpx 

# Your home instance URL
INSTANCE_URL="https://opalstack.social"

TOTAL_CANT = 0
TOTAL_CAN = 0


def grab_instance_domains():
  return httpx.get(url=f'{INSTANCE_URL}/api/v1/instance/peers').json()

async def grap_instance_info(domains):
    for domain in domains:
      print(domain)
      async with httpx.AsyncClient() as client:
        try:
          r = await client.get(f'https://{domain}/api/v2/instance', timeout=0.5)
        except Exception as ex:
          print(ex)
    

async def main():
  domains = grab_instance_domains()
  infos = await grap_instance_info(domains)
  print(infos)

if __name__ == '__main__':
  loop = asyncio.new_event_loop()
  asyncio.set_event_loop(loop)
  try:
    asyncio.run(main())
  except KeyboardInterrupt:
    pass


