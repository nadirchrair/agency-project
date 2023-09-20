from django import forms
from .models import *

class OffreForm(forms.ModelForm):

    class Meta:
        model = Offre
        fields = '__all__'
        exclude = ['username']

        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'name_offre': forms.TextInput(attrs={'class': 'form-control'}),
            'descreption': forms.Textarea(attrs={'class': 'form-control'}),
            'dureé': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'complete': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
        }
