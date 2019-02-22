190213 django intro

# 0. 준비사항

---

```bash
$ git config --global user.name 'example'
$ git config --global user.email "example@gmail.com"
$ git config --global color.ui true

```

https://github.com/djpy2/TIL/blob/master/doc/git.md 참고

https://gist.github.com/edujunho/bee20c196ecacc3e8cdf068b4ec64d9f

c9 설정

```bash
pyenv virtualenv 3.6.7 django-venv
  => 가상환경 설정
pyenv virtualenvs
  => 가상환경 확인
  3.6.7/envs/django-venv (created from /home/ubuntu/.pyenv/versions/3.6.7)
  django-venv (created from /home/ubuntu/.pyenv/versions/3.6.7)
  같은 메세지가 뜸
 
pyenv local django-venv 
  => 치면 왼쪽에 (django-venv)가 뜨면서 가상환경이 활성화됨

 pip install django
   => 장고 설치
 pip install --upgrade pip
   => 업그레이드 확인
```



```bash
django-admin startproject django_intro .
  => 장고 명령어, django_intro라는 파일을 만듬( .은 현재폴더라는 의미)
  => django, test, class, django 는 프로젝트 이름으로 사용 안함
ls 해보고 manage.py 파일이 있어야함

python manage.py runserver $IP:$PORT
  => 명령을 하면 서버가 켜짐, 아마 오류가 날건데
  django_intro에서 setting에서 ALLOWED_HOSTS를
  'django-intro-websvey1.c9users.io' 로 넣어줘야함 (앞 http 뒤 8080지우고), c9에서만 해야하는 설정 !
```



```bash
touch .gitignore 를 만들고 gitignore.io에가서 django를 검색해서 나온 내용을 
 git ignore안에 붙여넣기!

language_code를 ko-kr로 바꿈
time_zone을 'Asia/Seoul' 로 ㅂㅏ꾸고 다시 서버 키면 한글화 되어있음.

tree 를 bash에 입력하면 바로 구조가 나옴

PROJECT01 이름은 바꿔도 되지만, django_intro이름은 바꾸면 안됨 이미 설정이 되어있음
서버를ㅋ ㅣ니까 db.sqlite3가 만들어 졌따.( 장고 기본설정이기 때문)

urls.py파일은 첫 안내문 같은 내용이 들어있음(index에서 /admin을 붙이면 창이 뜸, url에 설정 되어있다.)

wsgi(web server gateway interface) - 장고에서 사용하는 ㅎ웹서버 규칙.
수정할 일이 없음.
```

여기까지가 프로젝트를 만든것....

---

```bash
django를 할때는 항상 탭을 꺼주자. 탭 이름이 같은게 많다
manage.py -> 장고 프로젝트와 다양한 방법으로 상호작용하는 커맨드라인 유틸리티

프로젝트 이름 폴더(django_intro, first_workshop, study )
 => 실제 파이썬 패키지들이 저장됌, 이 디렉토리 이름을 이용해 어디서드
  import할 수 있음

setting.py : 현재 장고프로젝트의 모든 황경과 구성 저장

__init__.py : 파이썬으로 하여금 이  디렉토리를 패키지처럼 다루라고 알려주는 용도의 단순한 빈 파일

urls.py : 현재 장고의 URL 선언을 저장, 사이트의 URL과 WIEWS의 연결을
지정

views.py => 사용자들에게 정보를 보여줄 곳.. 중요하단다 MTV중 V에 해당
```



```django
python manage.py startapp home
  ==> app을 만든것. 하나의 프로젝트가 여러개의 앱을 관리하는 구조
	  app 자체마다 MTV구조를 가지고 있단다(?)

PROJECT한테 app을 만들었따는 것을 알려줘야함. 
  PROJECT의 settings.py의 INSTALLED_APPS에 'home.apps.HomeConfig', 추가
'student.apps.StudentConfig'과 같이 유동적인 변수임.

  *장고는 항상 문장 마무리에 ,를 넣어야 함*
  home의 apps.py에 들어가보면 이름이 'home'이기 때문에 저렇게 입력한 것.
```

# 1차 commit 완료 // 



## 장고 어플리케이션(APP)

- 실제로 특정한 역할을 하는것이 APP
- 프로젝트는 이런 어플의 집합
- 하나의 프로젝트엔 여러개의 APP이 있음
- 각각의 APP은 MTV패턴으로 구성되어 있다.



어플리케이션 구조

- `admin.py`: 관리자용 페이지 커스터마이징 장소
- `apps.py`: 앱의 정보가 있는 곳ㄴ, 수정할 일이 없다
- `models.py` : 앱에서 사용하는 model을 정의
- `views.py`: 뷰들이 정의되는 곳, 사용자에게 어떤 데이터를 보여줄지 구현

---

---

# 2차 commit 완료 //MTV패턴

---

# 3차 완료 / ()

앞으로 수업 순서 - 

1. 처리할 views(controller)
2. 요청 url
3. 결과 보여줄 templates



-  HttpResponse로 첫 리턴 값 출력하기
- path(route, views, name) 전자 2개는 필수, 후자는 선택
- 저녁메뉴 리턴 실습
- 

---

---

# 4c차 완료 / 오후 시작(Template)

---

---

```
옥션 썰.
ㄴ해커가 옥션과 똑같이 만든 사이트를 운영자에게 보내서 운영자가 로그인하여 계정이 탈취당한적이 있었음. 이걸 방지하기 위해 CSRF방식(사이트간 요쳥 위조)
POST 방식은 DATABASE에 제대로 된 정보를 넣기 위해 사용한다. 그래서 token이 필요하다

```

- 장고에서 사용되는 템플릿은 DTL(Django Template Language)이다

- jinja2와 유사하지만 다르다.!

  4-1.  Template variable

  render()

  - `render(request, template_name, context=None, content_type=None, using=None)`

  4-2. Variable Routing

  def hello(request, name):

  ​	return render(Request, 'hello.html', {'name':name})

----

-----

# 5. From data(get/post)

request.GET.get('data') 

  = > flask는 args가 들어갔음!

request.POST.get('data')

{% csrf_token %}를 form안에 같이 보내줘야합니다

  ```
csef 공격같은 보안관련 사항은 settings에 MIDDLEWARE에 되어있다.
실제로 요청은 미들웨어 설정 사항들은 순차적으로 거친다. 응답은 아래에서 위로 거쳐서 응답이 리턴된다
  ```

---

# 6. Template inheritance

home/templates/base.html 생성하여 반복작업 제거

