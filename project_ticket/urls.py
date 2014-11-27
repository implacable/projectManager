from django.conf.urls import patterns, include, url
from project_ticket import views

urlpatterns = patterns('',
	url(r'^home$', views.home, name='home'),
	url(r'^logout$', views.logout_view, name='logout'),
	url(r'^project/(?P<project_id>\d+)/$', views.project, name="project"),
	url(r'^ticket/(?P<ticket_id>\d+)/$', views.ticket_detail, name="ticket_detail"),
	url(r'^change_status/(?P<ticket_id>\d+)/$', views.change_ticket_status, name="change_status"),
	url(r'^profile$', views.profile, name='profile'),
	url(r'^editprofile$', views.editprofile, name='editprofile'),
	url(r'^addticket$', views.addticket, name='addticket'),
	url(r'^register$', views.register, name='register'),
    url(r'^$', views.login_view, name='login'),
   )