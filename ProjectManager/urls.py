from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
	url(r'^$', 'project_ticket.views.home', name="home"),
    url(r'^user/', include('project_ticket.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
