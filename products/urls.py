from django.conf.urls import url, include
from .views import all_products, single_product


urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^product$', single_product, name='product')
]