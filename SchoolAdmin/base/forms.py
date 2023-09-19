from django import forms
from .models import Grade_7_8

class Grade_7_8_Form(forms.ModelForm):
    class Meta:
        model = Grade_7_8
        fields = ['physics', 'chemistry', 'biology']