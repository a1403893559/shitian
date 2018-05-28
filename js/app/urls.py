from django.conf.urls import include, url
from app import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = {
    url(r'^register/$', views.register, name='register'),
    url(r'register_handle/$', views.register_handle),
    url(r'login/', views.login),
    url(r'dengl/', views.dengl),
    url(r'xieliu/', views.xieliu),
    url(r'zhanshi/', views.zhanshi),
    url(r'tiao/', views.tiao),

}