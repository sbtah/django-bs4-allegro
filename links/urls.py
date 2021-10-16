from django.urls import path

from links.views import home_view, product_list, product_delete

app_name = 'links'

urlpatterns = [
    path('', home_view, name='home'),
    path('products/', product_list, name='product-list'),
    path('delete/<int:pk>', product_delete, name='product-delete'),
]
