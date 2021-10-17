from django.urls import path

from links.views import home_view, product_list, product_detail, product_delete

app_name = 'links'

urlpatterns = [
    path('', home_view, name='home'),
    path('products/', product_list, name='product-list'),
    path('products/<int:pk>', product_detail, name='product-detail'),
    path('delete/<int:pk>', product_delete, name='product-delete'),
]
