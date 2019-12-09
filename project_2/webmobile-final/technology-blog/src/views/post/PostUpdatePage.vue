<template>
<v-layout wrap align-center justify-center row fill-height>
  <v-flex xs12 ma-5 text-xs-left v-if="post != null">
    <v-layout warp>
      <v-flex xs9>
        <fieldset style="margin-right:4px; height:100%">
          <legend>PICTURE</legend>
          <ImageUpload :random_picture="true" ref="imagePicker"></ImageUpload>
        </fieldset>
      </v-flex>
      <v-flex xs3>
        <fieldset style="margin-left:4px; height:100%">
          <legend>Project</legend>
          <div style="margin:16px;">
            <v-select
            style="margin:0 auto;"
            v-model="project"
            :items="items"
            item-text="project_title"
            :hint="`${project.team_name == undefined ? '' : '팀 이름 : ' + project.team_name} ${project.project_status == undefined ? '프로젝트를 선택해 주세요.' : ' ['+ project.project_status +']'}`"
            label="Project"
            return-object
            persistent-hint
            single-line
            ></v-select>
          </div>
        </fieldset>
      </v-flex>
    </v-layout>
    <fieldset>
      <legend>TITLE</legend>
      <div style="margin:0px 16px">
        <v-text-field xs12 label="제목을 입력해 주세요." v-model='post.post_title'></v-text-field>
      </div>
    </fieldset>
    <fieldset>
      <legend>CONTENT</legend>
      <div style="margin:16px;">
        <markdown-editor v-model="post.post_content" ref="markdownEditor"></markdown-editor>
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
            <v-radio-group v-model="post.post_share">
              <v-radio label="Public" color="primary" value="0"></v-radio>
              <v-radio label="Private" color="error" value="1"></v-radio>
            </v-radio-group>
          </div>
        </fieldset>
      </v-flex>
    </v-layout>

    <div style="text-align:center;" id="write-btn">
      <v-btn class="v-btn theme--dark" @click="updatePost">수정</v-btn>
      <v-btn class="v-btn theme--dark" @click="deletePost">삭제</v-btn>
      <v-btn class="v-btn theme--dark" @click="goRead">취소</v-btn>
    </div>

    <loading :active.sync="isLoading" :can-cancel="false" :is-full-page="true"></loading>
  </v-flex>
</v-layout>
</template>

<script>
import markdownEditor from 'vue-simplemde/src/markdown-editor'
import ImageUpload from "@/components/common/ImageUpload"
import HashTag from "@/components/common/HashTag"
import Loading from 'vue-loading-overlay';
import 'vue-loading-overlay/dist/vue-loading.css';
import Time from "@/services/Time"

export default {
  name: 'PostUpdatePage',
  components: {
    markdownEditor,
    ImageUpload,
    HashTag,
    Loading
  },
  data() {
    return {
      post: null,
      items:[],
      project:{},
      isLoading: false,
    }
  },
  async mounted() {
    await this.fetchData();
    this.readProjectList();
  },
  computed:{
    async form () {
      return {
        title: this.post.post_title,
        content: this.post.post_content,
        share: this.post.post_share,
        category:this.project.project_category,
        project:this.project.project_num,
        updated_at:Time.getFullDate(),
        tags: this.$refs.hashtag.getTagsForDb(),
        imageUrl: await this.$refs.imagePicker.getImageUrl(),
        user_num:this.post.user_num,
        image_num:this.post.image_num,
        imageconn_num: this.post.imageconn_num
      }
    },
  },
  beforeRouteLeave(to, from, next) {
    next();
  },
  methods: {
    async fetchData() {
      this.post = null;

      await this.$http.get(this.$store.state.testIp + "/post/readById/" + this.$route.params.id)
        .then((response) => {
          this.post = response.data.post;

          this.$refs.imagePicker.setImage(response.data.post.image_url);

          var tags = [];
          var colors = ['green', 'purple', 'indigo', 'cyan', 'teal', 'orange'];

          console.log(response.data);
          var val = response.data.tags;
          console.log(val);
          for (var i = 0; i < val.length; i++) {
            tags.push({
              text: val[i].tag_name,
              color: colors[i % 6]
            })
          }

          console.log(tags);
          this.$refs.hashtag.setTags(tags);
        })
        .catch(error => {
          console.log(error);
        })
    },
    async updatePost() {
      this.isLoading = true;
      var post = await this.form;

      this.$http.put(this.$store.state.testIp + "/post/updateById/"+this.$route.params.id, post)
      .then((response) => {
        alert("수정이 완료 되었습니다.");
        this.isLoading = false;
        this.$router.go(-1);
      })
      .catch((error) => {
        alert("수정 실패하였습니다.")
        this.isLoading = false;
      })
    },
    async deletePost() {
      var isDelete = confirm("정말 삭제하시겠습니까?");

      if(isDelete){
        this.isLoading = true;
        this.$http.delete(this.$store.state.testIp + "/post/deleteById/" + this.$route.params.id)
        .then((response) => {
          alert("삭제되었습니다.")
          this.isLoading = false;
          this.$router.push("/")
        })
        .catch((error) => {
          alert("삭제 실패하였습니다.")
          this.isLoading = false;
        })
      }
    },
    readProjectList(){
      this.$http.post(this.$store.state.testIp + "/post/project/list/" + this.$session.get("userInfo").user_num)
      .then((result) => {
        this.items = result.data;
        for(var i = 0; i < this.items.length; i++){
          if(this.items[i].project_num == this.post.post_project){
            this.project = this.items[i];
          }
        }
      })
    },
    goRead() {
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
