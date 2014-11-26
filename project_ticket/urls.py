from django.conf.urls import patterns, include, url
from project_ticket import views

urlpatterns = patterns('',
	url(r'^home$', views.home, name='home'),
	url(r'^logout$', views.logout_view, name='logout'),
	url(r'^project/(?P<project_id>\d+)/$', views.project, name="project"),
	url(r'^profile$', views.profile, name='profile'),
	url(r'^editprofile$', views.editprofile, name='editprofile'),
	url(r'^addticket$', views.addticket, name='addticket'),
	url(r'^register$', views.register, name='register'),
    url(r'^$', views.login_view, name='login'),
   )