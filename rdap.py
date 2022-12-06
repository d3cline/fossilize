import requests
import json 
from tld import get_tld
from grab import grab_outside

def rdap(url):
  pass

grabbed = grab_outside()
for instance in grabbed:
  domain = instance['domain']
  try: res = get_tld(domain, as_object=True, fix_protocol=True)
  except: res = None
  if res:
    res.subdomain
    # 'some.subdomain'
    res.domain
    # 'google'
    res.tld
    # 'co.uk'
    res.fld
    # 'google.co.uk'
    
    api_endpoint = f'https://www.rdap.net/domain/{res.fld}'
    print(f'{api_endpoint}domain/{res.fld}')

    """
    rdap_info = rdap(res.fld)
    f = open(f'rdaps/{res.fld}.json', "w")
    f.write(json.dumps(rdap_info))
    f.close()
    print(f"ADDED {instance['domain']}")
    """

  else:
    print(f"FAILED {instance['domain']}")