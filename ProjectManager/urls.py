from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
	url(r'^$', 'user_auth.views.home', name="home"),
    url(r'^user/', include('user_auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
