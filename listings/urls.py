from django.conf.urls import url

from .views import (
    ListingListView,
    ListingDetailView,
    ListingCreateView,
    ListingUpdateView,
)

urlpatterns = [
    url(r'^$', ListingListView.as_view(), name="list"),
    url(r'^create/$', ListingCreateView.as_view(), name="create"),
    url(r'^(?P<slug>[\w-]+)/$', ListingDetailView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', ListingUpdateView.as_view(), name='edit'),
]
