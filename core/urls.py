from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = patterns('',
     url(r'^$', Home.as_view(), name='home'),
     url(r'^user/', include('registration.backends.simple.urls')),
     url(r'^user/', include('django.contrib.auth.urls')),
     url(r'^business/create/$', login_required(BusinessCreateView.as_view()), name='business_create'),
     url(r'^business/$', login_required(BusinessListView.as_view()), name='business_list'),
     url(r'^business/(?P<pk>\d+)/$', login_required(BusinessDetailView.as_view()), name='business_detail'),
     url(r'^business/update/(?P<pk>\d+)/$', login_required(BusinessUpdateView.as_view()), name='business_update'),
     url(r'^business/delete/(?P<pk>\d+)/$', login_required(BusinessDeleteView.as_view()), name='business_delete'),
     url(r'^business/(?P<pk>\d+)/comment/create/$', login_required(CommentCreateView.as_view()), name='comment_create'),
     url(r'^business/(?P<business_pk>\d+)/comment/update/(?P<comment_pk>\d+)/$', login_required(CommentUpdateView.as_view()), name='comment_update'),
     url(r'^business/(?P<business_pk>\d+)/comment/delete/(?P<comment_pk>\d+)/$', login_required(CommentDeleteView.as_view()), name='comment_delete'),
)