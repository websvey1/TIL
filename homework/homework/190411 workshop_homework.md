190411 workshop_homework

1. 아래는 Django에서 myapp의 Musician class에 저장된 기본 시드 데이터이다.
   이를 적용하기 위해 필요한 json 파일을 만들어 적용해보자.

   ```python
   #1
   (bash) django-admin startproject prac .
   (bash) python manage.py startapp workshop
   
   모델, admin 만들기
   <<workshop>>에 <<fixtures>> 폴더 만들고 sample.json 만들기
   공식문서에 django procifid data 검색해서 data 를 sample.json에 넣기
    - 이때, 모델과 data의 컬럼명이 같아야함
   (bash) python manage.py loaddata sample.json  으로 데이터를 db에 넣는다.
   
   admin에 들어가서 확인
   
   (bash) python manage.py dumpdata (appname).(modelname) > (save_filename).json  하면 json파일이 만들어짐
   
   문제의 파일은 yaml이므로 django docs 참조.
    - pip install pyyaml  설치
    - docs에 나온대로 명령어 입력
      (bash) python manage.py dumpdata (appname).(modelname) --format yaml > final.yaml
   
   ```

   

![1556172103044](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1556172103044.png)

참고 : <https://coderwall.com/p/mvsoyg/django-dumpdata-and-loaddata>

---

homework

1. Django에서 모델의 기초 데이터베이스의 값을 제공하기 위해서는 Fixtures를
   사용한다. 해당 파일은 기본적으로 각각의 app에 fixtures 폴더에 있어야하며,
   파일 형식은 [ ]이거나 [ ]이다.

    [  json, xml ]

2. 워크샵처럼 실제 Django에 데이터가 저장되어 있을 때, 아래의 fixtures 파일
을 만들고자 한다. 사용해야하는 명령어를 작성하라.