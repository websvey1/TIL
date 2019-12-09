190502 homework_workshop

---

1. Axios 를 사용하는 아래 코드를 완성하시오.
   - Browser 는 axios CDN을 통해, 
   - Node 는 npm install 과 require 를 통해 axios 를 가져와야 합니다.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style>
        img {
            width:300px;
            height:300px;
        }
    </style>
</head>
<body>
    <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
    <script>
    const URL = "https://dog.ceo/api/breeds/image/random"
    axios.get(URL)
	    .then(res => {
            const imgSrc = res.data.message
            return imgSrc
    })
	    .then(imageSource =>{
            console.log(imageSource)
    })
    </script>
</body>
</html>
```

---

workshop

```javascript
const axios = require('axios');

const data = {
    "post": {
        "title": 'title1',
        "content": 'content1',
        "author": 'author1',
    }    
}
url = 'http://13.125.249.144:8080/ssafy/daejeon/2/posts/'

// axios.post(url, data)
//     .then(res => console.log('글이 작성 되었습니다'))
//     .catch(error => console.log('에러가 발생했습니다.'))

axios.get(url) 
.then(res => {
    console.log(res.data.posts)
})
```

