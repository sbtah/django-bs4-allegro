import requests
from bs4 import BeautifulSoup
import lxml


url_product_1 = "https://minibe.eu/pl/baseny-minibe-basic/13-basen-suchy-150-szt-pileczek-rozne-kolory.html"


def get_minibe_product(url_product_1):

    headers = {
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
        'Accept-Language': 'pl',
    }

    r_product = requests.get(url_product_1, headers=headers)
    soup_product = BeautifulSoup(r_product.text, 'lxml')

    name = soup_product.select_one(selector="h1").getText()  # Works!
    price = soup_product.select_one(
        selector='#our_price_display').getText()  # Works!

    price = float(price[:-3].replace(',', '.'))

    main_picture = soup_product.select_one(selector='#bigpic')  # Works!
    main_picture = main_picture['src']

    product_description = soup_product.select(
        selector='.rte')
    product_description = product_description[1].getText()
    # print(name)
    # print(float(price))
    # print(main_picture['src'])
    # print(product_description[1].getText())

    return name, price, main_picture, product_description


print(get_minibe_product(url_product_1))
