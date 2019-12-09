<template>
<div style="background-color: white; padding-bottom:50px;">
    <div style="padding:30px 17% 50px;">
    <v-btn @click="goWrite" outline color="indigo" round style="float:right;">Project 추가</v-btn>
    </div>
    <span class="mdi mdi-home"></span>
    <div class="container project">
        <v-layout wrap v-if="projects.length > 0">
            <v-flex v-for="project in projects" :key="project" px-3 xs6 style="margin-bottom: 65px;">
                <MyprojectCard :project="project"></MyprojectCard>
            </v-flex>
        </v-layout>
        <v-layout v-else wrap>
          <v-flex xs12 px-2 mt-4 style="margin-bottom: 35px;">
            <h1 style="margin-top:50px;text-align:center;">PROJECT가 없습니다.</h1>
          </v-flex>
        </v-layout>
    </div>
</div>
</template>


 <script>
import MyprojectCard from '@/components/MyprojectCard'
import { async } from 'q';

export default {
    name: 'MyprojectPage',
    components: {
        MyprojectCard
    },
    data() {
        return {
            projects: [],
        }
    },
    async created() {
        if (this.$session.has('userInfo')) {
            await this.getProject()
        } else {
            alert("로그인 해주세요.");
            this.$router.push("/");
        }
    },
    mounted(){
        // this.getProject()
    },
    methods: {
        async getProject() {
            var data = {
                userNum: this.$session.get('userInfo').user_num
            }
            await this.$http.post(this.$store.state.testIp + '/myproject/userproject', data)
            .then(async (response) => {
                for (var i=0; i < response.body.length; i++){
                    var temp = {
                        pjtNum: response.body[i].project_num
                    }
                    // console.log(temp)
                    await this.$http.post(this.$store.state.testIp + '/myproject/getProject', temp)
                    .then(async (res) => {
                        // console.log(res.body)
                        this.projects.push({
                            pjt: res.body.project[0],
                            image: res.body.image
                        })
                        // console.log(this.projects)
                    })
                }
            })
        },

        goWrite() {
            this.$router.push('/myproject/create')
        }
    },
 }
 </script>

 <style>
   .container.project {
    background-color: white;
    width: 75%;
    margin: 0 auto;
  }
 </style>
