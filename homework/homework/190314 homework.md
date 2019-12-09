190314 homework

---

1. School 모델과 Student 모델을 1:N관계로 설정하려고 한다. models.py에 넣어야 하는 코드를 작성하세요. (1:N관계중 N의 클래스를 작성해주세요)

```python
class Student(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    content = models.TextField()
    def __str__(self):
        return self.content
```

2. Question 모델과 Comment 모델은 1:N관계를 가지고 있다. A = Question.objects.get(id=id) 위의 코드가 있을때 views.py에서 Comment를 모두 가져오기 위한 코드를 작성하세요. (related_name 은 설정하지 않았다고 가정한다.)

```python
comments = question.comment_set.all()
```

3.기본적으로 1:N관계를 설정을 할때 ForeignKey를 이용해서 1에 해당하는 클래스 를 지정해준다. 지정한 클래스가 Movie일때 ForeignKey로 지정된 컬럼의 이름은 무엇인가?

```python
movie_pk or id
```

---

homework 2

1. Question 모델과 Comment 모델이 1:N관계라고 할때 하나의 Question을 보여 주는 페이지에서 Comment를 모두 보여주려고 한다. 다음과 같은 detail.html이 있을때 모든 Comment의 content를 h3태그를 이용해서 출력하는 for문을 작성 하세요. (related_name은 설정해주지 않았다고 가정한다.)

   ```html
   {% for comment in comments %}
   	<li>
       	{{ comment.content }}                
   	</li>
   {% endfor %}
   ```

   

2.  다음과 같은 urls.py 파일이 있다고 가정할때 comment를 작성하는 버튼을 만들기 위해 form태그 안에 action속성값으로 넣어줘야 하는 경로를 작성하세요

   ```html
   {% url 'boards:comments_create' board.pk %}
   ```

   





----

190314 workshop



설문 앱을 만들려고 한다. 이 앱은 질문에 대한 답변을 투표하여 각각의 항목이 몇 표 를 받았는지 저장하는 기능을 가지고 있다. 설문 앱은 Question 모델과 Choice 모델을 가지고 있으며, 각각의 모델은 다음과 같은 컬럼을 가지고 있고 1:N 관계를 가지고 있다.

Question title(제목) : CharField Choice content(내용) : CharField votes(투표수) : IntegerField

해당 컬럼을 가지고 있는 Question 모델과 Choice 모델을 정의하는 코드(models.py) 를 작성하시오.

```python
from django.db import models

class Question(models.Model):
    title = models.CharField(max_length=20)
class Chice(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    content = models.CharField(max_length=20)
    votes= models.IntegerField()
```



workshop(2)

```html
{% for choice in choices %}
<li>
	{{ choice.content }} : {{ choice.vote }} 표
</li>
{% endfor %}
```

