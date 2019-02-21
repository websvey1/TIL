# 190220 django_day_3

```
PROCJECT02 안에서
pyenv virtualenvs => 가상환경 이름 확인하기
pyenv local django-venv => django-venv가 이름.. 가상환경 실행
django-admin startproject crud .
  = >  현재경로에 crud 라는 프로젝트를 만듬

setting에서 ALLOWED HOST에 '*' 넣고 언어설정(ko-kr, Asia/Seoul)
서버열면 로켓과함꼐 바뀐언어로 나옴
python manage.py startapp boards
  = > 앱을 프로젝트와 같은 위치(동등한 위치)에 생성후 setting에서 
  INSTALLEDS APPS에 "boards.apps.BoardsConfig" 추가

django는 기본ㄱ적으로 sqlite3가 설치되어있다
다른 SQL을 쓰고싶으면 setting애서 DATABASE에서 바꾸면 된다

models에서 만들기 ! ( 파일 참조)

이후 bash에서

python manage.py makemigrations boards => mygrations폴더에 파일 생성
	Migrations for 'boards':
  		boards/migrations/0001_initial.py
    	- Create model Board
   라는 창이 뜨는게 정상.
  001.initial 파일은 우리가 만든 설계도 라고 생각하면 된다. migrate를 하면 sql문으로 바뀌면서 들어가게 된다. 모델은 만드는 중간과정
  
python manage.py sqlmigrate boards 0001 를 하면 sql문으로 어덯게 바뀌어서 들어갈지 출력해서 보여준다(실행하는것이 아님, 보여줌)

models.py에서 update를 만들고
$ python manage.py makemigrations boards  하면 002가 생김
$ python manage.py migrate 를 하면 OK창이 여러개 뜨는데 db가 만들어진것이다
python manage.py sqlmigrate boards 0002를 해보면 어떻게 추가될지 볼 수 있다.

sqlite3 db.sqlite3 해서 sqlite3로 ㄷㄹ어간다
.tables를 하면 테이블 목록이 나옴.
.schema boards_board 로 스키마 확인
.exit로 나간다.

python manage.py shell을 켜서
from boards.models import Board 입력
(아래부터 장고 ORM 문법)
Board.objects.all() => 빈 리스트가 뜬다. db안에 아무것도 만든게 없어서

board= Board()로 클래스 생성
board.title = 'first'
board.content = 'django!' 클래스 내 메서드 값 입력
board.save() => 저장 .. 하면 db에 저장됌
다시 Board.objects.all() 하면 아까와다르게 방금 만든 db가 보임
(model에 메서드를 추가하고 다시 파이썬쉘을 킴)

다시 Board.objects.all() 하면 더 직관적으로 보인다.

---
django extension 설치 (from boards.models import Board
>>> Board.objects.all() 같은 반복과정을 업애기 위해서 ㄱ 설치)
pip install django-extensions 설치하고  setting에 들어가서
INSTALLEDS APPS에 'django_extensions', 추가 해야 확장프로그램 사용가능

이후 bash에서 python manage.py shell_plus를 하면 알아서 from import가 되어있음
board = Board(title='second', content='django!!') 로 만들고
board.save()로 저장한후 Board.objects.all()로 보면
우리가 만든게 하나 추가되어서 두개가 되어있다.
Board.objects.create(title="third", content="django!!!")는
save에 print까지 해준다.
Board.objects.all()로 확인해보면 DB가 3개이다.

>>> board.title= "1234567890123"
>>> board.full_clean() 하면 django.core.exceptions.ValidationError: {'title': ['이 값이 최대 10 개의 글자인지 확인하세요(입력값 13 자).'], 'content': ['이 필드는 빈 칸으로 둘 수 없습니다.']}라는 오류가 뜬다

Board.objects.filter(title="first").all()= SELECT * FROM Board where title="first"
>>> Board.objects.filter(title="first").all()
<QuerySet [<Board: 1: first>]> 몇개인지 모르기때문에  리스트로 나옴
>>> Board.objects.filter(title="first").first()
<Board: 1: first> 1개만 출력이기때문에 객체로 나옴

board = Board.objects.get(pk=1) 기본키 가져오기.
<Board: 1: first> 하나의 객체로 가져옴.
board = Board.objects.filter(id=1) 이렇게 가져오면 
<QuerySet [<Board: 1: first>]> 이렇게 쿼리로떠버림. 


SQL의 %LIKE 같은 것
>>> boards = Board.objects.filter(title__contains="fi").all()
>>> boards
<QuerySet [<Board: 1: first>]>

!로 끝나는 것 검색
>>> boards = Board.objects.filter(content__endswith="!")
>>> boards
<QuerySet [<Board: 1: first>, <Board: 2: second>, <Board: 3: third>, <Board: 4: fourth>]>

fi 로 시작하는 것 검색
>>> boards = Board.objects.filter(title__startswith="fi")
>>> boards	
<QuerySet [<Board: 1: first>]>

내림차순 ( -를 없애면 오름차순)
>>> boards= Board.objects.order_by('-title').all()
>>> boards
<QuerySet [<Board: 3: third>, <Board: 2: second>, <Board: 4: fourth>, <Board: 1: first>]>

지우기
>>> board = Board.objects.get(pk=1)
>>> board.title = 'hello'
>>> board.save()
>>> board.title
'hello'
>>> board.delete()
(1, {'boards.Board': 1}) 이걸 지웟다는 뜻

views.py에서 실행(파일참조)
```

---

---

---

점심먹고 이후

``` 
python manage.py createsuperuser 실행 후 id email pw 만들기
만들면 admin 주소로 들어갈 수 있따.
admin.py에서 관리자 계정 로그인 가능함.

class BoardAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'create_at', 'update_at',)
admin.site.register(Board, BoardAdmin) 입력하면, 들어가지 않아도 글 내용과 이력이 다 보임
```

