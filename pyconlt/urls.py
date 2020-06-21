"""pyconlt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.flatpages.views import flatpage
from django.views.generic.base import TemplateView

from proposals.views.talks import TalksListView

urlpatterns = [
    url(r'^accounts/', include('allauth.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^talks/', TalksListView.as_view(), name='talks_list'),
    url(r'^', include('presenters.urls')),
    url(r'^proposals/', include('proposals.urls')),
    url(r'^demo/', include('demo.urls')),
    url(r'^', include('program.urls')),
    url(r'^(?P<url>.*/)$', flatpage),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]
