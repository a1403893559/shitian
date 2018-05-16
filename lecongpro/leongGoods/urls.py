from django.conf.urls import include, url
from leongGoods import views

urlpatterns = [
    url(r'index/',views.index),
    url(r'cart/',views.cart),
    url(r'detail/',views.detail),
    url(r'gengduo/(\d+)/$',views.gengduo),
    url(r'price/(\d+)/$',views.price)
]
