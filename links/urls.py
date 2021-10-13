from django.urls import path

from links.views import home_view

app_name = 'links'

urlpatterns = [
    path('', home_view, name='home'),
]
