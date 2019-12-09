<template>
<v-layout wrap>
  <v-flex xs12 ma-5>
    <v-card>
      <v-card-title>
        <span class="headline">회원 탈퇴</span>
      </v-card-title>
      <v-card-text>
        <v-container grid-list-md>
          <v-layout wrap my-5>
            <v-flex xs12>
              <h1>정말 탈퇴하시겠습니까?</h1>
              <h1>탈퇴 하시려면 아래 문구를 입력해 주세요.</h1>

              <h1 style="margin-top:50px;text-align:center;color:#999;">탈퇴하겠습니다.</h1>
              <v-spacer></v-spacer>
            </v-flex>
            <v-flex xs12>
              <v-text-field type="text" v-model="words" required></v-text-field>
            </v-flex>
          </v-layout>
        </v-container>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn :disabled="isDisabled" color="blue darken-1" flat @click="removeUser">회원 탈퇴</v-btn>
      </v-card-actions>

    </v-card>
  </v-flex>
  <Loading :isLoading="isLoading" />
</v-layout>
</template>

<script>
import Loading from "@/components/common/Loading"

export default {
  name: 'UserDeletePage',
  components: {
    Loading
  },
  data() {
    return {
      words: "",
      isDisabled: true,
      isLoading: false
    }
  },
  watch: {
    words: function(val) {
      if (val == "탈퇴하겠습니다.") {
        this.isDisabled = false;
      } else {
        this.isDisabled = true;
      }
    }
  },
  methods: {
    async removeUser() {
      alert("안되용 가지마세용!")
      this.goHome();
    },
    goHome(){
      this.$router.push("/");
    }
  },
  async created(){
    if (!this.$session.has("userInfo")) {
      alert("잘못된 접근입니다.")
      this.$router.push("/")
    }
  },
  beforeRouteLeave(to, from, next) {
    next();
  },
  destroyed() {

  }
}
</script>
