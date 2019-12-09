<template>
<div style="background-color: white;">
  <v-layout wrap row pa-4> 
      <v-flex fill-height d-flex xs12>
        <div class="container">
            <h1 style="display:inline;">{{ pjtName }}</h1>
            <v-divider></v-divider>
            <PostDownList :posts="posts" :category="'2'" ref="post"></PostDownList>
        </div>
      </v-flex>
      <v-flex xs12 text-xs-center>
         <v-pagination v-model="page" :length="length" :total-visible="totalVisible"></v-pagination>
       </v-flex>
    </v-layout>
</div>
</template>
<script>
import PostList from '@/components/post/PostList'
import PostDownList from '@/components/post/PostDownList'

export default {
  name: 'MyPostPage',
  components: {
    PostList,
    PostDownList,
  },
  data() {
    return {
      posts:[],
      page: 1,
      length: 1,
      totalVisible: 7,
      pjtName: ''
    }
  },
  watch: {
    async page(v) {
        await this.readPosts(v - 1);
    },
  },
  async created() {
    if (this.$session.has('userInfo')) {
      await this.getProjectName();
      await this.readPosts(this.page - 1);
      await this.getTotalPageNum();
    } else {
      alert("로그인 해주세요.");
      this.$router.push("/");
    }
  },
  mounted() {
      // console.log(this.$route.params.num)
  },
  methods: {
    async getProjectName(){
      await this.$http.post(this.$store.state.testIp + '/myproject/getProjectName', {pjtNum: this.$route.params.num})
      .then((response) => {
        this.pjtName = response.body[0].project_title
      })
      .catch((error) => {
        console.log(error)
      })
    },
    allPosts(){
        this.page = 1;
    },

    async readPosts(page) {
      await this.$http.post(this.$store.state.testIp + "/post/teamAllList/" + page, {pjtNum:this.$route.params.num})
      .then((response) => {
        this.posts = response.data;
      })
      .catch((error) => {
        console.log(error);
      })
    },

    async getTotalPageNum() {
      await this.$http.post(this.$store.state.testIp + "/post/teamPageNum", {pjtNum:this.$route.params.num})
        .then((req) => {
          console.log(req.data);
          this.length = req.data * 1;
        })
    }
  },
  beforeRouteLeave(to, from, next) {
    next();
  },
  destroyed() {

  }
}
</script>
<style scoped>
#page {
  background-color: white;
  width: 90%;
  height: 100%;
  margin: 0 auto;
}

.searchbar-total {
  display: flex;
  justify-content: center;
  padding-top: 40px;
  padding-bottom: 20px;
  /* background-color: rgba(9,9,9,0.1); */
}

.container h1 {
  margin-left: 50px;
}

.searchbar-first {
  float: left;
  display: inline-block;
  margin: 5px;
  max-width: 150px;
}

.searchbar-second {
  float: left;
  display: inline-block;
  margin: 5px;

}

.searchbar-third {
  float: left;
  display: inline-block;
  margin: 5px 0px;
  vertical-align: center;

}

.searchBtn {
  border-radius: 5%;
  /* font-weight:bold; */
  color: rgb(0, 0, 0);
  background-color: rgb(156, 156, 156);
  text-align: center;
}
</style>
