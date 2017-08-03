from django import forms

from .models import *


class PlaceForm(forms.ModelForm):
    placename = forms.CharField(max_length=100, min_length=5)
    placetype = forms.ChoiceField(choices=PLACE_TYPES, widget=forms.RadioSelect())
    WiFiSSID = forms.CharField(max_length=32)
    WiFiPassword = forms.CharField(max_length=32, min_length=8)
    power = forms.ChoiceField(choices=POWER_TYPES, widget=forms.RadioSelect())
    Noiselevel = forms.ChoiceField(choices=NOISELEVEL_TYPES, widget=forms.RadioSelect())
    protips = forms.Textarea()
    OpenHour = forms.TimeField()
    CloseHour = forms.TimeField()
    Amenties = forms.MultipleChoiceField(choices=Amenties_CHOICES, widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Place
        fields = '__all__'
