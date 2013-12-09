from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'web.views.home', name='home'),
    url(r'^login/', 'web.views.login', name='login'),
    url(r'^logout/$', 'web.views.logout', name='logout'),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^actions/', include('web.actions.urls')),

    url('^do/(?P<id>\d*)$', 'web.views.do', name='do'),
)
