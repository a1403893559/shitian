from django.conf.urls import include, url
from userapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
   url(r'^register/$',views.register,name='register'),
   url(r'register_handle/$',views.register_handle),
   url(r'tiao/$',views.tiao),
   url(r'chuan/$',views.chuan),
   url(r'kan/$',views.kan),
   url(r'login/$',views.login),
   url(r'dengl/',views.dengl)

]
