190409 homework

1. 로그인을 한 사용자만 게시물을 작성할 수 있도록 코드를 작성하려고 한다. 빨간 박스에 들어갈 코드를 작성하세요.

   ```python
   from django.contribu.auth import User
   
   @login required
   ```

2. Board모델에 게시물을 작성한 사람을 저장할 칼럼을 추가하려고 한다. 이 를 위해 필요한 모듈과 ForeignKey에 너허야 할 인자를 작성하세요.

   ```python
   from django.conf import settings
   
   class Board(models.Model):
       user = models.ForeignKey(setting.AUTH_USER_MODEL, on_delete=models.CASCADE)
   ```

   

190409 workshop

view

```python
def signup(request):
    if request.user.is_authenticated:
        return redirect('boards:index')
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('boards:index')
    else:
        form = UserCreationForm()
    context={'form':form}
    return render(request, 'accounts/auth_form.html', context)      
```

urls

```python
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
]
```

templates

```html
{% extends 'boards/base.html' %}
{% block body %}
{% load crispy_forms_tags %}
<h1>회원가입</h1>
<form action="" method='POST'>
    {% csrf_token %}
    {{ form|crispy }}
    <input type="submit" value="submit"/>
</form>
{% endblock %}
```

