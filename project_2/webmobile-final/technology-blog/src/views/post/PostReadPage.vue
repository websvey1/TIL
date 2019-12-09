<template>
<v-layout wrap align-center justify-center row fill-height>
  <v-flex xs12 text-xs-left>
    <v-img v-if="post != null" :src="post.image_url" aspect-ratio="1.7">
      <v-layout wrap pa-5 fill-height>
        <v-flex pa-5 ma-5 white xs12>
          <span>
            <v-chip color="light-green lighten-4" large style="margin-top: -30px; font-size: 20px;"><b>{{post.project_title}}</b></v-chip>
          </span>
          <h1 class="multipleline" style="display: inline-block">&nbsp;{{post.post_title}}</h1>
          <h3 style="text-align:right; color:grey;">작성자 : {{post.user_name}}</h3>
          <v-divider></v-divider>
          <h3 style="text-align:right;color:grey;">마지막 수정 날짜 : {{post.post_updated_at}}</h3>
          <v-divider dark></v-divider>
          <h1 class="multipleline content-field">{{post.post_content}}</h1>
          <div style="text-align:center;" id="write-btn">
            <v-chip v-for="tag in tags" outline :color="tag.color" >
               #{{tag.text}}
             </v-chip>

            <v-divider dark></v-divider>
            <v-btn class="v-btn theme--dark" @click="goHome">목록</v-btn>
            <v-btn v-if="$session.has('userInfo') && post.user_id == $session.get('userInfo').user_id" class="v-btn theme--dark" @click="goUpdate">수정</v-btn>
          </div>
        </v-flex>
      </v-layout>
    </v-img>
  </v-flex>
</v-layout>
</template>

<script>
import markdownEditor from 'vue-simplemde/src/markdown-editor'
import ImageUpload from "@/components/common/ImageUpload"

export default {
  name: 'PostReadPage',
  components: {
    markdownEditor,
    ImageUpload
  },
  data() {
    return {
      post:null,
      tags:[],
      modify:false
    }
  },
  methods: {
    goHome(){
      this.$router.go(-1);
    },
    goUpdate(){
      this.$router.push({name:"PostUpdatePage", params:{id:this.$route.params.id, email:this.post.email}})
    },
    async fetchData(){
      this.post = null;

      this.$http.get(this.$store.state.testIp + "/post/readById/" + this.$route.params.id, {
        headers: {'Cache-Control': 'no-cache'}
      })
      .then((response) => {
        this.post = response.data.post
        if(this.post.post_share == '1'){
          if(!this.$session.has("userInfo") || this.$session.get('userInfo').user_num != this.post.post_user){
            alert("권한이 없습니다.");
            this.$router.go(-1);
          }
        }
        var colors =  ['green', 'purple', 'indigo', 'cyan', 'teal', 'orange'];

        this.tags = [];

        for(var i = 0; i < response.data.tags.length; i++){
          this.tags.push({
            text:response.data.tags[i].tag_name,
            color:colors[i%6]
          })
        }
      })
      .catch((error) => {
        alert(error)
      })
    }
  },
  async created(){
    await this.fetchData();
  },
  beforeRouteLeave(to, from, next){
    next();
  },
  destroyed(){

  }

}
</script>

<style scoped>
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

.content-field{
  /* width: 100%; */
  min-height: 500px;
}

.multipleline {
  max-width: 1200px;
  display: inline-block;
  overflow: hidden;
  text-overflow: ellipsis;
  /* 여러 줄 자르기 추가 스타일 */
  white-space: normal;
  text-align: left;
  word-wrap: break-word;
  display: -webkit-box;
  -webkit-box-orient: vertical;
}
</style>
