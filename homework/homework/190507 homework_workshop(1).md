190507 homework_workshop(1)

1. SPA가 무엇의 약자인지 작성하고, 어떤 것을 의미하는지 간략하게 작성하시오.

   ```
   Single Page Application의 약자, 처음 호출된 HTML상에서 필요한 데이터를 호출하여 화면을 새로 구성하여 실제 페이지로의 이동이 일어나지 않ㄴ는다
   ```

   

2. 'MVVM 패턴'에서 MVVM은 무엇의 약자인지 작성하고, 그 중에서 Vuejs가 담당하는 부분은 무엇인지 간략 하게 작성하시오.

   ```
   model, 
   view
   viewmodel (O)
   ```

   

---

workshop

다음은 Vue 인스턴스를 사용하여 렌더링한 DOM의 결과물이다.

`Hello, World!`

위와 같이 렌더링 하기 위하여 필요한 (a), (b)를 작성하여 Vue 인스턴스를 완성하시오.

(a) = {{ message }}

(b) = '#app'

```html
<body>
    <div id='app'>
        <h1> ( a ) </h1>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
        const app = new Vue({
            el: ( b ) ,
            data:{
                meaasge:'Hello, World'
            },
        })
    </script>
</body>
```

