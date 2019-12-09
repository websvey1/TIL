<template>
<v-hover>
  <v-card slot-scope="{ hover }" :class="`elevation-${hover ? 12 : 2}`" class="rounded-card" @dblclick="goReadPage(post)">
    <v-img v-if="post.image_url != null" height="230px" :src="post.image_url" aspect-ratio="2.75"></v-img>
    <v-img v-else height="230px" src="https://source.unsplash.com/random/300x300" aspect-ratio="2.75"></v-img>

    <v-card-title primary-title>
      <h3 class="headline mb-0 oneline">
        <i v-if="post.post_share=='1'"><img src="@/assets/lock.png/" style="width:20px; height:20px; margin-right:5px;"/></i>
        {{post.post_title}}</h3>
    </v-card-title>
    <v-card-text>
      <p v-if="post.post_share==1" class="secret_board"> (비밀글입니다.) </p>
      <p v-else class="fourline"> {{post.post_content}} </p>

      <v-list-tile avatar @click="" style="overflow:hidden; width:300px;">
        <v-list-tile-avatar class="hidden-xs-only">
          <v-img v-if="post.user_image" :src="post.user_image"></v-img>
          <v-img v-else src="https://t1.daumcdn.net/cfile/tistory/2513B53E55DB206927"></v-img>
        </v-list-tile-avatar>

        <v-list-tile-content>
          <v-list-tile-title ><span class="oneline">{{post.post_created_at}}  </span></v-list-tile-title>
          <v-list-tile-sub-title class="oneline">{{post.user_name}}</v-list-tile-sub-title>
        </v-list-tile-content>
      </v-list-tile>
    </v-card-text>
  </v-card>

</v-hover>
</template>

<script>
import router from '@/router'

export default {
  name: 'PostCard',
  data() {
    return {
      isActive: false,
    }
  },
  props: {
    post: {}
  },
  mounted(){
    // console.log(this.$props.post);
  },
  methods: {
    toggle: function() {
      this.isActive = !this.isActive
    },

    goReadPage(post) {
      var postNum = post.post_num;
      router.push({
        name: "PostReadPage",
        params: {
          id: postNum,
        }
      })
    }
  }
}
</script>

<style media="screen" scoped>
.rounded-card {
  border-radius: 30px !important;
  overflow: hidden;
}

.visibility-1 {
  background: white !important;
}

.visibility-2 {
  background: #BBB !important;
}

.oneline {
  display: inline-block;
  overflow: hidden;
  text-overflow: hidden;
  /* 여러 줄 자르기 추가 스타일 */
  white-space: normal;
  line-height: 1.2;
  height: 1.2em;
  text-align: left;
  word-wrap: break-word;
  display: -webkit-box;
  -webkit-line-clamp: 1;
  -webkit-box-orient: vertical;
}
.secret_board {
  font-style: italic;
  color: gray;
  display: inline-block;
  overflow: hidden;
  text-overflow: ellipsis;
  /* 여러 줄 자르기 추가 스타일 */
  white-space: normal;
  line-height: 1.5;
  height: 6em;
  text-align: left;
  word-wrap: break-word;
  display: -webkit-box;
  -webkit-line-clamp: 4;
  -webkit-box-orient: vertical;
}
.fourline {
  display: inline-block;
  overflow: hidden;
  text-overflow: ellipsis;
  /* 여러 줄 자르기 추가 스타일 */
  white-space: normal;
  line-height: 1.5;
  height: 6em;
  text-align: left;
  word-wrap: break-word;
  display: -webkit-box;
  -webkit-line-clamp: 4;
  -webkit-box-orient: vertical;
}
</style>
