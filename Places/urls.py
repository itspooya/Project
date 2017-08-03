from django.conf.urls import url

from Places.views import place_detail_view_func

urlpatterns = [

    url(r'^(?P<id>\d+)', place_detail_view_func, name='places_detail_view')
]
