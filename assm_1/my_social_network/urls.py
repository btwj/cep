from django.conf.urls import patterns, include, url
from my_social_network import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'assm_1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^users/$', views.index, name='index'),
    url(r'(?P<username>[\w_-]+)/followers$', views.followers, name='followers'),
    url(r'(?P<username>[\w_-]+)/following$', views.following, name='following')
)
