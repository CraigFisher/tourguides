from django.conf.urls import patterns, include, url
from django.contrib import admin
# from django.contrib.auth.urls


urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'tourguides.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^profiles/', include('profiles.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # FOR LOGIN, LOGOUT, PASSWORD RESET, ETC.
    # url('^', include('django.contrib.auth.urls')),
    url('^', include('base.urls')),
)
