190416 homework_Workshop

---

1. HTTP 상태 코드에서 200 Ok는 요청에 대해 성공적으로 수행하였음을 나타낸
  다. 아래의 HTTP 응답 코드의 의미를 작성하시오.
  – 404 : 서버가 요청한 페이지를 찾을 수 없다
  – 405 : method not allowd / 클라이언트가 요청한 리소스에서는 사용불가능한 method를 이용했을 경우 서버가 응답하는 코드
  – 500 : internal sever error 내부 서버 오류

2. Django에서 지정된 레코드에 값이 없을 때 404 에러를 나타내도록 하는
  shortcut은 무엇인가. (import 문 포함)

  from django.shortcut import get_objects_or_404

3. 아래의 설명 중 REST API 설계 기본 규칙에 어긋난 것은?
  V (1) 자원에 필요한 경우 CRUD 동사 표현이 들어갈 수 있다.
  – (2) 자원은 대문자보다 소문자를 사용한다.
  – (3) URL에 HTTP Method를 사용하지 않는다.
  – (4) 자원간의 연관 관계가 있는 경우 posts/1/comments/ 와 같이 작성한다.
  – (5) URL에서 변하는 부분은 posts/<int:post_pk>/ 와 같이 유일한 값이다.



---

아래의 두 코드에 적절한 데코레이터를 작성하여 허용되지 않은 HTTP Method의 경우
405 Method Not Allowed 상태코드를 반환하도록 하시오.

from django.views.decorators.http import require_http_methods, require_POST

@require_http_methods(['GET','POST'])

![1556173314902](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1556173314902.png)

@ require_POST

![1556173322287](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1556173322287.png)