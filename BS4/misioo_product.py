import requests
from bs4 import BeautifulSoup
import lxml

# https://misioohandmade.pl/sklep/page/2/
url_product_1 = "https://misioohandmade.pl/sklep/basenik-z-pilkami-velvet"


def get_misioo_product(url_product_1):

    headers = {
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36",
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept': 'image/webp,*/*',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Accept-CH': 'UA, Platform',
    }

    r_product = requests.get(url_product_1, headers=headers)
    soup_product = BeautifulSoup(r_product.text, 'lxml')

    name = soup_product.select_one(selector="h1").getText()  # Works!

    # This doesn't pull proper value.
    price = soup_product.select_one(selector=".price").getText()
    # This is ok.
    price = float(price[9:-3].replace(',', '.'))

    main_picture = soup_product.select_one(
        selector='.wp-post-image')  # Works!
    main_picture = main_picture['src']

    product_description = soup_product.select_one(
        selector='.product-tabs__half').getText()

    # print(name)
    # print(price)
    # print(main_picture)
    # print(product_description)

    return name, price, main_picture, product_description


print(get_misioo_product(url_product_1)[3])
