190501 homework_workshop

----

1. DOM에서 특정 요소를 선택할 때 document.querySelector() 뿐만 아니라 document.querySelectorAll() 역시 사용할 수 있다. 둘의 차이를 검색하여 기술하시오.

   ```
   특정 name이나 id를 제한하지 않고 css선택자를 통해 제일먼저 등장하는 1개를 가져옴, 없으면 null를 반환
   All = 해당하는 모든 것을 리스트로 가져옴, 없으면 빈 리스트 []를 반환
   ```

   

2. JS에서 자주 사용하는 EventListener 들 중 아래와 같은 것들이 있다. 각각 간 략하게 어떤 Trigger 를 의미하는지 조사하여 간략하게 기술하시오. 

   ```
   – click //클릭했을때
   – mouseover/mouseout/mousemove 올렸을때, 객체바깥으로 나갔을때, 마우스움직일때마다
   – keypress/keydown/keyup 키를 누르고있을때, 키를 눌렀을때, 키를 눌럿따 뗐을때
   – load / 문서나 객체가 로딩되었을때
   – scroll / 스크롤바를 조작할때, 드래그할때
   – change / 객체의 내용ㅇ이 바뀌고 focus를 잃었을때
   ```

   

3. DOM 에 요소를 추가할 때, innerHTML += 의 방법과 appendChild() 함수를 통해 추가하는 방법이 있다. 둘의 차이를 간략하게 기술하시오.

   ```
   InnerHTML - Property, 내부를 완전교체, 속도가 빠름, 
   appendChild() - Method, 추가(후방삽입), 속도가 느림,
   ```

---

---

아래 instruction에 따라 js코드를 작성해보자

```html
<!DOCTYPE html>
<html lang="en">
	<head>
		<title>Clicked</title>
	</head>
<body>
    <h1>0</h1>
    <button id="change-btn">Click it</button>
    <script>
        // #change-btn 을 button 상수에 할당한다.
        const button = document.querySelector('#change-btn')

        // h1 태그를 header 상수에 할당한다.
        const header = document.querySelector('h1')

        // clickCount 변수를 0으로 초기화 한다.
        let clickCount = 0

        // button에 'click' eventListner를 추가한다. 클릭이 일어나면,
        button.addEventListener('click', event => {

            // clickCount 가 1씩 올라간다.
            clickCount += 1
            
            //  클릭수 증가와 내용변경을 한줄ㄹ
            // header.innerText = ++clickCount
            
            // header 안의 내용을 clickCount 로 바꾼다.
            header.innerText = clickCount
        })        

        
    </script>
</body>
```

