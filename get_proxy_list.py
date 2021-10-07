import requests
from bs4 import BeautifulSoup
import lxml
from requests.api import head
import re

# !! Proxy Test !!
# test_url = 'https://httpbin.org/ip'


# Normal Function.
url = 'https://free-proxy-list.net/'


proxies = proxies = {
    "http": 'http://78.92.231.44:55443',
    "https": 'http://78.92.231.44:55443',
    "http": 'http://54.93.108.168:9300',
    "https": 'http://54.93.108.168:9300',
}


headers = {
    # 'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36",
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept': 'image/webp,*/*',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-CH': 'UA, Platform',
}

# !! This checks if request went from proxy !!
# test_r = requests.get(test_url, proxies=proxies)
# print(test_r.json())

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, 'lxml')
# print(soup.prettify())

tr = soup.select('tbody > tr > td')
# print(tr)
for td in tr:
    print(td)
