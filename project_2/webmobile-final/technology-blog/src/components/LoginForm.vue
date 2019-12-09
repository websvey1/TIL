<template>
<v-dialog v-model="dialog" persistent max-width="550px" @keydown.esc="closeDialog">
  <template v-slot:activator="{ on }">
    <v-flex v-if="isLogin">
        <div style="float:left; padding-top:12px; padding-right:10px; font-family: 'Nanum Pen Script', cursive; font-size:25px; width:210px; ">
         <div class="text-center" style="float:left; margin-right:40px;">
          <v-menu offset-y>
            <template v-slot:activator="{ on }">
              <v-badge>
                <template v-slot:badge>{{ messagesLength }}</template>
                <v-icon v-on="on">mail</v-icon>
              </v-badge>
            </template>
            <v-list style="border-radius: 20px;">
              <div v-if="messages.length > 0">
                <v-list-item v-for="(message, key) in messages" :key="key" @click="ccc">
                <v-card class="mx-auto" width="600" tile style="margin-bottom: 20px; border-radius: 10px;">
                  <v-list-item three-line>
                    <v-list-item-content>
                      <v-list-item-title>
                        <v-chip color="#00C853" text-color="white">
                          <v-avatar left>
                            <v-icon>account_circle</v-icon>
                          </v-avatar>
                          {{ message.user_id }}
                        </v-chip>
                      </v-list-item-title>
                      <div style="margin-bottom:5px;">
                      </div>
                      <v-list-item-subtitle>
                        Title : {{ message.message_title }}
                      </v-list-item-subtitle>
                      <br>
                      <v-list-item-subtitle>
                        Content : {{ message.message_content }}
                      </v-list-item-subtitle>
                      <br>
                      <v-list-item-subtitle>
                        {{ message.created_at }}
                      </v-list-item-subtitle>
                      <span style="float: right; margin-top: -40px; margin-right: 10px;">
                        <v-icon @click="" color="#FF3D00" style="cursor: pointer; margin-right: 5px;">fas fa-reply</v-icon>
                        <v-icon v-if="message.message_read === 0" @click="messageRead(message.message_num)" color="primary" style="cursor: pointer;">fas fa-envelope</v-icon>
                        <v-icon v-else-if="message.message_read === 1" color="primary">fas fa-envelope-open</v-icon>
                        <v-icon @click="messageDelete(message.message_num, key)" color="#FF3D00" style="cursor: pointer; margin-left: 5px;">fas fa-trash-alt</v-icon>
                      </span>
                    </v-list-item-content>
                  </v-list-item>
                </v-card>
                </v-list-item>
              </div>
              <div v-else>
                <v-list-item-title>
                  새로운 메세지가 없습니다.
                </v-list-item-title>
              </div>
            </v-list>
          </v-menu>
        </div>
          <p>{{ userName }}님 환영합니다</p>
        </div>
        <v-btn flat class="outlined" @click="signout" v-on="" color="rgb(57, 117, 72)">Logout</v-btn>
    </v-flex>
    <v-flex v-else>
      <v-btn flat class="outlined" @click="" v-on="on" color="rgb(57, 117, 72)">Login</v-btn>
    </v-flex>
  </template>
  <v-card>
    <v-card-title>
      <span class="headline">LOGIN</span>
    </v-card-title>
    <v-card-text>
      <v-container grid-list-md>
        <v-layout wrap @keydown.enter="loginWithId">
          <v-flex xs12>
            <v-text-field label="Id*" required v-model="id" ref="id" :rules="idRules"></v-text-field>
          </v-flex>
          <v-flex xs12>
            <v-text-field label="Password*" type="password" required v-model="pw" ref="password" :rules="pwRules"></v-text-field>
          </v-flex>
        </v-layout>
      </v-container>
    </v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="blue darken-1" flat @click="loginWithId">LOGIN</v-btn>
      <v-btn color="blue darken-1" flat @click="goSignup">SIGN UP</v-btn>
      <v-btn color="blue darken-1" flat @click="closeDialog">CANCEL</v-btn>
    </v-card-actions>
    <Loading :isLoading="isLoading" :isFullPage="false"/>
  </v-card>
</v-dialog>
</template>

<script>
import Loading from '@/components/common/Loading';

export default {
  name: "LoginForm",
  data() {
    return {
      id: "",
      pw: "",
      dialog: false,
      userName: '',
      isLogin: true,

      isLoading: false,
      isLoadingForSignout: false,
      idRules: [v => !!v || '아이디를 입력해 주세요.'],
      pwRules: [v => !!v || '비밀번호를 입력해 주세요.'],
      alert: false,
      messages: [],
      message_status: 0,
      // gomsg: {
      //   sender: {text: this.$session.get('userInfo').user_id , value: this.$session.get('userInfo').user_num},
      //   receiver: {text: '', value: ''},
      //   msg_title: '',
      //   msg_content: ''
      // },

      flag: true,
      messagesLength: 0
    }
  },
  components:{
    Loading
  },
  created() {
    this.isLoading = true;

    this.isLogin = this.$session.has("userInfo")

    if(this.isLogin){
      console.log(this.$session.get("userInfo"));
      this.userName = this.$session.get('userInfo').user_name
    }
  },
  mounted(){
    this.isLoading = false;
    this.messageCheck();
  },
  computed: {
    form () {
      return {
        id: this.id,
        password: this.pw
      }
    }
  },
  methods: {
    ccc(){
      this.flag = true
    },
    messageCheck() {
      if (this.$session.has('userInfo')){
        var data = {
          id : this.$session.get('userInfo').user_num
        }
        this.$http.post(this.$store.state.testIp + '/another/checkNew', data)
        .then((response) => {
          console.log(response.body)
          this.messages = response.body

          this.$http.post(this.$store.state.testIp + '/another/checkRead', {id: this.$session.get('userInfo').user_num})
          .then((response) => {
            this.messagesLength = response.body[0].total
          })
          .catch((error) => {
            console.log(error)
          })
        })
        .catch((error) => {
          console.log(error)
        })
      }
    },
    messageDelete(msgNum, key) {
      this.messages.splice( key, 1 )
      var data = {
        msg: msgNum
      }
      this.$http.post(this.$store.state.testIp + '/another/messagedelete', data)
      .then((res) => {
        console.log(res.body)
      })
    },

    async messageRead(msgNum) {
      this.messagesLength = this.messagesLength - 1
      var data = {
        msg: msgNum
      }
      this.$http.post(this.$store.state.testIp + '/another/messageread', data)
      .then(async (res) => {
        await this.messageCheck()
        
      })
    },
    checkValidation() {
      var validation = true;

      Object.keys(this.form).forEach(f => {
        if (this.$refs[f].validate(true) == false) {
          validation = false;
        }
      })

      return validation;
    },

    resetForm() {
      Object.keys(this.form).forEach(f => {
        this.$refs[f].reset();
      })
    },

    async loginWithId() {
      if (this.checkValidation()) {
        this.isLoading = true;

        await this.$http.post(this.$store.state.testIp + '/user/login', this.form)
          .then(async (res) => {
            console.log(res.data);
            if (res.data == "fail") {
              alert("아이디와 비밀번호를 확인해 주세요.");
              this.resetForm();
            } else {
              this.isLogin = true;
              this.$session.set("userInfo", res.data);
              await this.messageCheck()
              alert("로그인 되었습니다.")
              console.log(this.$session.get('userInfo').user_num)
              this.userName = this.$session.get('userInfo').user_name
              this.closeDialog();
              this.$emit('loginstate');
            }
            this.isLoading = false;
          })
      }
    },

    goSignup() {
      this.dialog = false;
      this.$router.push("/user/create");
    },

    signout() {
      this.isLogin = false;
      this.$session.remove("userInfo");

      this.resetForm();
      alert("로그아웃 되었습니다.")
      this.$emit('loginstate');
      this.$router.push("/")
    },

    closeDialog() {
      this.dialog = false;
      this.resetForm();
    }
  }
}
</script>

<style>
.v-btn.outlined {
    border: 1px solid rgb(57, 117, 72);
    border-radius:10%;
    height: 40px;
    width: 60px;
  }
</style>
