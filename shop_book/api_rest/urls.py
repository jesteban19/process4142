from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api_rest import views

urlpatterns = [
    url(r'^book/(?P<pk>[0-9]+)$', views.book_detail),
    url(r'^book/$', views.book_list),
    url(r'^author/$', views.author_list),
    url(r'^author/(?P<pk>[0-9]+)$', views.author_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)