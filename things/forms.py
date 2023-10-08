from django import forms
from django.core.validators import RegexValidator
from .models import Thing

"""Forms of the project."""

class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
        widgets = {'description' : forms.Textarea(), 'quantity' : forms.NumberInput()}
