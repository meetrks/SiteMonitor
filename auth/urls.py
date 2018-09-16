from django.conf.urls import url

from auth import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^login$', TemplateView.as_view(template_name='auth/login.html')),
]
