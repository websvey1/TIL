<template>
<v-app>
  <sequential-entrance fromTop v-if="items.length > 0">
    <!-- <v-card flat v-for="item in items" max-width="1000" max-height="170" style="margin: auto; margin-bottom:30px; border:1px solid rgb(143, 143, 143);"> -->
    <v-card v-for="item in items" max-width="1000" max-height="135" style="margin: auto; margin-bottom:30px; border-radius: 15px;">
      <div v-if="item.exist == true">
        <v-layout py-4 pl-4>
          <v-flex shrink>
            <v-img height="120" width="120" src="https://gravitylab.nz/wp-content/uploads/2018/11/OnboardYourTeam-011.jpg" style="border-radius: 50%; margin-top: -17px;"></v-img>
          </v-flex>
          <v-flex>
            <v-container grid-list-lg style="margin-left: 0px;">
              <v-layout column>
                <v-flex style="padding-top: 3px;">
                  <h1>{{ item.title }}</h1>
                </v-flex>
                <v-flex v-if="item.auth == 0" style="margin-top: -20px; margin-left: auto;">
                  <v-btn flat class="outlined_first" @click="openDialog(item)">팀원보기</v-btn>
                  <v-btn flat class="outlined_second" @click="item.auth = 1 && accept(item.title)">수락</v-btn>
                  <v-btn flat class="outlined_third" @click="del(item)">거절</v-btn>
                </v-flex>
                <v-flex v-else style="margin-top: -20px; margin-left: auto;">
                  <v-btn flat class="outlined_first" @click="openDialog(item)">팀원보기</v-btn>
                  <v-btn flat class="outlined_second" @click="addMember(item)">팀원추가</v-btn>
                  <v-btn flat class="outlined_fourth" @click="go(item.teamNum)">선택</v-btn>
                  <v-btn flat class="outlined_third" @click="del(item)">팀 나가기</v-btn>
                </v-flex>
              </v-layout>
            </v-container>
          </v-flex>
        </v-layout>
      </div>
    </v-card>
  </sequential-entrance>
  <v-layout v-else wrap>
    <v-flex xs12 px-2 mt-4 style="margin-bottom: 35px;">
      <h1 style="margin-top:50px;text-align:center;">TEAM이 없습니다.</h1>
    </v-flex>
  </v-layout>
  <v-dialog hide-overlay v-model="dialog" persistent max-width="400px">
    <v-card>
      <v-card-title style="display:flex; justify-content:center;">
        <h2> 팀원을 확인하세요! </h2>
      </v-card-title>
      <v-card-text style="text-align:center;">
        <v-container grid-list-md style="display:flex; justify-content:center;">
          <v-layout wrap>
            <v-flex xs12>
              [ {{ this.selectItem.member }} ]
            </v-flex>
          </v-layout>
        </v-container>
      </v-card-text>
      <v-card-actions style="display:flex; justify-content:center;">
        <!-- <v-spacer></v-spacer> -->
        <v-btn color="blue darken-1" flat @click="closeDialog">OK!</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>

  <v-dialog v-model="showModal" persistent max-width="600px">
    <v-card>
      <v-card-title>
        <span class="headline">Team member추가하기</span>
      </v-card-title>
      <v-card-text>
        <v-container grid-list-xl>
          <v-layout wrap>
            <v-flex xs12>
              <v-autocomplete v-model="members" :disabled="isUpdating" :items="people" filled chips color="blue-grey lighten-2"
                label="Member *" item-text="name" item-value="name" required multiple>
              <template v-slot:item="data">
                <template v-if="typeof data.item !== 'object'">
                  <span v-text="data.item"></span>
                </template>
                <template v-else>
                  <span>{{data.item.name}} ({{data.item.id}})</span>
                </template>
              </template>
              </v-autocomplete>
            </v-flex>
          </v-layout>
        </v-container>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="blue darken-1" flat @click="updateMember">Add</v-btn>
        <v-btn color="blue darken-1" flat @click="showModal = false">CANCEL</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</v-app>
</template>

<script>
import router from '@/router'

export default {
  name: 'TeamList',
  components: {},
  data() {
    return {
      items: [],
      tempPeople: [],
      people: [],
      members: [],
      dialog: false,
      showModal: false,
      isUpdating: false,
      selectItem: "",
      data: []
    }
  },
  props: {
    post: {}
  },
  mounted() {
    this.start();
    this.getUsers();
  },
  methods: {
    addMember(item){
      this.people = []
      this.data = item
      this.showModal = true
      var temp = item.member.split(' ')

      for(var i = 0; i < this.tempPeople.length; i++){
        var tag = 0;

        for(var m = 0; m < temp.length; m++){
          if(this.tempPeople[i].name == temp[m]){
            tag = 1
          }
        }

        if(tag == 0){
          this.people.push(this.tempPeople[i])
        }
      }
    },
    async updateMember(){
      var mem = {
        teamNum: this.data.teamNum,
        member: this.members
      }
      console.log(this.members)
      ////////////////////////// Member table에 user들 넣기 /////////////////////////
      await this.$http.post(this.$store.state.testIp + '/team/makeMember', mem)
      .then(async (response) =>{
        console.log('member 입력 완료.')
        // await this.update(mem.teamNum);
        this.items = []
        this.members = []
        this.start();
        this.showModal = false;
      })
      .catch((error) => {
        console.log(error)
      })
    },
    getUsers(){ // 전체 user 다 가져오는 함수
      this.$http.post(this.$store.state.testIp + '/team/getUser')
        .then((response) => {
            var items = response.body;

            for(var i = 0; i < items.length; i++){
                this.tempPeople.push({name: items[i].user_name, id: items[i].user_id});
            }
        })
        .catch((error) =>{
            console.log(error)
        })
    },
    openDialog(item) {
      this.selectItem = item;
      this.dialog = true;
    },
    closeDialog() {
      this.selectItem = "";
      this.dialog = false;
    },
    async start() {
      var temp = {
        num: this.$session.get('userInfo').user_num
      }

      await this.$http.post(this.$store.state.testIp + '/team/getTeamList', temp)
        .then(async (response) => {
          // 속해있는 여러 개의 팀이 response.body를 통해 전달됨
          for (var i = 0; i < response.body.length; i++) {
            // 여러 개의 팀 중, 1개씩 순서대로 실행
            var data = {
              teamNum: response.body[i].team_num
            }
            // 선택된 팀에 속한 member들을 구함
            await this.$http.post(this.$store.state.testIp + '/team/getMember', data)
              .then(async (response) => {
                var tempTeamName = response.body[0].team_name;
                var tempMember = '';
                var tempTeamNum = response.body[0].team_num;

                for (var k = 0; k < response.body.length; k++) {
                  tempMember += response.body[k].user_name + " "
                }

                var tempData = {
                  num: this.$session.get('userInfo').user_num,
                  teamNum: response.body[0].team_num
                }

                await this.$http.post(this.$store.state.testIp + '/team/getAuth', tempData)
                  .then((response) => {
                    this.items.push({
                      title: tempTeamName,
                      member: tempMember,
                      auth: response.body[0].member_auth,
                      exist: true,
                      teamNum: tempTeamNum
                    })
                  })
                  .catch((error) => {
                    console.log(error)
                  })
              })
              .catch((error) => {
                console.log(error)
              })
          }
        })
        .catch((error) => {
          console.log(error)
        })
    },
    goReadPage(postNum, email) {
      console.log(postNum);
      router.push({
        name: "PostReadPage",
        params: {
          id: postNum
        }
      })
    },
    show(memberData) {
      alert(memberData)
    },
    ModalHide() {
      this.modal = false;
    },
    accept(titleData) {
      var temp = {
        num: this.$session.get('userInfo').user_num,
        teamName: titleData
      }
      this.$http.post(this.$store.state.testIp + '/team/getTeamNum', temp)
        .then((response) => {
          var auth = {
            num: this.$session.get('userInfo').user_num,
            teamNum: response.body[0].team_num
          }
          this.$http.post(this.$store.state.testIp + '/team/changeAuth', auth)
            .then((response) => {
              console.log("Change complete")
              var data = {
                id: this.$session.get('userInfo').user_num
              }
              this.$http.post(this.$store.state.testIp + '/team/checkNew', data)
                .then((response) => {
                  if (response.body[0].total > 0) {
                    this.$store.state.exist = true
                  } else {
                    this.$store.state.exist = false
                  }
                })
                .catch((error) => {
                  console.log(error)
                })
            })
            .catch((error) => {
              console.log(error)
            })
        })
        .catch((error) => {
          console.log(error)
        })

    },
    del(team) {
      var state;

      if(team.auth == 0){
        state = confirm("정말 거절하시겠습니까?");
      }
      else{
        state = confirm("팀에서 나가시겠습니까?");
      }

      if(state){
        var titleData = team.title;
        for (var i = 0; i < this.items.length; i++) {
          if (this.items[i].title == titleData) {
            this.items[i].exist = false
          }
        }

        var temp = {
          num: this.$session.get('userInfo').user_num,
          teamName: titleData
        }
        this.$http.post(this.$store.state.testIp + '/team/getTeamNum', temp)
          .then((response) => {
            var auth = {
              num: this.$session.get('userInfo').user_num,
              teamNum: response.body[0].team_num
            }
            this.$http.post(this.$store.state.testIp + '/team/deleteTeam', auth)
              .then((response) => {
                console.log("Delete complete")
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
    async update(pk) {
      console.log("여기다 이자식아")
      var temp = {
        num: this.$session.get('userInfo').user_num,
        teamNum: pk
      }

      await this.$http.post(this.$store.state.testIp + '/team/getLatestTeam', temp)
        .then(async (response) => {
          console.log('team name:')
          console.log(response.body)
          var tempTeamName = response.body[0].team_name;
          console.log(tempTeamName)
          var data = {
            teamNum: pk
          }
          // 선택된 팀에 속한 member들을 구함
          await this.$http.post(this.$store.state.testIp + '/team/getMember', data)
            .then(async (response) => {
              console.log(response.body)
              var tempMember = '';
              var tempTeamNum = response.body[0].team_num;

              for (var k = 0; k < response.body.length; k++) {
                tempMember += response.body[k].user_name + " "
              }

              this.items.push({
                title: tempTeamName,
                member: tempMember,
                auth: 0,
                exist: true,
                teamNum: tempTeamNum
              })
            })
            .catch((error) => {
              console.log(error)
            })
        })
        .catch((error) => {
          console.log(error)
        })
    },
    go(id) {
      console.log(id)
      this.$router.push({
        name: "TeamProjectPage",
        params: {
          id: id
        }
      })
    }
  }
}
</script>

<style scoped>
@import url(https://fonts.googleapis.com/css?family=Jura:300,400,500,600);
@import url(https://fonts.googleapis.com/css?family=Play);
@import url(https://fonts.googleapis.com/css?family=Open+Sans:400,300);

.logo {
  float: left;
}

.post-container {
  position: relative;
  padding-left: 50px;
}

.published {
  position: absolute;
  width: 50px;
  left: 25px;
  padding: 10px 0;
  /* text-align: center; */
  background-color: #fff;
}

.date {
  text-transform: uppercase;
  font-family: Open Sans;
  font-weight: bold;
  color: #222;
  font-size: 12px;
}

.post {
  padding-left: 50px;
  padding-bottom: 60px;
  margin: 0 auto;
  border-left: 1px solid #999;
}

.post-container:last-child .post {
  padding-bottom: 60px;
}

.posth1 {
  /* padding-top: 3px; */
  font-family: Open Sans;
  font-weight: bold;
  color: #222;
  font-size: 30px;
  margin: 0;
  text-transform: uppercase;
  /* 여러 줄 자르기 추가 스타일 */
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: normal;
  line-height: 1.2;
  height: 1.2em;
  text-align: left;
  word-wrap: break-word;
  display: -webkit-box;
  -webkit-line-clamp: 1;
  -webkit-box-orient: vertical;
}

.pub-date {
  font-family: Open Sans;
  color: #666;
  font-size: 12px;
}

.post img {
  width: 100px;
  height: 100px;
  border-radius: 9999px;
  float: left;
  margin-right: 15px;
  margin-top: 5px;
}

.ptag {
  padding-top: 10px;
  font-family: Open Sans;
  color: #333;
  line-height: 1.6;
  font-size: 14px;
  margin-top: 0;
  text-overflow: ellipsis;
  /* 여러 줄 자르기 추가 스타일 */
  white-space: normal;
  /* height: 4.5em; */
  text-align: left;
  word-wrap: break-word;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.v-card__text {
  padding: 0px !important;
  padding-bottom: 4px !important;
}

.v-card__title {
  padding: 0px !important;
  padding-top: 25px !important;
  padding-bottom: 5px !important;
}

.v-btn.outlined_first {
  border: 1px solid rgb(255, 159, 0);
  border-radius: 5%;
  height: 40px;
  width: 60px;
  /* font-weight:bold; */
  color: rgb(255, 159, 0);
  background-color: rgb(255, 159, 0, 0.2);
}

.v-btn.outlined_second {
  border: 1px solid rgb(0, 68, 194);
  border-radius: 5%;
  height: 40px;
  width: 60px;
  /* font-weight:bold; */
  color: rgb(0, 68, 194);
  background-color: rgba(0, 68, 194, 0.2);
}

.v-btn.outlined_third {
  border: 1px solid rgb(224, 0, 0);
  border-radius: 5%;
  height: 40px;
  width: 60px;
  /* font-weight:bold; */
  color: rgb(224, 0, 0);
  background-color: rgb(224, 0, 0, 0.2);
}

.v-btn.outlined_fourth {
  border: 1px solid rgb(86, 147, 0);
  border-radius: 5%;
  height: 40px;
  width: 60px;
  /* font-weight:bold; */
  color: rgb(86, 147, 0);
  background-color: rgb(86, 147, 0, 0.2);
}

.modal-enter {
  opacity: 0;
}

.modal-leave-active {
  opacity: 0;
}

.modal-enter .modal-container,
.modal-leave-active .modal-container {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}
</style>
