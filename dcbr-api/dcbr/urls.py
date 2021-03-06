"""dcbr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

from . import views

admin.site.site_header = "Dog and Cat Breeder Registry"
admin.site.site_title = "Dog and Cat Breeder Registry"
admin.site.index_title = "Dog and Cat Breeder Registry"

urlpatterns = [
    path("", RedirectView.as_view(url="authenticate")),
    path("authenticate", views.authenticate),
    path("admin/doc/", include("django.contrib.admindocs.urls")),
    path("admin/", admin.site.urls),
    url(r"^health/", include("health_check.urls")),
    url(r"^api/", include("api.urls")),
    url(r"^oidc/", include("mozilla_django_oidc.urls")),
]
