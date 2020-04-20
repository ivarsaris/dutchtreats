from django.conf.urls import url

from .views import all_products, delete_review, new_review, product_detail

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^(?P<pk>\d+)/$', product_detail, name='product'),
    url(r'^(?P<pk>\d+)/detail/review', new_review, name='new_review'),
    url(r'^(?P<pk>\d+)/deleteReview/', delete_review, name='delete_review'),
]
