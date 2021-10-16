import requests
from bs4 import BeautifulSoup
import lxml

# # https://misioohandmade.pl/sklep/page/2/
# url_product_1 = "https://misioohandmade.pl/sklep/misioo-bluza-rozpinana-z-kapturem/?attribute_pa_kolekcja=forest-leaves&attribute_pa_rozmiar=128-134"


def get_misioo_product(url_product_1):

    headers = {
        # 'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36",
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept': 'image/webp,*/*',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Accept-CH': 'UA, Platform',
    }

    r_product = requests.get(url_product_1, headers=headers)
    soup_product = BeautifulSoup(r_product.text, 'lxml')

    # Pulls from form : Name, ID, SKU, Price....
    form_info = soup_product.find_all('input')
    for price in form_info:
        if price.get('name') == 'gtm4wp_name':
            article_name = price.get('value')
        elif price.get('name') == 'gtm4wp_id':
            article_id = price.get('value')
        elif price.get('name') == 'gtm4wp_sku':
            article_sku = price.get('value')
        elif price.get('name') == 'gtm4wp_price':
            article_price = price.get('value')

    # This gets main picture.
    main_picture = soup_product.select_one(
        selector='.wp-post-image')  # Works!
    main_picture = main_picture['src']

    # This gets description.
    product_description = soup_product.select_one(
        selector='.product-tabs__half').getText()

    return article_name, article_id, article_sku, float(article_price), main_picture, product_description


# print(get_misioo_product(url_product_1))
