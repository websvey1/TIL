<template>
<div id="top__container" style="width: 90%; margin: 0 auto;">
  <v-container>
    <div style="margin-top: 20px;">
      <!-- 사진 -->
      <v-layout wrap fill-height>
      <v-flex>
        <h1 style="text-align: center">Project</h1>
        <v-speed-dial style="margin-left: 90%;" v-model="fab" :top="top" :bottom="bottom" :right="right" :left="left" :direction="direction" :open-on-hover="hover" :transition="transition">
        <template v-slot:activator>
          <v-btn v-model="fab" color="blue darken-2" dark fab>
            <v-icon v-if="fab">close</v-icon>
            <v-icon v-else>fas fa-list</v-icon>
          </v-btn>
        </template>
        <v-btn fab dark large color="green" @click="postRead">
          Post<br>보기
        </v-btn>
        <v-btn fab dark large color="indigo" @click="postWrite">
          Post<br>작성
        </v-btn>
        <v-btn fab dark large color="red" @click="todo()">
          To do<br>List
        </v-btn>
      </v-speed-dial>
      </v-flex>
    </v-layout>

    <v-carousel hide-delimiters style="width: 50%; float:left; margin-top: 3px;">
      <v-carousel-item v-for="(image, i) in images" :key="i" :src="image.image_url"></v-carousel-item>
    </v-carousel>
  <!-- 상세 -->
    <v-layout wrap align-center justify-center row fill-height style="
      width:47%; height:50%; float:right;">
      <v-flex wrap>
        <fieldset style="margin-right:4px; height:100%; padding:10px 15px;">
          <!-- <legend style="text-align:right; padding-bottom:10px;"><h1>&nbsp;Project&nbsp;</h1></legend> -->
          <div style="margin:15px 20p;">
            <h2 style="padding:5px 0;">Title</h2>
            <p>{{ project.project_title }}</p>
            <h2 style="padding:5px 0;">Goal</h2>
            <p>{{ project.project_goal }}</p>
            <h2 style="padding:5px 0;">Term</h2>
            <v-menu v-model="menu" bottom right transition="scale-transition" origin="top left">
              <template v-slot:activator="{ on }">
                <v-chip pill v-on="on">
                  <v-icon left>event</v-icon>
                  <span style="cursor: pointer">{{ project.project_start_date }} ~ {{ project.project_end_date }}</span>
                </v-chip>
              </template>
              <v-layout justify-center>
                <v-date-picker v-model="picker" no-title :show-current="false" locale="ko-kr"></v-date-picker>
              </v-layout>
            </v-menu>
            <br>

            <h2>Status</h2>
            <v-chip color="green" dark>{{ project.project_status }}</v-chip>
            <br>
            <br>
            <h2>Member</h2>
            <span v-for="member in members" :key="member">
              <v-chip v-if="project.project_captain == member" color="primary" style="display: inline-block" dark>{{ member }}</v-chip>
              <v-chip v-else color="rgb(191, 234, 255)" style="display: inline-block">{{ member }}</v-chip>
            </span>
            <br>
            <v-btn fab small dark color="indigo" style="float: right;" @click="dialog = true">
              <v-icon dark>add</v-icon>
            </v-btn>
          </div>
        </fieldset>
        </v-flex>
      </v-layout>
    </div>

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

    <v-layout wrap align-center justify-center row fill-height style="clear:both; padding-top:20px;">
      <v-flex>
        <fieldset style="padding:10px 15px; height:80%">
          <h2 style="padding:10px 0;">Content</h2>
          <p>{{ project.project_content }}</p>
        </fieldset>
      </v-flex>
    </v-layout>
<!-- /////////////// ///////////////////////////// -->
    <v-layout wrap align-center justify-center row fill-height style="clear:both; padding-top:20px;">
      <v-flex>
        <fieldset style="padding:10px 15px; height:80%">
          <h2 style="padding:10px 0;">Post</h2>
          <ul v-for="post in posts">
            <li><a @click="postMove(post)">{{ post.post_title }} / {{ post.user_name }} / {{ post.post_updated_at.split(' ')[0] }}</a></li>
          </ul>
        </fieldset>
      </v-flex>
    </v-layout>
<!-- /////////////// ///////////////////////////// -->
    <div style="text-align:center; margin-top: 20px;" id="write-btn">
      <v-btn v-if="chk === 1" class="v-btn theme--dark" @click="goUpdate">수정</v-btn>
      <v-btn v-if="loginName === project.project_captain" class="v-btn theme--dark" @click="goDelete">삭제</v-btn>
      <v-btn class="v-btn theme--dark" @click="goHome">목록</v-btn>
    </div>
  </v-container>
</div>
</template>

<script>
export default {
  name: 'TeamProejctReadPage',
  data(){
    return {
      project: [],
      images: [],
      modify: false,
      menu: false,
      picker: new Date().toISOString().substr(0, 10),
      members: null,
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
  computed: {
    activeFab () {
      switch (this.tabs) {
        case 'one': return { class: 'purple', icon: 'account_circle' }
        case 'two': return { class: 'red', icon: 'edit' }
        case 'three': return { class: 'green', icon: 'keyboard_arrow_up' }
        default: return {}
      }
    },
  },
  watch: {
    top (val) {
      this.bottom = !val
    },
    right (val) {
      this.left = !val
    },
    bottom (val) {
      this.top = !val
    },
    left (val) {
      this.right = !val
    },
  },
  mounted() {
    this.getProject()
    this.getImage()
    this.getMember()
    this.getPostList()
    // console.log(this.$session.get('userInfo').user_name)
  },
  methods: {
    todo(){
      this.$router.push(`/todolist/${this.$store.state.pn}`)
    },
    postMove(post){
      // this.$router.push(`/post/read/${num}`)
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
    getPostList(){
      var data = {
        num : this.$route.params.num
      }
      this.$http.post(this.$store.state.testIp + '/teamProject/getPost', data)
      .then((response) => {
        this.posts = response.body
      })
      .catch((error) => {
        console.log(error)
      })
    },
    getImage() {
      var data = {
        pjtNum: this.$route.params.num
      }
      this.$http.post(this.$store.state.testIp + '/teamProject/getimage', data)
      .then((res) => {
        this.images = res.body
      })
    },
    getProject() {
        var team_num = this.$route.params.id
        var pjt_num = this.$route.params.num

        var data = {
            teamNum: team_num,
            pjtNum: pjt_num
        }
        this.$http.post()
        this.$http.post(this.$store.state.testIp + '/teamProject/getproject', data)
        .then((res) => {
            this.project = res.body[0]
            this.created = this.project.project_created_at.substring(0, 10)
            this.modified = this.project.project_updated_at.substring(0, 10)
            // console.log(this.project)
        })
    },
    getMember() {
        var data = {
            teamNum: this.$route.params.id
        }
        this.$http.post(this.$store.state.testIp + '/team/getMember', data)
        .then((res) => {
            var member = []
            for (var i=0; i < res.body.length; i++) {
                var name = res.body[i].user_name
                member.push(name)
                // console.log(this.loginUser)
                // console.log(name)
                if (this.loginName === name) {
                  this.chk = 1
                }
            }
            this.members = member
        })
    },
    goHome() {
        var teamNum = this.$route.params.id
        this.$router.push(`/teamProject/${teamNum}`)
    },
    goUpdate() {
        var teamNum = this.$route.params.id
        var pjtNum = this.$route.params.num // 이걸 어디서 받아오는걸까.
        this.$router.push(`/teamProject/${teamNum}/update/${pjtNum}`)
    },
    goDelete() {
      var teamNum = this.$route.params.id
      var data = {
        pjtNum: this.$route.params.num
      }
      this.$http.post(this.$store.state.testIp + '/teamProject/delete/project', data)
      .then((res) => {
        alert("글 삭제 완료");
        this.$router.push(`/teamProject/${teamNum}`)
      })
    },
    postWrite(){
      // this.$router.push({ name: "PostCreatePage", params: {id: this.$route.params.id, num: this.$route.params.num} })
      this.$router.push(`/post/create/${this.$route.params.num}`)
    },
    postRead(){
      // this.$router.push({ name: "TeamPostPage", params: {id: this.$route.params.id, num: this.$route.params.num} })
      this.$router.push(`/teamPostPage/${this.$route.params.num}`)
    }
  }
}
</script>
<style scoped>
#create .v-speed-dial {
  position: absolute;
}

#create .v-btn--floating {
  position: relative;
}
</style>
