<template>
<div class="container">
  <div class="searchbar-total">
    <div class="searchbar-first">
      <v-select v-model="categoryForSearch" :items="categorysForSearch" item-text="text" :menu-props="{ top: true, offsetY: true }" label="Category"  return-object></v-select>
    </div>
    <div class="searchbar-second">
      <v-text-field xs12 label="검색어를 입력해 주세요." v-model='textForSearch'></v-text-field>
    </div>
    <div class="searchbar-third">
      <v-btn class="v-btn theme--dark" @click="searchUser(categoryForSearch)">검색</v-btn>
      <v-btn class="v-btn theme--dark" @click="allUsers">전체 보기</v-btn>
    </div>
  </div>

  <v-layout wrap v-if="search">
    <v-flex wrap v-for="userInfo in users" v-bind:key="userInfo.userN" xs3 style="margin-top: 30px; margin-bottom: 40px;">
      <div class="card" @click="userRead(userInfo.userN)">
        <div class="banner">
          <!-- <div class="avatar"> -->
          <img class="avatar" :src="userInfo.user_image|image"></img>
          <!-- </div> -->
        </div>
        <h3><b>{{ userInfo.userId }}</b></h3>
        <a>📧 {{ userInfo.userEmail }}</a>
        <a>📱 Project - {{ userInfo.userProject }} Post - {{ userInfo.userPost }}</a>
        <span v-for="tech in userInfo.userTech">
          <v-chip color="rgb(191, 234, 255)">{{ tech }}</v-chip>
        </span>
        <ul>
        </ul>
      </div>
    </v-flex>
  </v-layout>

  <v-layout v-else wrap>
    <v-flex wrap v-for="userInfo in tempUsers" v-bind:key="userInfo.userN" xs3 style="margin-top: 30px; margin-bottom: 40px;">
      <div class="card" @click="userRead(userInfo.userN)">
        <div class="banner">
          <!-- <div class="avatar"> -->
          <img class="avatar" :src="userInfo.user_image|image"></img>
          <!-- </div> -->
        </div>
        <h3><b>{{ userInfo.userId }}</b></h3>
        <a>📧 {{ userInfo.userEmail }}</a>
        <a>📱 Project - {{ userInfo.userProject }} Post - {{ userInfo.userPost }}</a>
        <span v-for="tech in userInfo.userTech">
          <v-chip color="rgb(191, 234, 255)">{{ tech }}</v-chip>
        </span>
        <ul>
        </ul>
      </div>
    </v-flex>
  </v-layout>

  <v-layout v-if="nonexist" wrap style="display:flex; justify-content:center; margin:0 20%; padding-top: 70px;">
    <img src="@/assets/crying.png" style="width:30%; position:relative;"/>
    <h1 style="margin-top:50px;">검색한 내용에 해당하는 User가 없습니다.</h1>
  </v-layout>
</div>
</template>

<script>
export default {
  name: "AnotherUser",
  data() {
    return {
      users: [],
      tempUsers: [],
      search: true,
      nonexist: false,
      searchResult:'',
      searchContent:{
        category:'',
        text:''
      },
      categorysForSearch: [
        {text:'ID', value:'0'},
        {text:'Email', value:'1'},
        {text:'관심 기술', value:'2'},
      ],
      categoryForSearch: {text:'', value:''} ,
      textForSearch: '',
    }
  },
  filters: {
    image(v) {
      if (!v) {
        return "https://t1.daumcdn.net/cfile/tistory/2513B53E55DB206927";
      } else {
        return v;
      }
    }
  },
  async created() {
    if (this.$session.has('userInfo')) {
      await this.onUser()
    } else {
      alert("로그인 해주세요.");
      this.$router.push("/");
    }
  },
  mounted() {
    // this.onUser();
  },
  methods: {
    async onUser() {
      await this.$http.post(this.$store.state.testIp + '/another/getUsers')
        .then(async (response) => {
          for (var i = 0; i < response.body.length; i++) {
            var data = {
              userNum: response.body[i].user_num
            }
            await this.$http.post(this.$store.state.testIp + '/another/getInfo', data)
              .then(async (response) => {
                var tech = response.body;
                this.users.push(tech)
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
    userRead(user_id) {
      var userid = user_id
      console.log(userid)
      this.$router.push(`/another/${userid}`)
    },
    async searchUser(input){
      if(input.value !== ''){
        if(this.textForSearch !== ''){
          this.search = false
          this.tempUsers = []

          var data = {
            category: input.value,
            text: this.textForSearch
          }

          if(input.value == 2){
            for(var i = 0; i < this.users.length; i++){
              if(this.users[i].userTech.length > 0){
                for(var m = 0; m < this.users[i].userTech.length; m++){
                  if(this.users[i].userTech[m].toLowerCase().includes(this.textForSearch.toLowerCase())){
                    this.tempUsers.push(this.users[i])
                    break;
                  }
                }
              }
            }
          }else{
            await this.$http.post(this.$store.state.testIp + '/another/getSelectUsers', data)
            .then(async (response) => {
              // console.log(response.body)
              for (var i = 0; i < response.body.length; i++) {
                var data = {
                  userNum: response.body[i].user_num
                }
                // console.log(data.userNum)
                await this.$http.post(this.$store.state.testIp + '/another/getInfo', data)
                .then(async (response) => {
                  var tech = response.body;
                  // console.log(tech)
                  this.tempUsers.push(tech)
                })
                .catch((error) => {
                  console.log(error)
                })
              }
            })
            .catch((error) => {
              console.log(error)
            })
          }
          if(this.tempUsers.length > 0){
              this.nonexist = false;
            }else{
              this.nonexist = true;
            }
        }
      }
    },
    allUsers(){
      // this.onUser();
      this.search = true
      this.textForSearch = ''
    }
  }
}
</script>

<style scoped>
.card {
  height: auto;
  min-height: 318px;
  width: 225px;
  /* ⬅ Size - Small (width: 200px), Medium (width: 225px), Large (width: 250px) */
  overflow: hidden;
  background-color: #FFFFFF;
  border-radius: 10px;
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
  text-align: center;
  -webkit-transition: .1s ease-in-out;
  transition: .1s ease-in-out;
  cursor: pointer;
}

.card:first-of-type {
  margin-right: 25px;
}

.card:hover {
  margin-top: -25px;
  box-shadow: 0 15px 20px rgba(0, 0, 0, 0.2);
}

.banner {
  height: 100px;
  width: 100%;
  background-image: url("https://images.unsplash.com/photo-1533158326339-7f3cf2404354?ixlib=rb-1.2.1&auto=format&fit=crop&w=1004&q=80");
  padding-top: 35px;
  background-color: #FAFAFA;
  background-size: cover;
  background-position: center;
}


.avatar {
  height: 100px;
  width: 100px;
  margin: auto;
  background-size: cover;
  background-position: center;
  background-color: #F1F1F1;
  border: 3px solid #FFFFFF;
  border-radius: 100%;
  box-shadow: 0 2px 2px rgba(0, 0, 0, 0.1);
}

h3,
a,
i {
  font-family: 'Roboto', sans-serif;
  font-weight: lighter;
  -webkit-transition: .1s ease-in-out;
  transition: .1s ease-in-out;
}

h3 {
  margin-top: 45px;
  margin-bottom: 5px;
  font-size: 18px;
  color: #212121;
}

a {
  display: block;
  padding: 5px 0px;
  font-size: 14px;
  color: rgb(71, 71, 71);
  text-decoration: none;
  font-weight: 400;
  cursor: default !important;
}

a:hover {
  background-color: #FAFAFA;
  color: inherit;
}

ul {
  margin-top: 10px;
  padding: 15px 0px;
  background-color: #FAFAFA;
}

ul a {
  display: inline;
  margin-right: 10px;
}

ul a:last-of-type {
  margin-right: 0px;
}

.searchbar-total {
  display: flex;
  justify-content: center;
  padding-top: 10px;
  padding-bottom: 10px;
  /* background-color: rgba(9,9,9,0.1); */
}

.container h1 {
  margin-left: 50px;
}

.searchbar-first {
  float: left;
  display: inline-block;
  margin: 5px;
  max-width: 150px;
}

.searchbar-second {
  float: left;
  display: inline-block;
  margin: 5px;

}

.searchbar-third {
  float: left;
  display: inline-block;
  margin: 5px 0px;
  vertical-align: center;

}

.searchBtn {
  border-radius: 5%;
  /* font-weight:bold; */
  color: rgb(0, 0, 0);
  background-color: rgb(156, 156, 156);
  text-align: center;
}
</style>
