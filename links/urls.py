from django.urls import path

from links.views import home_view, product_list

app_name = 'links'

urlpatterns = [
    path('', home_view, name='home'),
    path('products/', product_list, name='product-list'),
]
