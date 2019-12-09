<template>
<v-layout wrap>
  <v-flex xs12 ma-5>
    <v-card>
      <v-card-title>
        <span class="headline">Update User Info</span>
      </v-card-title>
      <v-card-text>
        <v-container grid-list-md>
          <v-layout wrap my-5>
            <v-flex xs12>
              <ImageUpload :random_picture="false" ref="imagePicker"></ImageUpload>
            </v-flex>
            <v-flex xs12>
              <v-text-field readonly label="Name" v-model="user.user_name"></v-text-field>
            </v-flex>
            <v-flex xs12>
              <v-text-field readonly label="id" v-model="user.user_id"></v-text-field>
            </v-flex>
            <v-flex xs12>
              <v-text-field readonly label="Email" v-model="user.user_email"></v-text-field>
            </v-flex>
            <v-flex xs12>
              <v-text-field label="기존 비밀번호*" type="password"  v-model="before_pw" required ref="before_pw"></v-text-field>
            </v-flex>
            <v-flex xs12>
              <v-text-field label="변경할 비밀번호*" type="password" :rules="passRules" v-model="after_pw" required ref="after_pw"></v-text-field>
            </v-flex>
            <v-flex xs12>
              <v-autocomplete v-model="favor" :items="techs" filled chips color="blue-grey lighten-2" label="관심기술" item-text="tech_name" item-value="tech_num" multiple>
                  <template v-slot:item="data">
                      <template v-if="typeof data.item !== 'object'">
                          <span v-text="data.item"></span>
                      </template>
                      <template v-else>
                        <span v-text="data.item.tech_name"></span>
                      </template>
                  </template>
              </v-autocomplete>
            </v-flex>
          </v-layout>
        </v-container>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="blue darken-1" flat @click="updateUser">수정</v-btn>
        <v-btn color="blue darken-1" flat @click="goHome">취소</v-btn>
      </v-card-actions>

    </v-card>
  </v-flex>
  <Loading :isLoading="isLoading"/>
</v-layout>
</template>

<script>
import Loading from "@/components/common/Loading"
import ImageUpload from "@/components/common/ImageUpload"

export default {
  name: 'UserUpdatePage',
  components: {
    Loading,
    ImageUpload
  },
  data() {
    return {
      user:{
        user_name:"",
        user_email:"",
      },
      favor:[],
      techs:[],
      before_pw:"",
      after_pw:"",
      passRules: [
        v => !!v || 'Password is required',
        v => v.length >= 6 || 'Password must be longer than 6 characters'
      ],

      isLoading: false
    }
  },
  computed:{
    validate(){
      return {
        // before_pw: this.before_pw,
        // after_pw: this.after_pw,
      }
    },
    form(){
      return {
        user_num: this.user.user_num,
        before_pw: this.before_pw,
        after_pw: this.after_pw,
        email: this.user.email,
        name: this.user.name,
        favor: this.favor,
        image:this.$refs.imagePicker.getProfileUrl()
      }
    }
  },
  methods: {
    checkValidation(){
      Object.keys(this.validate).forEach(f => {
          if(this.$refs[f].validate(true) == false){
            return false;
          }
      })

      return true;
    },

    async readTech(){
      await this.$http.get(this.$store.state.testIp + "/user/tech")
      .then((req) => {
        this.techs = req.data;
      })
    },

    async updateUser(){
      if(this.checkValidation()){
        this.isLoading = true;

        if(this.favor.length > 3){
          alert("관심기술은 3개까지 등록할 수 있습니다.")
          this.isLoading = false;
          return
        }

        this.$http.put(this.$store.state.testIp + "/user/update", this.form).
        then((req) => {
          if(req.data == "fail"){
            alert("비밀번호를 다시 확인해주세요.");
            this.isLoading = false;
          }
          else{
            this.$http.post(this.$store.state.testIp + "/user/read/" + this.$session.get("userInfo").user_num)
            .then((req) => {
              this.$session.set("userInfo", req.data);
              console.log(req.data);
              alert("변경되었습니다.")
              this.isLoading = false;
              this.$router.go(-1)
            })
          }
        })
        .catch(error => {
          alert("알 수 없는 에러가 발생했습니다.")
          this.isLoading = false;
        })
      }
    },

    goRemoveUser(){
      this.$router.push("/removeuser")
    },
    goHome(){
      this.$router.push("/")
   }
  },
  async created(){
    if (this.$session.has('userInfo')) {
    } else {
      alert("로그인 해주세요.");
      this.$router.push("/");
    }
    await this.readTech();
    this.user = this.$session.get("userInfo")
    this.$refs.imagePicker.setImage(this.user.user_image);
    // console.log(this.user);
    for(var i = 0; i < this.user.favor.length; i++){
      this.favor.push(this.user.favor[i].tech_num);
    }
    // console.log(this.favor);
  },
  beforeRouteLeave(to, from, next) {

    next();
  },
  destroyed() {

  },
  
}
</script>
