"""sitemonitor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.views.generic.base import RedirectView

favicon_view = RedirectView.as_view(url='/st/logo/favicon.png', permanent=True)

urlpatterns = [
    url(r'^favicon\.ico$', favicon_view),
    url(r'', include('monitor.urls')),
    url(r'^auth/', include('auth.urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^memberdir/', include('members.urls')),
    url(r'^roles/', include('roles.urls')),
    url(r'^settings/', include('settings.urls')),
]
