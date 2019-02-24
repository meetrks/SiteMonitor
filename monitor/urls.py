from django.conf.urls import url
from django.views.generic import TemplateView

from monitor import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='monitor/index.html')),
    url(r'^site/$', views.SiteDetailView.as_view()),
    url(r'^site/(?P<id>[a-zA-Z0-9-]{36})/$', views.SiteDetailView.as_view()),
]
