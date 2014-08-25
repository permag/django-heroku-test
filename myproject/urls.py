from django.conf.urls import patterns, include, url
from django.contrib import admin
from apps.myapp import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', views.index, name='index'),
    url(r'^polls/', views.polls, name='polls'),
    url(r'^polls\.(?P<extension>(json)|(xml))$', views.polls, name='polls'),
)

import settings
from settings.prod import DEBUG

if DEBUG is False:   # if DEBUG is True it will be served automatically
    urlpatterns += patterns('',
            url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.prod.STATIC_ROOT}),
    )
print "UUEUEUEUEUEUEUEU"