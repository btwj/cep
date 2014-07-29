from django.conf.urls import patterns, url, include
import views

urlpatterns = patterns('',
                       url(r'^list/$', views.notes_list, name='notes_list'),
                       url(r'^detail/(?P<id>\d+)/$', views.notes_detail, name='notes_detail')
)