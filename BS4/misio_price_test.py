import requests
from bs4 import BeautifulSoup
import lxml

url_product_1 = "https://misioohandmade.pl/sklep/basenik-z-pilkami-velvet/?attribute_pa_kolor=liliowy&attribute_pa_ksztalt=okragly"

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
# print(soup_product.prettify())

# This get price and works - but ignores ::before in css?!
# price = soup_product.select_one(selector=".price").getText()
# price = float(price[9:-3].replace(',', '.'))
# print(price)
# === #

# This doesn't !
prices = soup_product.find_all('input')
for price in prices:
    if price.get('name') == 'gtm4wp_name':
        article_name = price.get('value')
    elif price.get('name') == 'gtm4wp_id':
        article_id = price.get('value')
    elif price.get('name') == 'gtm4wp_sku':
        article_sku = price.get('value')
    elif price.get('name') == 'gtm4wp_price':
        article_price = price.get('value')


print(article_price)
# product-6003 > div > div.single-product__summary > form > div.single_variation_wrap > div.woocommerce-variation.single_variation > div.woocommerce-variation-price > span > ins > span


# print(soup.select_one('.price-current-label').find_next_sibling(text=True))
#product-6003 > div > div.single-product__summary > form > div.single_variation_wrap > div.woocommerce-variation-add-to-cart.variations_button.woocommerce-variation-add-to-cart-enabled > button

#product-6003 > div > div.single-product__summary > form > div.single_variation_wrap > div.woocommerce-variation-add-to-cart.variations_button.woocommerce-variation-add-to-cart-enabled

#product-6003 > div > div.single-product__summary > form > div.single_variation_wrap > div.woocommerce-variation-add-to-cart.variations_button.woocommerce-variation-add-to-cart-enabled > button
