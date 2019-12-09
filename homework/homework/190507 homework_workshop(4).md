190507 homework_workshop(4)

---

1. v-model 디렉티브는 input, textarea, select와 같은 엘리먼트들과 ____(a)____을 생성합니다. 빈칸 (a)에 들어 갈 말을 작성하시오.

   (a) form 관련 태그

   

2. v-model 디렉티브는 엘리먼트의 종류에 따라 인스턴스의 속성을 업데이트하는 데이터의 타입이 다릅니다. 아래의 엘리먼트들이 기본적으로 어떠한 데이터 타입으로 인스턴스의 속성을 업데이트 하는지 https://kr.vuejs.org/v2/guide/forms.html를 참고하여 작성하시오.

- input -str
- textarea  - str
- 단일 checkbox  - boolean
- 다중 checkbox  - arr
-  radio - str
-  단일 select -str
-  다중 select = arr

---

 v-bind와 v-model 디렉티브를 활용하여, 다음와 같이 'Go!' 링크를 누르면 입력 창에 작성한 URL로 가도록 하는 '주소가 변하는 링크'를 만들어 봅시다.

```html
<body>
    <div id='app'>
        <input type="text" v-model="url">
        <a v-bind:href="url">GO!</a>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
        const app = new Vue({
            el: '#app',
            data:{ url:'', }
        })
    </script>
</body>
```

