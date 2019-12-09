 <template>
  <div class="post-container" v-if="post.post_share=='0'">
    <span class="published">
      <v-chip
        v-if="post.post_category == '0'"
        small
        color="#FFD54F">
        <b>personal</b>
      </v-chip>
      <v-chip
        v-else
        small
        color="#FF8A65">
        <b>Team</b>
      </v-chip>
      <p class="date">
        {{ post.post_created_at | date}}
        <br>
        {{ post.post_created_at | time}}
      </p>
    </span>
    <div class="post">
      <img v-if="post.image_url != null" :src="post.image_url"/>
      <img v-else src="https://source.unsplash.com/random/300x300"></img>

      <a @click="goReadPage(post)">
        <br>
        <h1 class="posth1">
          <i v-if="post.post_share=='1'"><img src="@/assets/lock.png/" style="width:20px; height:20px; margin-right:10px;"/></i>
          <i v-if="post.post_share=='1'" class="fas fa-lock">&nbsp;&nbsp;</i>
          {{ post.post_title}}
        </h1>
      </a>
      <p class="pcontent">{{ post.post_content | content }}</p>
      <v-divider style="margin-left:170px"></v-divider>
      <p class="puser">{{post.project_title|project}} {{post.user_name|name}}
        <v-avatar v-if="post.user_image"><img style="height:30px; width:30px; margin:0px;" :src="post.user_image"></img></v-avatar>
        <v-avatar v-else><img style="height:30px; width:30px; margin:0px;" src="https://t1.daumcdn.net/cfile/tistory/2513B53E55DB206927"></img></v-avatar>
      </p>
    </div>
  </div>
  <div class="post-container" v-else>
    <span class="published">
      <v-chip
        v-if="post.post_category == '0'"
        small
        color="#FFD54F">
        <b>personal</b>
      </v-chip>
      <v-chip
        v-else
        small
        color="#FF8A65">
        <b>Team</b>
      </v-chip>
      <p class="date">
        {{ post.post_created_at | date}}
        <br>
        {{ post.post_created_at | time}}
      </p>
    </span>
    <div class="post">
      <img v-if="post.image_url != null" :src="post.image_url"/>
      <img v-else src="https://source.unsplash.com/random/300x300"></img>

      <a @click="goReadPage(post)">
        <br>
        <h1 class="posth1">
          <i v-if="post.post_share=='1'"><img src="@/assets/lock.png/" style="border-radius:0; width:30px; height:30px; margin-top: 2px; margin-right: 8px;"/></i>
          <!-- <i v-if="post.post_share=='1'" class="fas fa-lock">&nbsp;&nbsp;</i> -->
          {{ post.post_title}}
        </h1>
      </a>
      <p class="pcontent">비밀 글입니다.</p>
      <v-divider style="margin-left:170px"></v-divider>
      <p class="puser">{{post.project_title|project}} {{post.user_name|name}}
        <v-avatar v-if="post.user_image"><img style="height:30px; width:30px; margin:0px;" :src="post.user_image"></img></v-avatar>
        <v-avatar v-else><img style="height:30px; width:30px; margin:0px;" src="https://t1.daumcdn.net/cfile/tistory/2513B53E55DB206927"></img></v-avatar>
      </p>
    </div>
  </div>
 </template>

<script>
import router from '@/router'

export default {
  name: 'PostDownCard',
  data: () => ({}),
  props: {
    post: {}
  },
  mounted() {
    // console.log(this.$props.post);
  },
  methods: {
    goReadPage(post) {
      // console.log(postNum);

      var postNum = post.post_num;
      router.push({
        name: "PostReadPage",
        params: {
          id: postNum,
        }
      })
    }
  },
  filters: {
    date(v) {
      if (v != undefined) {
        return v.split(' ')[0];
      } else {
        return v;
      }
    },
    time(v) {
      if (v != undefined) {
        return v.split(' ')[1];
      } else {
        return v;
      }
    },
    content(v) {
      return '"' + v + '"'
    },
    name(v) {
      return "작성자 - " + v;
    },
    project(v) {
      if (v == undefined) {
        return "";
      }
      return v + " | ";
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
  padding-left: 75px;
}

.published {
  position: absolute;
  width: 100px;
  left: 25px;
  padding: 7px 0;
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
  padding-bottom: 40px;
  margin: 0 auto;
  border-left: 1px solid #999;
  min-height: 180px;
}

/* .post-container:last-child .post {
    padding-bottom: 60px;
} */

.posth1 {
  /* padding-top: 10px; */
  font-family: Open Sans;
  font-weight: bold;
  color: #222;
  font-size: 30px;
  padding-left: 10px;
  /* margin: 0; */
  margin-top: 7px;
  margin-bottom: 7px;
  text-transform: uppercase;
  /* 여러 줄 자르기 추가 스타일 */
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: normal;
  line-height: 1.2;
  height: 1.2em;
  text-align: left;
  word-wrap: break-word;
  display: -webkit-box;
  -webkit-line-clamp: 1;
  -webkit-box-orient: vertical;
}

.pub-date {
  font-family: Open Sans;
  color: #666;
  font-size: 12px;
}

.post img {
  width: 140px;
  height: 140px;
  border-radius: 9999px;
  float: left;
  margin-right: 15px;
  margin-top: 13px;
}

.pcontent {
  padding-left: 13px;
  padding-top: 15px;
  font-family: Open Sans;
  color: #333;
  line-height: 1.6;
  min-height: 90px;
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

.puser {
  padding-left: 25px;
  font-family: Open Sans;
  color: #333;
  line-height: 1.6;
  margin-top: 0;
  text-overflow: ellipsis;
  /* 여러 줄 자르기 추가 스타일 */
  white-space: normal;
  /* height: 4.5em; */
  text-align: right;
  word-wrap: break-word;
  display: -webkit-box;
  -webkit-line-clamp: 1;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

p {
  margin-bottom: 0px !important;
}
</style>
