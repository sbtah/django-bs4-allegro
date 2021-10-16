import requests
from misioo_product import get_misioo_product
from bs4 import BeautifulSoup
import lxml


url_misio_category = 'https://misioohandmade.pl/mata-dla-dzieci-velvet/'


headers = {
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36",
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept': 'image/webp,*/*',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-CH': 'UA, Platform',
}

r = requests.get(url_misio_category, headers=headers)
soup = BeautifulSoup(r.text, 'lxml')
# print(soup.prettify())
all_arts = soup.find_all(
    'a', "button button--secondary button--md woocommerce-LoopProduct-link woocommerce-loop-product__link")

# print(all_arts)  # Lista

for art in all_arts:
    print(get_misioo_product(art['href']))
    print("------------------------------------------------------------------")
    print("------------------------------------------------------------------")
