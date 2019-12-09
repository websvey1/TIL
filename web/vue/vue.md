190507 vue

# 디렉티브

---

- vue에서 제공하는 특수 속성임을 나타내는 v-접두어가 붙어있으며, 렌더링된 dom에 특수한 반응형 동작을 한다

- v-on:click = addEventlistener와 같다, 디렉티브(v-on)뒤에 붙은것=> 전달인자 == 이벤트이름

  - v-on:이벤트이름(click) == '메서드 이름'

- v-bind = html 태그의 속성값에  vue에서 만든 데이터 값으로 사용해야 할때 사용한다

  ```html
  <img v-bind:src="">
  <img src = "">
  ```

- v-model 은 input, select, textarea과 같은 form에 관련된 태그에만 사용할 수 있다.

  - v-4 누르면 행복해집니다 부분이 작동안함



- v-if 는 렌더링 할지 말지 자체를 결정 // 
- v-show는 렌더링은 항상 되고 css를통해 숨겨질지 보여질지를 ㅂ결정함

---

2.리스트 렌더링

- v - for
  - 동일한 노드에 for와 if가 있으면 우선순위는 for가 높ㄴ다, 즉 if는 for가 반복될때마다 실행된다

---



3.이벤트 리스너(형식)

- v- on / @ 
- v-on:전달인자.수식어
- v-on:keyup.enter



4. 데이터바인딩

- v-bind / 생략가능
- v-model

5. 렌더링 & 컴파일 관련

- v-pre : 컴파일 하지 않고 강제로 출력
- v-once : 처음에 단 한번ㅇ만 렌더링 함
- v-cloak: 컴파일이 완료디면 사라지는 디렉티브 (?)

6. template element

- <template> </template> wrapper역할을 한다

---

computed 

- 미리 계산된 값을 반환(Method는 그때그때 계산값을 반환함)
- 템플릿 내에 직접 로직을 넣을 수 있지만, 코드가 너무 복잡해지므로 vue안에 정의해두는것