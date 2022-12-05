from grab import grab_outside
from rdap import rdap
from tld import get_tld
from pprint import pprint

grabbed = grab_outside()
for instance in grabbed:
  res = get_tld(instance['domain'], as_object=True, fix_protocol=True)
  res.subdomain
  # 'some.subdomain'
  res.domain
  # 'google'
  res.tld
  # 'co.uk'
  res.fld
  # 'google.co.uk'
  rdap_info = rdap(res.fld)
  print(res.fld)
  pprint(rdap_info)
