import requests
from bs4 import BeautifulSoup
import lxml

# url = "https://allegro.pl/oferta/krajalnica-szatkownica-warzyw-tarka-czosnku-cebuli-9569830082"


def get_article(url):

    headers = {
        # 'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36",
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept': 'image/webp,*/*',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Accept-CH': 'UA, Platform',
    }

    # Reads url and prepare soup file. !! ADD url valiadtion/cleaning mechanism for urls with not needed arguments !!.
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')

    # Get Article's Name. !! FIND EDGE CASE OF CRASH : https://allegro.pl/oferta/krajalnica-szatkownica-warzyw-tarka-czosnku-cebuli-9569830082 !!
    if soup.select_one('h1').getText() is not None:
        name = soup.select_one('h1')  # .getText()
    else:
        name = None

    # Get Article's Price.
    if soup.select_one('._1svub._lf05o.mpof_vs.munh_8.mp4t_4').getText() is not None:
        price = soup.select_one(
            '._1svub._lf05o.mpof_vs.munh_8.mp4t_4').getText()
        price = price.replace(',', '.')[:-3]
        if ' ' in price:
            price = float(price.replace(' ', ''))
    else:
        price = None

    # Get Article's statistics : number of customers and number of sales.
    if soup.select_one('._1h7wt.mgn2_13._1vryf._1t7v4') is not None:
        sold_recently = soup.select_one(
            '._1h7wt.mgn2_13._1vryf._1t7v4').getText()
        recent_sales = sold_recently.split()[3]
        recent_customers = sold_recently.split()[0]
    else:
        recent_sales = None
        recent_customers = None

    # Get seller's name and seller's percentage of positive reviews.
    if soup.select_one('a._w7z6o._15mod._7030e_3tKtu').getText() is not None:
        seller_data = soup.select_one('a._w7z6o._15mod._7030e_3tKtu').getText()
        seller_data = seller_data.split('-')
        seller_reviews = float(seller_data[1][1:-1].replace(',', '.'))
        seller_name = seller_data[0]
    else:
        seller_reviews = None
        seller_name = None

    return name, float(price), seller_name, int(recent_sales), int(recent_customers), seller_reviews
