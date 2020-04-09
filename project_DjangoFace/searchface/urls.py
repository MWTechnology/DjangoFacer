from django.urls import path, include
from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

urlpatterns = [
                path ('', views.Mysearchfaceviews, name='searchface'),
                url(r'^(?P<pk>[0-9]+)/$', views.Mysearchfaceviews_sent, name='searchface_sent'),
]


