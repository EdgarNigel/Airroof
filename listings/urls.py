from django.conf.urls import url

from .views import (
    ListingListview,
    ListingDetailview,
    ListingCreateView,
    ListingUpdateView,
)

urlpatterns = [
    url(r'^$', ListingListview.as_view(), name="list"),
    url(r'^create/$', ListingCreateView.as_view(), name="create"),
    url(r'^(?P<slug>[\w-]+)/$', ListingDetailview.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', ListingUpdateView.as_view(), name='edit'),
]
