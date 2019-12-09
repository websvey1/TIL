190430 homework_workshop

---

1. JS 는 ES6 이전과 이후로 많은 것이 바뀌었다. ES5 까지는 ‘var ‘키워드로 변수
    를 선언했다면, ES6 이후로는 ‘let’ 과 ‘const’ 키워드가 등장했다.
    ‘let’ 과 ‘const’ 의 차이점과 언제 사용하는지 간략하게 기술하시오.

  ```
  let은 변하는 값, const는 변하지 않는 상수값을 선언할때 씀.(?)
  ------------
  let은 일반적인 변수에 해당한다. 추후에 값이 바뀔것이 확실할 경우 사용
  const는 상수, 언제나 같은 값. 한번 할당되고 않은경우 사용
  ```

  

2. JS 에서는 key – value 로 이루어진 자료구조를 Object 라고 부른다. Object
    와 JSON 의 차이를 간략하게 기술하시오.

  ```
객체 - key:value형식으로 이루어진 자료구조
json -  js객체형식으로 데이터의 구조를 표기하가 위한 단순 문자열
  ```

  

3. 해당 코드에서 ‘Value’ 에 접근하는 두 가지 방법(코드)을 모두 작성하시오

```javascript
const myObject = { key: 'Value' }
1. myObject[key]
2. myObject.key
```

4. 아래 주석에 따라 JS 코드를 작성하시오.

   ```html
   <!DOCTYPE html>
   <html lang="en">
       <head>
           <title>Document</title>
       </head>
       <body>
           <h1>
               Hello World!
           </h1> 
           <script>
               // 1. h1 태그를 선택한 뒤, header 라는 상수에 할당한다.
               let header = document.querySelector('h1')
               // 2. 브라우저 콘솔에 header 안의 내용을 출력한다.
               console.log(header.innerText)
               // 3. header 안의 내용을 'Happy Hacking!' 으로 변경한다. 
               header.innerText = 'Happy Hacking'
           </script>
       </body>
   </html
   ```

   

---

아래 Python 코드를 JS 코드로 변환해보자..
Checkpoint
1. 브라우저는 생각하지 않는다.
2. 변수/함수 이름은 JS naming convention(lowerCamelCase) 을 따른다.
3. F String => Template Literal.

```python
# This is Comment
def concat(str1, str2):
	return f'{str1} - {str2}'
def check_long_str(string):
	if len(string) > 10:
		return True
	else:
		return False
	if check_long_str(concat('Happy', 'Hacking')):
		print('LONG STRING')
	else:
		print('SHORT STRING')
```



```javascript
const concat = function(num1,num2){
    return `${num1} - ${num2}`
}
//위와 같은 함수, arrow function
const concat = (num1, num2) => `${num1}-${num2}`


const check_long_str = function(string) {
    if (string.length >10){       // leng이 아니라 length
        return true            // t가 대문자가 아님
    }else {
        return false          // f도
    }
if (check_long_str(concat('Lee', 'Ho'))){
        console.log('Long string')   // print가 아니라 console.log
    }
else {
        console.log('short stiong')
    }
```



