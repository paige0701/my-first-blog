from django.conf.urls import url
from django.urls import reverse_lazy

from . import views
from django.contrib.auth.views import login as login
from django.contrib.auth.views import logout as logout

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),

    url(r'^category/(?P<category>\d+)/$', views.post_list_with_category, name='post_list_with_category'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),

    url(r'^login/$',login, {'template_name':"auth/login.html"}, name='blog_login'),
    url(r'^logout/$', logout, {'next_page': reverse_lazy('post_list')}, name='blog_logout'),

    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),




]