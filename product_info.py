import requests
from bs4 import BeautifulSoup
import lxml

url = "https://allegro.pl/oferta/turystyczny-namiot-2-osobowy-190x130-wojskowy-moro-10801343832"


def get_article(url):

    headers = {
        # 'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36",
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept': 'image/webp,*/*',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Accept-CH': 'UA, Platform',
    }

    # Read url and prepare soup file.
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')

    # Get Article Name.
    name = soup.select_one('h1').getText()

    # Get Article Price.
    price = soup.select_one('._1svub._lf05o.mpof_vs.munh_8.mp4t_4').getText()
    price = price.replace(',', '.')[:-3]
    if ' ' in price:
        price = float(price.replace(' ', ''))

    # Get Article statistics : number of customers and number of sales.
    if soup.select_one('._1h7wt.mgn2_13._1vryf._1t7v4') is not None:
        sold_recently = soup.select_one(
            '._1h7wt.mgn2_13._1vryf._1t7v4').getText()
        recent_sales = sold_recently.split()[3]
        recent_customers = sold_recently.split()[0]
    else:
        recent_sales = None
        recent_customers = None

    # Get seller name and seller's percentage of positive reviews.
    seller_data = soup.select_one('a._w7z6o._15mod._7030e_3tKtu').getText()
    seller_data = seller_data.split('-')
    seller_reviews = float(seller_data[1][1:-1].replace(',', '.'))
    seller_name = seller_data[0]

    return name, float(price), seller_name, int(recent_sales), int(recent_customers), seller_reviews


print(get_article(url))
