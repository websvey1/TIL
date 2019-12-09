<template>
<v-layout v-if="posts.length > 0" v-dragscroll class="overflow">
  <v-flex xs3 v-for="post in posts" px-2 py-4>
    <PostCard :post="post"></PostCard>
  </v-flex>
</v-layout>
<v-layout v-else wrap>
  <v-flex xs12 px-2 mt-4 style="margin-bottom: 35px;">
    <h1 style="margin-top:50px;text-align:center;">POST가 없습니다.</h1>
  </v-flex>
</v-layout>
</template>

<script>
import PostCard from "@/components/post/PostCard"

import {
  dragscroll
} from 'vue-dragscroll'

export default {
  name: "PostList",
  components: {
    PostCard
  },
  directives: {
    'dragscroll': dragscroll
  },
  data() {
    return {
      posts:[]
    }
  },
  filter: {

  },
  methods: {
    isVisible(post) {
      if (post.post_share == '0' || (this.$store.state.userInfo != null && post.post_share == '1' && post.email == this.$store.state.userInfo.email)) {
        return true;
      } else {
        return false;
      }
    },

    async readPosts() {
      var posts = await this.$http.get(this.$store.state.testIp + "/post")
        .then((response) => {
          // console.log(response.data);
          this.posts = response.data;
        })
        .catch((error) => {
          console.log(error);
        })
    }
  },
  mounted() {
    this.readPosts();
  }
}
</script>

<style media="screen" scoped>
.overflow {
  overflow-x: auto;
  overflow-y: hidden;
}

.overflow::-webkit-scrollbar {
  display: none;
}
</style>
