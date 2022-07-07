from dataclasses import fields
from tkinter import Widget
from .models import Database1
from django import forms
class Form1(forms.ModelForm):
    class Meta:
        model = Database1
        fields = ['name', 'roll', 'registration', 'department']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'roll' : forms.NumberInput(attrs={'class':'form-control'}),
            'registration' : forms.NumberInput({'class':'form-control'}),
            'department' : forms.TextInput(attrs={'class':'form-control'}),
        }