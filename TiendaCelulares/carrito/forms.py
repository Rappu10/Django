from django import forms
from .models import CarritoItem

class AgregarAlCarritoForm(forms.ModelForm):
    class Meta:
        model = CarritoItem
        fields = ['cantidad']
