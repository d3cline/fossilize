import asyncio
import httpx 

# Your home instance URL
INSTANCE_URL="https://opalstack.social"

TOTAL_CANT = 0
TOTAL_CAN = 0

def grab_instance_domains():
  return httpx.get(url=f'{INSTANCE_URL}/api/v1/instance/peers').json()

async def grap_instance_info(domains):
  infos = []
  errors = []
  i=1
  total = len(domains)
  for domain in domains:
    print(i, 'of', total)
    i+=1
    async with httpx.AsyncClient() as client:
      try:
        r = await client.get(f'https://{domain}/api/v2/instance', timeout=0.5)
        infos.append(r.json())
      except Exception as ex:
        errors.append(domain)
  return (infos, errors)
    

async def main():
  domains = grab_instance_domains()
  print("number of domains", len(domains))
  infos, errors = await grap_instance_info(domains)
  print(infos, errors)

if __name__ == '__main__':
  loop = asyncio.new_event_loop()
  asyncio.set_event_loop(loop)
  try:
    asyncio.run(main())
  except KeyboardInterrupt:
    pass


