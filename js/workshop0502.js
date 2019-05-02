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

axios.get(url) 
.then(res => {
    console.log(res.data.posts)
})