from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import staticfiles
from django.conf.urls import url

from zzh import views

urlpatterns = [
    url(r'^index/',views.index),
    url(r'^index1/',views.index1),
    url(r'^dl',views.dl),
    url(r'^zhuce',views.zhuce),
    url(r'^wangye',views.wangye),
    url(r'article/(?P<article_id>[0-9]+)/$',views.article_page,name='article'),
    url(r'^fabiao/',views.fabiao),
    url(r'^xin',views.xin),
    url(r'update',views.update),
    url(r'xiu',views.xiu),
    url(r'^wang$',views.wang),
    url(r'wangji',views.wangji),
    url(r'pddn',views.pddn),
    url(r'^wjgmm',views.wjgmm),
    url(r'^search',views.search),
    url(r'^shanchu',views.shanchu),
    url(r'delete',views.delete)


]
urlpatterns += staticfiles_urlpatterns()

