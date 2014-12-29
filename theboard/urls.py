from django.conf.urls import patterns, include, url
from django.contrib import admin
from job.views import *
from django.conf import settings


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'theboard.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^$', 'job.views.Index'),
    (r'^profile/$', 'crew.views.UserProfile'),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {         'document_root': settings.STATIC_ROOT     }),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {         'document_root': settings.MEDIA_ROOT     }),
    (r'^jobs/$', 'job.views.JobsAll'),
    (r'^jobs/(?P<jobslug>.*)/$', 'job.views.SpecificJob'),
    (r'^login/$', 'crew.views.LoginRequest'),
    (r'^logout/$', 'crew.views.LogoutRequest'),
    (r'^resetpassword/passwordsent/$', 'django.contrib.auth.views.password_reset_done'),
    (r'^resetpassword/$', 'django.contrib.auth.views.password_reset', {'post_reset_redirect' : '/reset/done/'}),
    (r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm'),
    (r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete'),

)
