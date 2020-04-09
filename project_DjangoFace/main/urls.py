from django.urls import path, include
from django.conf.urls import url
from . import views

from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

urlpatterns = [
                path ('', views.Suspect_list, name='main'),
                path ('', views.Suspect_list, name='account_login'),
                path ('', views.Suspect_list, name='suspect_list'),
                url(r'^suspect/(?P<pk>[0-9]+)/$', views.Suspect_detail, name='suspect_detail'),
                url(r'^suspect/new/$', views.Suspect_new, name='suspect_new'),
                #url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
                #url(r'^media/(?P<path>.*)$','django.views.static.serve', {'document_root':'media'}),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#.as_view()