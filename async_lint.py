import httpx

# Your home instance URL
INSTANCE_URL="https://opalstack.social"

TOTAL_CANT = 0
TOTAL_CAN = 0

def grab_instance_domains():
  return httpx.get(url=f'{INSTANCE_URL}/api/v1/instance/peers').json()


def main():
    domains = grab_instance_domains()
    print(domains)


if __name__ == '__main__':
    main()

