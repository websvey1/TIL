# java script

---

```javascript
const clap = '<p>짝!</p>'           //const는 문자변수선언
for (let i = 1; i<=10; i++) {        //let은 상수형
    if (i%3===0) {
        document.write(clap);
    } else {
        document.write(`<p>${i}</p>`);
    }
}
```

```javascript
1

2

짝!

4

5

짝!

7

8

짝!

10
```

```javascript
var name='이호중' // ES5 이전에서는 var를 사용했지만, 지금은 안씀 = function scope
let word = '외않되'; // EX6+에서는 이렇게 사용한다. = block scope 
//(const는?) 
  //=> 변하지 않는 값을 사용할때 씀. 재할당 불가!! eS6이후 나옴, 주로 TOKEN과 같은 상수에 씀...

//앞에 아무것도 없이 쓴다면..
word = '전역변수' 

/* 식별자(변수) 원칙
 - 글자, $, 밑줄로 시작(대문자 시작 X, 단, class 제외)
 - 글자, 숫자, $, 밑줄만 사용 가능
 - 유니코드(파이,오메가) 사용가능
 - 예약어 불가능(case, function, return, break 등)
 - camel case(userName) / snake case(user_name) 변수를 쓸때 두가지 방식 중 하나를 사용하자!!
 */
// ''와 ``(f-string과 유사)를 잘 구별하자......

/*
function foo(number){
return 11;
}
========================
파이썬으로 하면
def foo(number):
	return 11
*/
const c = {name:'ho'}
c
> `{name: "ho"}`
const d = {name:'ho'}
c
> `{name: "ho"}`
d
> `{name: "ho"}`
c === d
> `false`         // 객체는 값이 달라도 참조하는 주소가 달라서 같지 안다고 나온다
```

```javascript
function square(num) {
    return num*num
}
square(3)
> `9`
---
    
// 객ㅋ체 내 함수선언.
let person = {
    name:'kim',
    gender:'M',
    phone:'00700',
    sayHello: function () {
        console.log('Hi! my name is ' + this.name)
    }
}

console.log(person)
 > `{name: "kim", gender: "M", phone: "00700", sayHello: ƒ}`
person.sayHello()
 > `Hi! my name is kim`

// arr 인덱스 접근
let arr = [1,2,3,4,5,]
 > `undefined`
typeof arr
> `"object"`
console.log(arr[1])
> `2`
```

```javascript
/* 일치연산자 ===
 - 엄격한 비교, 
 - 메모리의 같은 객체를 가리키고, 같은 타입이고 값도 같다.
 - 일치연산자 사용을 지향함

동등연산자
 - 형변환비교 a= 1, b = '1' / a == b ?
 - 메모리의 같은 객체를 가리키거나 같은 값으 갖도록 변환할 수 있다면 비교
```

```javascript
while (i<10) {
    console.log(i)
    i++
} // 0q부터 9까지 출력
////////////////////////////////
for (let number of [1,2,3,4,5,]) {
    console.log(number)
} // 1부터 5까지 출력
////////////////////////////////

```

```javascript
function add(num1, num2){
    return num1+num2
}
//함수표현방법
const sub = function (num1,num2) {
    return num1 - num2
}

---
// arrow function    
```

