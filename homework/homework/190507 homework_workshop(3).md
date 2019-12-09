190507 homework_workshop(3)

---

1. 빈칸 (a) 들어갈 v-bind 디렉티브의 약어를 작성하시오.

   ```html
   <a v-bind:href="url"></a>
   <a (a)="url"></a>
   ```

   (a) :   href

2. 빈칸 (a)에 들어갈 v-on 디렉티브의 약어를 작성하시오.

   ```html
   <a v-on:click="doSomethind"></a>
   <a (b)="doSomethind"></a>
   ```

   (b) : @click

3. computed 속성과 watch 속성에 대하여 간략하게 설명하고, 이 둘의 차이점에 대해 작성하시오.

   computed - 미리 계산된 값을 반환한다. 처음 값이 바뀌지 않는다

   watch - 데이터변화를 감지하여 자동으로 특정 로직을 수행한다. 비동기처리에 적합

---

workshop

```html
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>v-model</title>
    
</head>
<body>
    <div id='app'>
        <h1>카운터 : {{ number }}</h1>
        <button @click="plus">증가</button>
        <button v-on:click="minus">감소</button>
    </div>
    
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
        const app = new Vue({
            el: '#app',
            data:{
               number:0,
            },
            methods:{
                plus: function () {
                    this.number++
                },
                minus: function () {
                    this.number--
                }
            }
        })
    </script>

</body>
</html>
```

