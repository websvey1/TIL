from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Movie, Score, Genre

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', '작성!'))
    
class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = ['content', 'score']
        widgets = {'score':forms.NumberInput(attrs={
            'min':0,
            'max':5,
        })}