import requests
from bs4 import BeautifulSoup
import lxml
from product_info_allegro import get_article

proxies = {
    'http': 'http://62.213.14.166:8080',

}

url = 'https://allegro.pl/uzytkownik/skandynawskidom/wyposazenie-przybory-kuchenne-5328'

headers = {
    # 'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36",
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept': 'image/webp,*/*',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-CH': 'UA, Platform',
}

r = requests.get(url, headers=headers, proxies=proxies)
soup = BeautifulSoup(r.text, 'lxml')
# print(soup.prettify())

all_products = soup.find_all('article')
# print(all_products)

for product in all_products:
    # print(product)
    product_link = product.select_one('a')
    print(product_link.get('href'))
    print(get_article(product_link.get('href')))
