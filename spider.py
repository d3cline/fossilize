import requests 

# What you want to search, lower case
SEARCH_TERM = "anthropology"
# Your home instance URL
INSTANCE_URL="https://opalstack.social"
# Number of accounts to search before stop
MAX_OFFSET = 10000

def grab_instance_domains():
  return requests.get(url=f'{INSTANCE_URL}/api/v1/instance/peers').json()

def spider(domains):
  for domain in domains:
    CURRENT_OFFSET = 0
    while CURRENT_OFFSET < MAX_OFFSET:
      try: r = requests.get(url=f'https://{domain}/api/v1/directory?offset={CURRENT_OFFSET}').json()
      except Exception as ex: 
        print(f'domain {domain} faild {ex}')
        break
      for account in r:
        try: 
          if SEARCH_TERM in account['note'].lower(): print(account['acct'])
        except Exception as ex: 
          print(f'domain {domain} faild {ex} account: {account}')
          break
      CURRENT_OFFSET += 40

def main():
  print(f'SEARCHING FOR {SEARCH_TERM}')
  domains = grab_instance_domains()
  spider(domains)

if __name__ == "__main__":
  main()
