from django.conf.urls import url

from .views import (
    EventListView,
    EventDetailView,
    EventCreateView,
    EventUpdateView,
)

urlpatterns = [
    url(r'^$', EventListView.as_view(), name="list"),
    url(r'^create/$', EventCreateView.as_view(), name="create"),
    url(r'^(?P<pk>\d+)/$', EventDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/edit/$', EventUpdateView.as_view(), name='edit'),
    #url(r'^(?P<slug>[\w-]+)/edit/$', ListingUpdateView.as_view(), name='edit'),
]
