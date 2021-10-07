import requests
from bs4 import BeautifulSoup
import lxml
import re


# !! Proxy Test !!
# test_url = 'https://httpbin.org/ip'
# !! This checks if request went from proxy !!
# test_r = requests.get(test_url, proxies=proxies)
# print(test_r.json())


url = 'https://free-proxy-list.net/'


def get_proxies(url):

    proxies = set()

    ip_pattern = re.compile(r'[0-9]+[.][0-9]+[.][0-9]+[.][0-9]+')
    port_pattern = re.compile(r'\B[0-9]{2,5}\B')

    headers = {
        # 'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36",
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept': 'image/webp,*/*',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Accept-CH': 'UA, Platform',
    }

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    # print(soup.prettify())

    tr = soup.select('.table.table-striped.table-bordered > tbody > tr')
    # print(tr)

    for td in tr:
        # print(td)

        ip_address = ip_pattern.findall(str(td))
        port_number = port_pattern.findall(str(td))
        proxy = ':'.join(ip_address+port_number)
        # print(proxy)
        proxies.add(proxy)

    return proxies


print(get_proxies(url))
