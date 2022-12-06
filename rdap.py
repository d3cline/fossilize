import requests
import json 
from tld import get_tld
from grab import grab_outside
from pprint import pprint

grabbed = grab_outside()
for instance in grabbed:
  domain = instance['domain']
  try: res = get_tld(domain, as_object=True, fix_protocol=True)
  except: res = None
  if res:
    api_endpoint = f'https://www.rdap.net/domain/{res.fld}'
    try: rdap = requests.get(url=api_endpoint, timeout=3)
    except: print(f"TIMEOUT {domain}")
    if rdap.status_code == 200: 
      f = open(f'rdaps/{res.fld}.json', "w")
      f.write(json.dumps(rdap.json()))
      f.close()
      print(f"ADDED {domain}")
  else:
    print(f"FAILED {domain}")
