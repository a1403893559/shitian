from django.conf.urls import include, url
from leongGoods import views

urlpatterns = [
    url(r'index/',views.index),
    url(r'cart/',views.cart),
    url(r'detail/',views.detail),
    url(r'gengduo/(\d+)/(\d+)/$',views.gengduo),
    url(r'price/(\d+)/$',views.price),
    url(r'moren/(\d+)/$',views.moren),
    url(r'detail/?a=(\d+)/$',views.detail),
    url(r'jisuan/d=(\d+)/$',views.jisuan),
    url(r'jiaru/f=(\d+)/$',views.jiaru),
    url(r'zhanshi/$',views.zhanshi),
    url(r'chuli/$',views.chuli),
    url(r'tiaoyong/$',views.tiaoyong),
    url(r'gwjs/$',views.gwjs),
    url('dizhi/$',views.dizhi),
    url(r'xiudi/$',views.xiudi),
    url(r'tijiao/$',views.tijiao),
    url(r'dingdan/$',views.dingdan),

]
