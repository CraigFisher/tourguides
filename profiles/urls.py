from django.conf.urls import patterns, url
from profiles import views
from profiles.views import Profile


urlpatterns = patterns(
    '',
    url(r'^(?P<user_id>\d+)/$', Profile.as_view(), name='profile')
)
