# 190220 workshop

문제
자신의 반에 있는 사람들의 데이터를 저장하는 Student모델을 생성합니다.
Student모델이 가져야 할 필드는 아래와 같습니다.
 name(이름) : CharField
email(이메일) : CharField
birthday(생년월일) : DateField
age(나이) : IntegerField

 모델 마이그레이션 작업을 거친 후
Admin페이지에서 주변 학생들의 이름을 세명 저장합니다.

 저장 후 Admin페이지에서 학생들의 목록을 보기 쉽게 만들기 위해서
__str__메소드를 오버라이드 하여 name이 출력되게 만듭니다.

```
class Student(models.Model):
name = models.Charfield(max_length=10)
email = models.Charfield(max_length=20)
birthday = models.DateField
age = models.IntegerField

python manage.py makemigrations boards

student = Student()
student.name = "NAM"
student.name = "KIM"
student.name = "JO"
student.save()

def __str__(self):
        return f'{self.id}: {self.name}'
```



# 190221 workshop





---

---

---

# homework



1. Django에서 선언한 Model을 실제 DB에 반영하는 과정을 무엇이라고 하는가?

2. 모델의 필드를 정의할 때 CharField는
    필수로 들어가야하는 인자가 존재한다. 무엇인가?

3. Django 에서 동작하는 모든 명령을 대화식 Python 쉘에서
    시험할 수 있는 명령어를 작성하세요

4. Post라는 이름의 모델은 CharField로 정해진 title과 CharField로 정해진 content가
    필드로 정의 되어있다. 제목은 자신의 이름, 내용은 자신의 이메일 정보가 들어
    간 Post를 만드는 코드를 작성하세요

  ```
  1. migrate
  2. max_length=x
  3. python manage.py shell
  4. 
  class Post(models.Model):
  	title = models.CharField(max_length=10)
  	content = models.CharFiedl(mak_length=20)
  	def __str__(self):
          return f'{self.id}: {self.title}'       # 모델이 바뀌면 
  ```

  

# 190221 workshop

1. Django에서는 사용자가 자신의 의지와는 무관하게 공격자가 의도한 행위를 특정 웹 사이트에 요청하게 하는 공격을 막는 기능을 기본적으로 동작시킨다. 위의 공 격은 무엇을 의미 하는가?

2. 기본적으로 Django에서 views.py에 함수들을 정의할 때 request인자 값을 넣어주 어야 한다. request를 활용해서 아래의 폼을 통해서 들어온 데이터를 가져오는 코드를 작성하세요

   ```html
   <form action="/create/" method="POST>
   	<input type="text" name="title">
   	<input type="submit" value="submit">
   </form>
                                          
   ```

   

3. 다음은 사용자가 이미 작성한 글을 수정하기 위해서 기존의 글을 보여주는 edit페이지를 위한 views.py의 코드이다.

  ```python
  def edit(request, id):
      post = Post.objects.get(id=id)
      return render(request, 'board/edit.html', {'post': post})
  ```

  

  아래의 코드에 기존의 데이터를 보여줄 수 있도록 코드를 수정하세요

  ```html
  <form action="/posts/{{post.id}}/update/" method="POST">
      {% csrf_token %}
      <input type="text" name="title" id=>
      <input type="text" name="content">
      <input type="submit" name="submit">
  </form>
  ```





---

```html
1. backdoor

2. data = request.POST.get("title")

3. 
<form action="/posts/{{post.id}}/update/" method="POST">
    {% csrf_token %}
    <input type="text" name="title" id="title" value= {{ post.title }}>
    <input type="text" name="content" id="content" value={{ post.contetn }}>
    <input type="submit" name="submit">
</form>
```

