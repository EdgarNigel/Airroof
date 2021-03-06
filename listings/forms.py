from django import forms

from .models import Listing
from. validators import validate_category

# class ListingCreateForm(forms.Form):
#         name        = forms.CharField()
#         location    = forms.CharField(required=False)
#         category    = forms.CharField(required=False)
#
#         def clean_name(self):
#             name = self.cleaned_data.get("name")
#             if name == "Hello":
#                 raise forms.ValidationError("Not a valid name")
#             return name

class ListingCreateForm(forms.ModelForm):
    class Meta:
        model   = Listing
        fields  = [
            'name',
            'location',
            'category',
        ]
    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name == "Hello":
            raise forms.ValidationError("Not a valid name")
        return name
