from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
     url(r'^$', Home.as_view(), name='home'),
     url(r'^user/', include('registration.backends.simple.urls')),
     url(r'^user/', include('django.contrib.auth.urls')),
     url(r'^business/create/$', BusinessCreateView.as_view(), name='business_create'),
     url(r'^business/$', BusinessListView.as_view(), name='business_list'),
     url(r'^business/(?P<pk>\d+)/$', BusinessDetailView.as_view(), name='business_detail'),
     url(r'^business/update/(?P<pk>\d+)/$', BusinessUpdateView.as_view(), name='business_update'),
     url(r'^business/delete/(?P<pk>\d+)/$', BusinessDeleteView.as_view(), name='business_delete'),
     url(r'^business/(?P<pk>\d+)/comment/create/$', CommentCreateView.as_view(), name='comment_create'),
     url(r'^business/(?P<business_pk>\d+)/comment/update/(?P<comment_pk>\d+)/$', CommentUpdateView.as_view(), name='comment_update'),
     url(r'^business/(?P<business_pk>\d+)/comment/delete/(?P<comment_pk>\d+)/$', CommentDeleteView.as_view(), name='comment_delete'),
)