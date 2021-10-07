import requests
from itertools import cycle
import traceback
from get_proxy_list import get_proxies


# !!! THIS IS FOR RESPONSE TEST !!!
# proxies = {
#     'http': 'http://207.244.227.169:443',
#     'https': 'http://207.244.227.169:443',
# }
# # !! Proxy Test !!
# test_url = 'https://httpbin.org/ip'
# # !! This checks if request went from proxy !!
# test_r = requests.get(test_url, proxies=proxies)
# print(test_r.json())


proxies = get_proxies()
proxy_pool = cycle(proxies)
url = 'https://httpbin.org/ip'

for i in range(10, 20):
    proxy = next(proxy_pool)
    print("Request #%d" % i)

    try:
        response = requests.get(url, proxies={"http": proxy, "https": proxy})
        print(response.json())
    except:
        # Most free proxies will often get connection errors. You will have retry the entire request using another proxy to work.
        # We will just skip retries as its beyond the scope of this tutorial and we are only downloading a single url
        print("Skipping. Connnection error")
