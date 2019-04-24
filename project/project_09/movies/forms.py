from django import forms
from .models import Score

class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = ['value', 'content',]
        widgets = {
            'value': forms.NumberInput(attrs={
                'max': '5',
                'min': '0',
            })
        }