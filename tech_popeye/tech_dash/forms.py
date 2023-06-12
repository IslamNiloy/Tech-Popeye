from django import forms
from .models import CarouselItem

class CarouselItemForm(forms.ModelForm):
    class Meta:
        model = CarouselItem
        fields = ['image', 'caption', 'title']
