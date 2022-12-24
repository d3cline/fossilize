import asyncio
import httpx 

# Your home instance URL
INSTANCE_URL="https://opalstack.social"
TOTAL_CANT = 0
TOTAL_CAN = 0

def grab_instance_domains():
  return httpx.get(url=f'{INSTANCE_URL}/api/v1/instance/peers').json()

async def grab_instance_info(domains):
  infos = []
  errors = []
  i=1
  total = len(domains)
  for domain in domains:
    print(i, 'of', total)
    i+=1
    async with httpx.AsyncClient() as client:
      try:
        r = await client.get(f'https://{domain}/api/v2/instance', timeout=1)
        infos.append(r.json())
      except Exception as ex:
        errors.append(domain)
  return (infos, errors)

async def grab_instance_peers(domains):
  global TOTAL_CANT 
  global TOTAL_CAN
  for domain, v in domains.items():
    users = v['users']
    async with httpx.AsyncClient() as client:
      try:
        r = await client.get(f'https://{domain}/api/v1/instance/peers', timeout=1)
        if 'opalstack.social' in r.json():
          print(f"✅ is present on {domain} Users: {users}")
          TOTAL_CAN+=users
        else:
          print(f"❌ is not present on {domain} Users: {users}")
          TOTAL_CANT+=users
      except Exception as ex:
        print(domain, r, ex)

def filter_mastodon_domains(infos):
  mastodon_domains = {}
  for info in infos:
    try:
      mastodon_domains[info['domain']] = {'users':info['usage']['users']['active_month']}
    except Exception as ex:
      print(ex, info)
      continue
  return mastodon_domains

async def main():
  domains = grab_instance_domains()
  print("number of domains", len(domains))
  infos, errors = await grab_instance_info(domains)
  mastodon_domains = filter_mastodon_domains(infos)
  lint = await grab_instance_peers(mastodon_domains)
  print(TOTAL_CAN, TOTAL_CANT)
  print(errors)

if __name__ == '__main__':
  loop = asyncio.new_event_loop()
  asyncio.set_event_loop(loop)
  try:
    asyncio.run(main())
  except KeyboardInterrupt:
    pass


