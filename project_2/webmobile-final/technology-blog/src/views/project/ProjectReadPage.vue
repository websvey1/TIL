<template>
<div id="top__container" style="
  width: 73%; margin: 0 auto;
  ">
  <v-container>
    <div style="margin-top: 20px;">
      <!-- 사진 -->
      <v-layout wrap fill-height>
        <v-flex  style="margin-bottom: 50px;">
          <h1 style="text-align: center">Project</h1>

          <!-- <v-btn round outline color="black" @click="todo()" style="margin-left: 85%; margin-bottom: 20px; font-size:13px; height:40px; ">
             <div style="color:black; font-weight:bolder;">todo list</div><img src="@/assets/todo2.png/" style="width:30px; margin-left:10px;"/>
          </v-btn> -->
        </v-flex>
      </v-layout>

      <v-carousel hide-delimiters style="
      width:50%; float:left; margin-top: 3px;
      ">
        <v-carousel-item v-for="image in images" :key="image.imgnum" :src="image.imgurl"></v-carousel-item>
      </v-carousel>

      <!-- 상세 -->
      <v-layout wrap align-center justify-center row fill-height style="
      width:47%; float:right;
      ">
        <v-flex wrap>
          <fieldset wrap style="margin-right:4px; height: 100%; padding:20px 5px 15px;">
            <!-- <legend style="text-align:right; padding-bottom:10px;"><h1>&nbsp;Project&nbsp;</h1></legend> -->
            <div style="margin:0 20px;">
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
              <!-- <v-btn rounded color="warning" dark>{{ project.project_status }}</v-btn> -->
              <br>

              <br>
              <h2>Tech</h2>
              <p>{{ project.project_tech }}</p>

              <v-btn fab dark small color="indigo" style="float: right; margin-top: -8px;" @click="dialog = true">
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
              - 프로젝트 생성일 : {{ project.project_created_at.substring(0, 10) }}<br>
              - 프로젝트 최종 수정일 : {{ project.project_updated_at.substring(0, 10) }}<br>
              - Tech : {{ project.project_tech }}<br>
              - Git-url : {{ project.project_git_url }}
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
  name: 'ProjectReadPage',
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
      loginUser: null,
      dialog: false
    }
  },
  mounted() {
    var id = this.$route.params.id;
    this.$http.get(`http://192.168.31.61:3000/myproject/${id}`)
      .then((res) => {
        this.project = res.data.project[0];
        this.images = res.data.images;
        this.loginUser = this.$session.get('userInfo').user_num;
        this.picker.push(res.data.project[0].project_start_date)
        this.picker.push(res.data.project[0].project_end_date)
      });
  },
  methods: {
    todo() {
      this.$router.push(`/todolist/${this.$route.params.id}`)
    },
    goHome() {
      this.$router.push("/project")
    },
    goUpdate() {
      var id = this.$route.params.id;
      this.$router.push(`/myproject/update/${id}`)
    },
    goDelete() {
      var id = this.$route.params.id;
      var data = {
        pjtNum: id
      }
      console.log(data)
      this.$http.post(this.$store.state.testIp + '/myproject/delete/project', data)
        .then((res) => {
          alert("글 삭제 완료");
          console.log(res)
          this.$router.push('/myproject')
        })
    }
  }
}
</script>

<style scoped>
v-container {
  max-width: 100px !important;
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
