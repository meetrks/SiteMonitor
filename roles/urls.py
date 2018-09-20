from django.conf.urls import url
from django.views.generic import TemplateView

from roles import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='roles/index.html')),
    url(r'^role/$', views.RolesView.as_view()),
    url(r'^role/(?P<id>[a-zA-Z0-9-]{36})/$', views.RolesView.as_view()),
]
