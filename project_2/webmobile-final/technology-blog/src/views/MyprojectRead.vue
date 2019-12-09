<template>
<div id="top__container" style="
  width: 73%; margin: 0 auto;
  ">
  <v-container>
    <div style="margin-top: 30px;">
      <!-- 사진 -->
      <v-layout wrap fill-height>
      <v-flex>
        <h1 style="text-align:center; padding-bottom:20px;">Project</h1>
        <v-speed-dial style="margin-left: 90%;" v-model="fab" :top="top" :bottom="bottom" :right="right" :left="left" :direction="direction" :open-on-hover="hover" :transition="transition">
        <template v-slot:activator>
          <v-btn v-model="fab" color="blue darken-2" dark fab>
            <v-icon v-if="fab">close</v-icon>
            <v-icon v-else>fas fa-list</v-icon>
          </v-btn>
        </template>
        <v-btn fab dark large color="green" @click="postRead">
          Post <br>보기
        </v-btn>
        <v-btn fab dark large color="indigo" @click="postWrite">
          Post <br>작성
        </v-btn>
        <v-btn fab dark large color="red" @click="todo()">
          To do <br>List
        </v-btn>
      </v-speed-dial>

      </v-flex>
    </v-layout>
      <v-carousel hide-delimiters style="
      width:50%; height:45%; float:left; margin-top: 3px;
      ">
        <v-carousel-item v-for="image in images" :key="image.imgnum" :src="image.imgurl"></v-carousel-item>
      </v-carousel>


      <!-- 상세 -->
      <v-layout wrap align-center justify-center row fill-height style="
      width:47%; height:50%; float:right;
      ">
        <v-flex wrap>
          <fieldset style="margin-right:4px; height:80%; padding:10px 15px;">
            <!-- <legend style="text-align:right; padding-bottom:10px;"><h1>&nbsp;Project&nbsp;</h1></legend> -->
            <div style="margin:15px 20p;">
              <h2 style="padding:5px 0;">Title</h2>
              <p style="font-size: 16px;">{{ project.project_title }}</p>

              <h2 style="padding:5px 0;">Goal</h2>
              <p style="font-size: 16px;">{{ project.project_goal }}</p>

              <h2 style="padding:5px 0;">Term</h2>
              <v-menu v-model="menu" bottom right transition="scale-transition" origin="top left">
                <template v-slot:activator="{ on }">
                  <v-chip pill v-on="on" style="margin-left: -2px;" color="#FFCDD2">
                    <v-icon left>event</v-icon>
                    <span style="cursor: pointer; font-size: 14px;"><b>{{ project.project_start_date }} ~ {{ project.project_end_date }}</b></span>
                  </v-chip>
                </template>
                <v-layout justify-center>
                  <v-date-picker v-model="picker" readonly multiple no-title :show-current="false" locale="ko-kr"></v-date-picker>
                </v-layout>
              </v-menu>
              <br>

              <h2>Status</h2>
                <v-chip color="#E1BEE7" style="margin-left: -2px;">
                  <span style="font-size: 13.5px;"><b>{{ project.project_status }}</b></span>
                </v-chip>
              <br>

              <br>
              <h2>Tech</h2>
              <p>{{ project.project_tech }}</p>

              <v-btn fab dark small color="#F57F17" style="float: right;" @click="dialog = true">
                <v-icon dark>add</v-icon>
              </v-btn>
            </div>
          </fieldset>
        </v-flex>
      </v-layout>
    </div>

    <v-layout wrap align-center justify-center row fill-height style="clear:both; padding-top:20px;">
      <v-flex>
        <fieldset style="padding:10px 15px; height:80%">

          <h2 style="padding:10px 0;">Content</h2>
          <p>{{ project.project_content }}</p>

        </fieldset>
      </v-flex>
    </v-layout>

    <v-dialog hide-overlay v-model="dialog" persistent max-width="520px">
      <v-card>
        <v-card-title style="display:flex; justify-content:center;">
        <h2> Detail Information </h2>
      </v-card-title>
      <v-card-text style="text-align:center;" >
        <v-container grid-list-md style="display:flex; justify-content:center;">
          <v-layout wrap>
            <v-flex xs12>
              - 프로젝트 생성일 : {{ created }}<br>
              - 프로젝트 최종 수정일 : {{ modified }}<br>
              - Git-url : {{ project.project_git_url }}<br>
              - Tech : {{ project.project_tech }}
            </v-flex>
          </v-layout>
        </v-container>
      </v-card-text>
      <v-card-actions style="display:flex; justify-content:center;">
      <!-- <v-spacer></v-spacer> -->
        <v-btn color="blue darken-1" flat @click="dialog = false">OK!</v-btn>
      </v-card-actions>
      </v-card>
    </v-dialog>

<!-- /////////////// ///////////////////////////// -->
    <v-layout wrap align-center justify-center row fill-height style="clear:both; padding-top:20px;">
      <v-flex>
        <fieldset style="padding:10px 15px; height:80%">
          <h2 style="padding:10px 0;">Post</h2>
          <ul v-for="post in posts" :key="post">
            <li><a @click="postMove(post)">{{ post.post_title }} / {{ post.user_name }} / {{ post.post_updated_at.split(' ')[0] }}</a></li>
          </ul>
        </fieldset>
      </v-flex>
    </v-layout>

    <div style="text-align:center; margin-top: 20px;" id="write-btn">
      <v-btn v-if="project.project_user === loginUser" class="v-btn theme--dark" @click="goUpdate">수정</v-btn>
      <v-btn v-if="project.project_user === loginUser" class="v-btn theme--dark" @click="goDelete">삭제</v-btn>
      <v-btn class="v-btn theme--dark" @click="goHome">목록</v-btn>
    </div>

  </v-container>
</div>
</template>

<script>
import ImageUpload from "@/components/common/ImageUpload"

export default {
  name: 'MyprojectRead',
  components: {
    ImageUpload
  },
  data() {
    return {
      project: [],
      images: null,
      modify: false,
      menu: false,
      picker: [],
      posts: [],
      direction: 'left',
      fab: true,
      fling: false,
      hover: false,
      tabs: null,
      top: false,
      right: false,
      bottom: true,
      left: true,
      transition: 'slide-y-reverse-transition',
      loginUser: this.$session.get('userInfo').user_num,
      loginName: this.$session.get('userInfo').user_name,
      chk: 0,
      dialog: false,
      created: '',
      modified: ''
    }
  },
  mounted() {
    var id = this.$route.params.id;
    this.$http.get(this.$store.state.testIp + '/myproject/' + id)
      .then((res) => {
        // console.log(res)
        this.project = res.data.project[0];
        if(!this.$session.has("userInfo") || this.$session.get("userInfo").user_num != this.project.project_user){
          alert("권한이 없습니다.");
          this.$router.push("/");
        }
        else{
          this.created = this.project.project_created_at.substring(0, 10)
          this.modified = this.project.project_updated_at.substring(0, 10)
          this.images = res.data.images;
          this.picker.push(res.data.project[0].project_start_date)
          this.picker.push(res.data.project[0].project_end_date)
        }
      });
    // console.log(this.$session.get('userInfo').user_num)
    this.getPostList()
  },
  methods: {
    todo(){
      this.$router.push(`/todolist/${this.$route.params.id}`)
    },
    getPostList(){
      var data = {
        num : this.$route.params.id
      }
      this.$http.post(this.$store.state.testIp + '/myproject/getPost', data)
      .then((response) => {
        this.posts = response.body
      })
      .catch((error) => {
        console.log(error)
      })
    },
    goHome() {
      this.$router.push("/myproject")
    },
    goUpdate() {
      var id =this.$route.params.id;
      this.$router.push(`/myproject/update/${id}`)
    },
    goDelete() {
      var id = this.$route.params.id;
      var data = {
        pjtNum: id
      }
      // console.log(data)
      this.$http.post(this.$store.state.testIp + '/myproject/delete/project', data)
      .then((res) => {
        alert("글 삭제 완료");
        // console.log(res)
        this.$router.push('/myproject')
      })
    },
    postMove(post){
      var num = post.post_num;

      this.$router.push({
        name: "PostReadPage",
        params: {
          id: num,
          user: post.user_id,
          share: post.post_share,
          route: 'ProjectRead'
        }
      })
    },
    postWrite(){
      // this.$router.push({ name: "PostCreatePage", params: {id: this.$route.params.id, num: this.$route.params.num} })
      this.$router.push(`/post/create/${this.$route.params.id}`)
    },
    postRead(){
      // this.$router.push({ name: "TeamPostPage", params: {id: this.$route.params.id, num: this.$route.params.num} })
      this.$router.push(`/myPostPage/${this.$route.params.id}`)
    }
  }
}
</script>

<style scoped>
v-container {
  max-width: 100px !important;
}

.container {
  padding-top: 10px !important;
}

#preview {
  display: flex;
  justify-content: center;
  align-items: center;
}

#preview img {
  max-width: 50%;
  max-height: 200px;
}

#btn {
  float: center;
}
</style>
