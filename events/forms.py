from django import forms

from listings.models import Listing
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'name',
            'listing',
            'tags',
            'public',
        ]

    def __init__(self, user=None, *args, **kwargs):
        print(user)
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['listing'].queryset = Listing.objects.filter(owner=user).exclude(event__isnull=False)
