from django.conf.urls import url

from monitor import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='monitor/index.html')),
    url(r'^site/$', views.SiteDetailView.as_view()),
    url(r'^site/(?P<id>[a-zA-Z0-9-]{36})/$', views.SiteDetailView.as_view()),
    # url(r'^user/roles$', (views.RolesView.as_view()), name='roles'),
    # url(r'^user$', (views.UserDetailsView.as_view()), name='user_details'),
    # url(r'^settings/', (views.SettingsView.as_view()), name='settings'),
    # url(r'^api/(?P<flag>.+)/$', (views.ApiView.as_view()), name='all_apis'),
]
