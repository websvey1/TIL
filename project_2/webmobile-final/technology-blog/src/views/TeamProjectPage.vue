<template>
<div style="background-color: white; padding-bottom:50px;">
    <div style="padding:50px 17%;">
        <v-btn @click="back" outline color="indigo" round style="float:left;">
            <v-icon dark left>arrow_back</v-icon>Back</v-btn>
        <v-btn @click="move" outline color="indigo" round style="float:right;">Project 추가</v-btn>
    </div>
    <span class="mdi mdi-home"></span>
    <div class="container project">
        <v-layout wrap mt-2>
            <v-flex v-for="project in projects" px-3 xs6 style="margin-bottom: 70px;">
                <TeamProjectCard :project="project"></TeamProjectCard>
            </v-flex>
        </v-layout>
    </div>
</div>
</template>


 <script>
import TeamProjectCard from '@/components/TeamProjectCard'
import { async } from 'q';

export default {
    name: 'TeamProjectPage',
    components: {
        TeamProjectCard
    },
    data() {
        return {
            projects: [],
        }
    },
    created(){

    },
    async mounted(){
        if(this.$session.has("userInfo")){
          var data = {
            user_num:this.$session.get("userInfo").user_num,
            team_num:this.$route.params.id
          }

          await this.$http.post(this.$store.state.testIp + '/team/isMember', data)
          .then((res) =>{
              if(res.data == 'f'){
                alert("권한이 없습니다.");
                this.$router.go(-1);
              }
              else{
                this.getProject();
              }
          })
        }
        else{
          alert("권한이 없습니다.");
          this.$router.go(-1);
        }
    },
    methods: {
        back(){
            this.$router.push({ name: "TeamChoose", params: {id: this.$route.params.id} })
        },
        move(){
            this.$router.push({ name: "TeamProjectWritePage", params: {id: this.$route.params.id} })
        },
        async getProject() {                     // 이 함수는 teamprojectpage에 마운트 되어있어 항상 떠있음
            var data = {
                id : this.$route.params.id
            }
            await this.$http.post(this.$store.state.testIp + '/teamProject', data)
            .then(async (response) => {


                for (var i=0; i < response.body.length; i++){
                    var temp = {
                        pjtNum: response.body[i].project_num
                    }
                    await this.$http.post(this.$store.state.testIp + '/teamProject/getpjt', temp)
                    .then(async (res) => {
                        this.projects.push({ pjt: res.body.project[0], image: res.body.image })
                    })
                }
            })
        }
    },
 }
 </script>

 <style>
   .container.project {
    background-color: white;
    width: 80%;
    margin: 0 auto;
  }
 </style>
