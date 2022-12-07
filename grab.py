import requests
from settings import PODUP_API_URL, INSTANCE_URL

podurl = PODUP_API_URL
body = """
query{
  nodes{
    domain
    masterversion
    shortversion
    softwarename
    daysmonitored
    monthsmonitored
    date_updated
    date_laststats
    date_created
  }
}
"""
def grab_outside():
  return requests.post(url=podurl, json={"query": body}).json()['data']['nodes']

def grab_inside():
  return requests.get(url=f'{INSTANCE_URL}api/v1/instance/peers').json()
