from django.conf.urls import patterns, include, url
from project_ticket import views

urlpatterns = patterns('',
	url(r'^register$', views.register, name='register'),
	url(r'^home$', views.home, name='home'),
	url(r'^logout$', views.logout_view, name='logout'),
	url(r'profile$', views.profile, name='profile'),
	url(r'^project/(?P<project_id>\d+)/$', views.project_detail, name='project_detail'),
    url(r'^$', views.login_view, name='login'),
)