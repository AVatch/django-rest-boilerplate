from django.conf import settings
from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/' + settings.API_VERSION + '/', include('accounts.urls')),
)

urlpatterns += staticfiles_urlpatterns()