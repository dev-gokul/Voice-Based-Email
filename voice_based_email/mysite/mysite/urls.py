from django.contrib import admin
#from django.conf.urls import url, include
from django.urls import include,re_path as url

urlpatterns = [
    url(r'^admin/$', admin.site.urls),
    url(r'^',include('homepage.urls')),
    
]
