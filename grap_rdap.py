from grab import grab_outside
from rdap import rdap
from tld import get_tld
from pprint import pprint
import json

grabbed = grab_outside()
for instance in grabbed:
  res = get_tld(instance['domain'], as_object=True, fix_protocol=True)
  if res:
    res.subdomain
    # 'some.subdomain'
    res.domain
    # 'google'
    res.tld
    # 'co.uk'
    res.fld
    # 'google.co.uk'
    rdap_info = rdap(res.fld)
    f = open(f'rdaps/{res.fld}.json', "w")
    f.write(json.dumps(rdap_info))
    f.close()
    print(f"ADDED {instance['domain']}")
  else:
    print(f"FAILED {instance['domain']}")