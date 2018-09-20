from django.conf.urls import url
from django.views.generic import TemplateView

from members import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='settings/index.html')),
    # url(r'^member/$', views.MemberDirectoryView.as_view()),
    # url(r'^member/(?P<id>[a-zA-Z0-9-]{36})/$', views.MemberDirectoryView.as_view()),
]
