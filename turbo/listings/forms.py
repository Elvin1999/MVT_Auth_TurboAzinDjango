from django import forms
from .models import Listing

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = [
            'title',
            'description',
            'price',
            'city',
            'brand',
            'model',
            'year',
            'milage',
            'fuel',
            'gearbox'
            'main_image'
        ]

        widgets={
            'description': forms.Textarea(attrs={'rows':4}),
        }