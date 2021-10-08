import requests
from bs4 import BeautifulSoup
import lxml
import re


# !! Proxy Test !!
# test_url = 'https://httpbin.org/ip'
# !! This checks if request went from proxy !!
# test_r = requests.get(test_url, proxies=proxies)
# print(test_r.json())


def get_proxies():

    url = 'https://free-proxy-list.net/'

    proxies = set()

    ip_pattern = re.compile(r'[0-9]+[.][0-9]+[.][0-9]+[.][0-9]+')
    port_pattern = re.compile(r'[<td>][0-9][0-9]+[</td>]')

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
        ip_address = ip_address[0]
        # print(type(ip_address))

        port_number = port_pattern.findall(str(td))
        port_number = port_number[0][1:-1]
        # print(type(port_number))

        proxy = ip_address + ':' + port_number
        proxy = 'http://' + proxy
        # print(proxy)
        proxies.add(proxy)

    return proxies
