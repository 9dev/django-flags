from django.conf.urls import patterns, url

from flags import views


urlpatterns = patterns('',               
    url(
        r'^create/(?P<app_label>[a-z0-9_]+)/(?P<model_name>[a-z0-9_]+)/(?P<pk>[0-9]+)$',
        views.FlagCreateView.as_view(),
        name='flag_create',
    ),
)
