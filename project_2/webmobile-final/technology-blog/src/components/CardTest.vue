 <template>
  <div class="post-container">
    <span class="published">
      <span class="date">
        {{ post.wdate }}
      </span>
    </span>
    <div class="post">
      <a @click="goReadPage(post.key)"><h1 class="posth1">{{ post.title}} <i v-if="post.visibility=='false'" class="fas fa-lock">&nbsp;&nbsp;</i></h1></a>
      <img :src="post.imageUrl"/>
      <p class="ptag">{{ post.content }}</p>
    </div>
  <!-- <br>
  <br>
  <hr style="width: 95%; margin: auto;"> -->
  </div>
 </template>

<script>
import router from '@/router'

export default {
    name: 'CardTest',
    data: () => ({
    }),
    props: {
        post: {}
    },
    methods: {
        goReadPage(postNum, email){
        console.log(postNum);
        router.push({name:"PostReadPage", params:{id:postNum}})
    }
    }
  }
</script>

<style scoped>
@import url(https://fonts.googleapis.com/css?family=Jura:300,400,500,600);
@import url(https://fonts.googleapis.com/css?family=Play);
@import url(https://fonts.googleapis.com/css?family=Open+Sans:400,300);

.logo {
  float: left;
}

.post-container {
  position: relative;
  padding-left: 50px;
}

.published {
  position: absolute;
  width: 50px;
  left: 25px;
  padding: 10px 0;
  text-align: center;
  background-color: #fff;
}

.date {
  text-transform: uppercase;
  font-family: Open Sans;
  font-weight: bold;
  color: #222;
  font-size: 12px;
}

.post {
  padding-left: 50px;
  padding-bottom: 60px;
  margin: 0 auto;
  border-left: 1px solid #999;
}

.post-container:last-child .post {
    padding-bottom: 60px;
}

.posth1 {
  /* padding-top: 3px; */
  font-family: Open Sans;
  font-weight: bold;
  color: #222;
  font-size: 30px;
  margin: 0;
  margin-bottom: 15px;
  text-transform: uppercase;
   /* 여러 줄 자르기 추가 스타일 */
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: normal;
  line-height: 1.2;
  height:1.2em;
  text-align: left;
  word-wrap: break-word;
  display: -webkit-box;
  -webkit-line-clamp: 1;
  -webkit-box-orient: vertical ;
}

.pub-date {
  font-family: Open Sans;
  color: #666;
  font-size: 12px;
}

.post img {
  width: 100px;
  height: 100px;
  border-radius: 9999px;
  float: left;
  margin-right: 15px;
  margin-top: 5px;
}

.ptag {
  padding-top: 10px;
  font-family: Open Sans;
  color: #333;
  line-height: 1.6;
  font-size: 18px;
  margin-top: 0;
  text-overflow: ellipsis;
  /* 여러 줄 자르기 추가 스타일 */
  white-space: normal;
  /* height: 4.5em; */
  text-align: left;
  word-wrap: break-word;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

</style>
