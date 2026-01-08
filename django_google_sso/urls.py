try:
    from django.urls import path
    USE_PATH = True
except ImportError:
    from django.conf.urls import url
    USE_PATH = False

from django_google_sso import conf, views

app_name = "django_google_sso"

urlpatterns = []

if conf.GOOGLE_SSO_ENABLED:
    if USE_PATH:
        urlpatterns += [
            path("login/", views.start_login, name="oauth_start_login"),
            path("callback/", views.callback, name="oauth_callback"),
        ]
    else:
        urlpatterns += [
            url(r'^login/$', views.start_login, name="oauth_start_login"),
            url(r'^callback/$', views.callback, name="oauth_callback"),
        ]
