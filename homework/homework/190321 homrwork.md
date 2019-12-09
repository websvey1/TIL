190321 homrwork

```python
from django import forms
```



```python
{{form.as_p}}
```

```python
cleaned_data
```





190321 workshop

```python
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class StudentForm(forms.ModelForm):
    class Meta:
        model =Student
        fields = ['name','age',] # __all __

class StudentForm(forms.Form): #가 위에 거랑 같음
    name = forms.CharField(max_length=10)
    age = forms.IntegerField()
```



```html
<form action="/students/create/" method="POST">
    {% csrf_token %}
    {{ form }}
    <input type="submit" value="submit">
</form>
```

