<template>
<v-layout wrap align-center justify-center row fill-height>
  <v-flex xs12 ma-5 text-xs-left>
    <v-layout warp>
      <v-flex xs9>
        <fieldset style="margin-right:4px; height:100%">
          <legend>PICTURE</legend>
          <ImageUpload :random_picture="true" ref="imagePicker"></ImageUpload>
        </fieldset>
      </v-flex>
      <v-flex xs3>
        <fieldset style="margin-left:4px; height:100%;">
          <legend>Project</legend>
          <h2  style="display:flex; justify-content:center; padding:10% 0;">{{ pjtName }}</h2>
        </fieldset>
      </v-flex>
    </v-layout>

    <fieldset>
      <legend>TITLE</legend>
      <div style="margin:0px 16px">
        <v-text-field xs12 label="제목을 입력해 주세요." v-model='title' required></v-text-field>
      </div>
    </fieldset>
    <fieldset>
      <legend>CONTENT</legend>
      <div style="margin:16px;">
        <markdown-editor v-model="content" ref="markdownEditor" required></markdown-editor>
      </div>
    </fieldset>

    <v-layout wrap>
      <v-flex xs9>
        <fieldset style="margin-right:4px; height:100%">
          <legend>TAG</legend>
          <div style="margin:16px;" id="hashtag">
            <HashTag ref="hashtag"></HashTag>
          </div>
        </fieldset>
      </v-flex>
      <v-flex xs3>
        <fieldset style="margin-left:4px; height:100%">
          <legend>VISIBILILTY</legend>
          <div style="margin:16px;">
            <v-radio-group v-model="share">
              <v-radio label="Public" color="primary" value="0"></v-radio>
              <v-radio label="Private" color="error" value="1"></v-radio>
            </v-radio-group>
          </div>
        </fieldset>
      </v-flex>
    </v-layout>

    <div style="text-align:center;" id="write-btn">
      <!-- <v-btn class="v-btn theme--dark" @click="checkValidation">확인</v-btn> -->
      <v-btn class="v-btn theme--dark" @click="writePost">확인</v-btn>
      <v-btn class="v-btn theme--dark" @click="goHome">취소</v-btn>
    </div>

    <Loading :isLoading="isLoading" />

  </v-flex>
</v-layout>
</template>

<script>
import markdownEditor from 'vue-simplemde/src/markdown-editor'
import ImageUpload from "@/components/common/ImageUpload"
import HashTag from "@/components/common/HashTag"
import Loading from "@/components/common/Loading"
import Time from "@/services/Time"

export default {
  name: 'PostWritePage',
  components: {
    markdownEditor,
    ImageUpload,
    HashTag,
    Loading
  },
  data() {
    return {
      title: "",
      project:{},
      // items:[],
      content: "",
      writer: "",
      share:"0",
      isLoading:false,
      pjtName: '',
      category: ''
    }
  },
  created(){                               // 동작이 완벽하지 않음
    if(!this.$session.has("userInfo")){    // POST작성 버튼을 누르면 작성 form이 잠깐 떴다가 다시 뒤로 가짐.
      alert("로그인 해주세요.")               // 수정요망
      this.$router.go(-1)
    }
    else{
      this.getTeamName();
    }
  },
  computed:{
    async form () {
      return {
        user: this.$session.get("userInfo").user_num,
        title: this.title,
        content: this.content,
        share: this.share,
        created_at:Time.getFullDate(),
        category: this.category,
        tags: this.$refs.hashtag.getTagsForDb(),
        imageUrl: await this.$refs.imagePicker.getImageUrl(),
        project: this.$route.params.num
      }
    },
  },
  methods: {
    checkValidation(){
      // if(this.project.project_num == undefined){
      //   alert("프로젝트를 선택해 주세요.")
      //   return false;
      // }
      if(!this.title){
        alert("제목을 입력해 주세요.")
        return false;
      }
      if(!this.content){
        alert("내용을 입력해 주세요.")
        return false;
      }
      if (this.title.length>45){

          alert("제목이 너무 깁니다");
          return false;
        }
      var num ="{}[]()<>?_|~`!@#$%^&*-+\"'\\/";
      console.log(this.title, '중간체크')
      for (var i=0; i<this.title.length; i++){
        for (var j=0; j<num.length; j++){
          if (this.title[i] == num[j]){
            alert("특수문자 사용 금지입니다");
            return false;
          }
        }
      }

      return true;
    },

    async writePost() {
      this.isLoading = true;

      if(this.checkValidation()){
        // project table 가서, 지금 project_num으로 검색하여 category가 0이면, form.category = 0으로 해주자
        var data = {
          pjtNum: this.$route.params.num
        }
        await this.$http.post(this.$store.state.testIp + "/myproject/getCategory", data)
        .then(async(response) => {
          if(response.body[0].project_category == 0){
            this.category = 0
          }else{
            this.category = 1
          }

          var form = await this.form
          await this.$http.post(this.$store.state.testIp + "/post/create", form)
          .then((req) => {
            alert("글이 작성되었습니다.");
            this.isLoading = false;
            this.goHome();
          })
          .catch((error) => {
            this.isLoading = false;
          })
        })
        .catch((error) => {
          console.log(error)
        })
      }
      else{
        this.isLoading = false;
      }
    },
    getTeamName(){
      var data = {
        pjtNum: this.$route.params.num
      }
      this.$http.post(this.$store.state.testIp + '/teamProject/getProjectName', data)
      .then((response) => {
        this.pjtName = response.body[0].project_title
      })
      .catch((error) => {
        console.log(error)
      })
    },
    goHome(){
      this.$router.go(-1);
    }
  }
}
</script>

<style scoped>
@import '~simplemde/dist/simplemde.min.css';

#preview {
  display: flex;
  justify-content: center;
  align-items: center;
}

#preview img {
  max-width: 100%;
  max-height: 200px;
}

#btn {
  float: center;
}
</style>
