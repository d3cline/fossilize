import requests
import json 
from tld import get_tld
from grab import grab_outside

def get_tld_map():
  rdap_api_endpoints = requests.get(url='https://data.iana.org/rdap/dns.json').json()['services']
  print("TLD API MAP OBTAINED")
  return rdap_api_endpoints

TLD_API_MAP = get_tld_map()

def find_api_endpoint(tld):
  for x in TLD_API_MAP:
    if tld in x[0]: return x[1][0]
    elif tld == 'de': return 'https://rdap.denic.de/'

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

    api_endpoint = find_api_endpoint(res.tld.encode('idna').decode())
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