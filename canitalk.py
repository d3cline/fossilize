import httpx

# Your home instance URL
INSTANCE_URL="https://opalstack.social"

TOTAL_CANT = 0
TOTAL_CAN = 0

def grab_instance_domains():
  return httpx.get(url=f'{INSTANCE_URL}/api/v1/instance/peers').json()

def spider(domains):
  for domain in domains:
    try: r = httpx.get(url=f'https://{domain}/api/v1/instance/peers', timeout=3).json()
    except Exception as ex: 
      #print(f'domain {domain} faild request lookup {ex}')
      pass

    try: 
      i = httpx.get(url=f'https://{domain}/api/v2/instance', timeout=3).json()
    except Exception as ex: 
      #print(f'domain {domain} faild request lookup {ex}')
      pass

    try:
      if 'opalstack.social' in r:
        print(f"✅ is present on {domain} Users: {}")
        TOTAL_CAN = TOTAL_CAN + i['usage']['users']['active_month']
      else:
        print(f"❌ is not present on {domain} Users: {i['usage']['users']['active_month']}")
        TOTAL_CANT = TOTAL_CANT + i['usage']['users']['active_month']
    except Exception as ex:
      #print(f'{domain} {ex}')
      pass

def main():
  domains = grab_instance_domains()
  spider(domains)
  print(f'TOTALS: CAN:{TOTAL_CAN} CANT:{TOTAL_CANT}')

if __name__ == "__main__":
  main()