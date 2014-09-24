from django.conf.urls import patterns, include, url
from user_auth import views

urlpatterns = patterns('',
	url(r'^home$', views.home, name='home'),
	url(r'^logout$', views.logout_view, name='logout'),
	url(r'profile$', views.profile, name='profile'),
    url(r'^$', views.login_view, name='login'),
)