from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
     url(r'^$', Home.as_view(), name='home'),
     url(r'^user/', include('registration.backends.simple.urls')),
     url(r'^user/', include('django.contrib.auth.urls')),
     url(r'^business/create/$', BusinessCreateView.as_view(), name='business_create'),
     url(r'^business/$', BusinessListView.as_view(), name='business_list'),
)