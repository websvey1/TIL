190507 homework_workshop(2)

---

1. html 속성(attributes)에는 인터폴레이션(Interpolation)으로 값을 직접 넣지 못하기 때문에 디렉티브 ____(a)____를 사용해야 한다. 빈칸 (a)에 들어갈 디렉티브를 작성하시오.

   (a) v-bind

2. 동일한 노드에 ____(a)____와 ____(b)____ 두 디렉티브가 함께 있다면 ____(a)____가 ____(b)____보다 높은 우선 순위를 가지며, ____(b)____는 루프가 반복될 때마다 실행됩니다. 빈칸 (a), (b)에 들어갈 디렉티브를 작성 하시오.

   (a) for

   (b) if

---

workshop

 다음과 같은 Vue 인스턴스가 있을 때, v-for와 v-if 디렉티브를 활용하여 짝수만 나타나 도록 하는 리스트를 만들어 봅시다.

```javascript
var app = new Vue ({
    el: '#app',
    data: {
        numbers: [0,1,2,3,4,5,6,7,8,9],
    },
})
```

```
- 0
-2
-4
-6
-8
```

```html
<div id='app'>
	<h2>
        <li v-for="number in numbers" v-if="!(number%2)">
            {{ number }}
        </li>
    </h2>
</div>
```

