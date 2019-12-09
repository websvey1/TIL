<template>
<v-layout wrap v-if="projects.length > 0 || teamprojects.length > 0">

    <v-layout wrap v-if="status == 'Project' && content == ''">
        <v-flex v-for="project in projects" px-3 xs6 style="margin-bottom: 40px;">
            <ProjectCard :project="project"></ProjectCard>
        </v-flex>
    </v-layout>

    <v-layout wrap v-else-if="status == 'Project' && category == 0 && content != ''">
        <v-layout v-if="nameProjects.length > 0">
        <v-flex v-for="project in nameProjects" px-3 xs6 style="margin-bottom: 40px;">
            <ProjectCard :project="project"></ProjectCard>
        </v-flex>
        </v-layout>
        <v-layout v-else wrap style="display:flex; justify-content:center; margin:0 20%; padding: 70px 0;">
          <img src="@/assets/crying.png" style="width:30%; position:relative;"/>
          <h1 style="margin:50px 0;">검색한 내용에 해당하는 PROJECT가 없습니다.</h1>
        </v-layout>
    </v-layout>

    <v-layout wrap v-else-if="status == 'Project' && category == 1 && content != ''">
        <v-layout v-if="contProjects.length > 0">
        <v-flex v-for="project in contProjects" px-3 xs6 style="margin-bottom: 40px;">
            <ProjectCard :project="project"></ProjectCard>
        </v-flex>
      </v-layout>
      <v-layout v-else wrap style="display:flex; justify-content:center; margin:0 20%; padding: 70px 0;">
        <img src="@/assets/crying.png" style="width:30%; position:relative;"/>
        <h1 style="margin:50px 0;">검색한 내용에 해당하는 PROJECT가 없습니다.</h1>
      </v-layout>
    </v-layout>

    <v-layout wrap v-else-if="status == 'Project' && category == '' && content == ''">
        <v-layout v-if="projects.length > 0">
        <v-flex v-for="project in projects" px-3 xs6 style="margin-bottom: 40px;">
            <ProjectCard :project="project"></ProjectCard>
        </v-flex>
      </v-layout>
      <v-layout v-else wrap style="display:flex; justify-content:center; margin:0 20%; padding: 70px 0;">
        <img src="@/assets/crying.png" style="width:30%; position:relative;"/>
        <h1 style="margin:50px 0;">검색한 내용에 해당하는 PROJECT가 없습니다.</h1>
      </v-layout>
    </v-layout>

    <v-layout wrap v-else-if="status == 'TeamProject' && content == ''">
        <v-flex v-for="teampjt in teamprojects" px-3 xs6 style="margin-bottom: 40px;">
            <TeamCard :teampjt="teampjt"></TeamCard>
        </v-flex>
    </v-layout>

    <v-layout wrap v-else-if="status == 'TeamProject' && category == 0 && content != ''">
        <v-layout v-if="teamNameProjects.length > 0">
        <v-flex v-for="teampjt in teamNameProjects" px-3 xs6 style="margin-bottom: 40px;">
            <TeamCard :teampjt="teampjt"></TeamCard>
        </v-flex>
      </v-layout>
      <v-layout v-else wrap style="display:flex; justify-content:center; margin:0 20%; padding: 70px 0;">
        <img src="@/assets/crying.png" style="width:30%; position:relative;"/>
        <h1 style="margin:50px 0;">검색한 내용에 해당하는 PROJECT가 없습니다.</h1>
      </v-layout>
    </v-layout>

    <v-layout wrap v-else-if="status == 'TeamProject' && category == 1 && content != ''">
        <v-layout v-if="teamContProjects.length > 0">
        <v-flex v-for="teampjt in teamContProjects" px-3 xs6 style="margin-bottom: 40px;">
            <TeamCard :teampjt="teampjt"></TeamCard>
        </v-flex>
      </v-layout>
      <v-layout v-else wrap style="display:flex; justify-content:center; margin:0 20%; padding: 70px 0;">
        <img src="@/assets/crying.png" style="width:30%; position:relative;"/>
        <h1 style="margin:50px 0;">검색한 내용에 해당하는 PROJECT가 없습니다.</h1>
      </v-layout>
    </v-layout>

    <v-layout wrap v-else-if="status == 'TeamProject' && category == '' && content == ''">
        <v-layout v-if="teamprojects.length > 0">
        <v-flex v-for="teampjt in teamprojects" xs6 style="margin-bottom: 40px;">
            <TeamCard :teampjt="teampjt"></TeamCard>
        </v-flex>
      </v-layout>
      <v-layout v-else wrap style="display:flex; justify-content:center; margin:0 20%; padding: 70px 0;">
        <img src="@/assets/crying.png" style="width:30%; position:relative;"/>
        <h1 style="margin:50px 0;">검색한 내용에 해당하는 PROJECT가 없습니다.</h1>
      </v-layout>
    </v-layout>

    <v-layout wrap v-else >
        <img src="@/assets/crying.png" style="width:30%; position:relative;"/>
        <h1 style="margin-top:50px;text-align:center;">검색한 내용에 해당하는 PROJECT가 없습니다.</h1>
    </v-layout>
</v-layout>

</template>

<script>
import ProjectCard from "./ProjectCard"
import TeamCard from "./TeamCard"
import { async } from 'q';

export default {
    name: "ProjectList",
    components: {
        ProjectCard,
        TeamCard
    },
    data() {
        return {
            projects: [],
            nameProjects: [],
            contProjects: [],
            teamprojects: [],
            teamNameProjects: [],
            teamContProjects: [],
            items: ['Project', 'TeamProject'],
            status: 'Project',
            category: '',
            content: '',
        }
    },
    mounted() {
        this.onList();
        this.onTeamList();
    },
    methods: {
        // 여기 parameter에 검색의 category, content 포함해서 받아와야 함!
        async selectProject(status, category, content){
            
            this.nameProjects = []
            this.contProjects = []
            this.teamNameProjects = []
            this.teamContProjects = []

            if(status == '0'){ // Personal Project만 보여주는 상태
                this.status = this.items[0];
                this.category = category
                this.content = content

                if(category == 0 && content != ''){ // 제목 검색이면
                    await this.$http.post(this.$store.state.testIp + '/myproject/searchNameProject', {content: content})
                    .then(async (response) => {
                        // this.nameProjects = []
                        for (var i=0; i < response.body.length; i++){
                            var temp = {
                                pjtNum: response.body[i].project_num,
                                userNum: response.body[i].project_user
                            }
                            await this.$http.post(this.$store.state.testIp + '/myproject/getProject', temp)
                            .then(async (response) => {
                                this.nameProjects.push({pjt: response.body.project[0], image: response.body.image})
                            })
                            .catch((error) => {
                                console.log(error)
                            })
                        }
                    })
                    .catch((error) => {
                        console.log(error)
                    })
                }else if(category == 1 && content != ''){ // 내용 검색이면
                    await this.$http.post(this.$store.state.testIp + '/myproject/searchContProject', {content: content})
                    .then(async (response) => {
                        for (var i=0; i < response.body.length; i++){
                            var temp = {
                                pjtNum: response.body[i].project_num,
                                userNum: response.body[i].project_user
                            }
                            await this.$http.post(this.$store.state.testIp + '/myproject/getProject', temp)
                            .then(async (response) => {
                                this.contProjects.push({pjt: response.body.project[0], image: response.body.image})
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
            }
            else{ // Team Project만 보여주는 상태
                this.status = this.items[1];
                this.category = category
                this.content = content

                if(category == 0 && content != ''){ // 제목 검색이면
                    await this.$http.post(this.$store.state.testIp + '/teamProject/searchNameProject', {content: content})
                    .then(async (res) => {
                        if (res.body.length > 0) {
                            for (var i=0; i < res.body.length; i++) {
                                var data = {
                                    pjtNum: res.body[i].project_num
                                }
                                await this.$http.post(this.$store.state.testIp + '/teamProject/projectimage', data)
                                .then(async (response) => {
                                    var image = []
                                    if (response.body.length > 0) {
                                        image.push(response.body[0])
                                    }
                                    this.teamNameProjects.push({pjt: res.body[i], image: image})
                                })
                            }
                        }
                    })
                    .catch((error) => {
                        console.log(error)
                    })
                }else if(category == 1 && content != ''){ // 내용 검색이면
                    await this.$http.post(this.$store.state.testIp + '/teamProject/searchContProject', {content: content})
                    .then(async (res) => {
                        if (res.body.length > 0) {
                            for (var i=0; i < res.body.length; i++) {
                                var data = {
                                    pjtNum: res.body[i].project_num
                                }
                                await this.$http.post(this.$store.state.testIp + '/teamProject/projectimage', data)
                                .then(async (response) => {
                                    var image = []
                                    if (response.body.length > 0) {
                                        image.push(response.body[0])
                                    }
                                    this.teamContProjects.push({pjt: res.body[i], image: image})
                                })
                            }
                        }
                    })
                    .catch((error) => {
                        console.log(error)
                    })
                }
            }
        },
        async onList() {
            await this.$http.post(this.$store.state.testIp + '/myproject/getPjt') // "개인 프로젝트 && 공개"인 post만 가져오기
            .then(async (res) => {
                for (var i=0; i < res.body.length; i++){
                    var temp = {
                        pjtNum: res.body[i].project_num,
                        userNum: res.body[i].project_user
                    }
                    // console.log(temp)
                    await this.$http.post(this.$store.state.testIp + '/myproject/getProject', temp)
                    .then(async (res) => {
                        this.projects.push({
                            pjt: res.body.project[0],
                            image: res.body.image
                        })
                    })
                    .catch((error) => {
                        console.log(error)
                    })
                }
                // console.log(this.projects)
            })
            .catch((error) => {
                console.log(error)
            })
        },

        async onTeamList() {
            await this.$http.post(this.$store.state.testIp + '/teamProject/teamproject')
            .then(async (res) => {
                // console.log(res.body)
                if (res.body.length > 0) {
                    for (var i=0; i < res.body.length; i++) {
                        var data = {
                            pjtNum: res.body[i].project_num
                        }
                        await this.$http.post(this.$store.state.testIp + '/teamProject/projectimage', data)
                        .then(async (response) => {
                            var image = []
                            if (response.body.length > 0) {
                                image.push(response.body[0])
                            }
                            this.teamprojects.push({
                                pjt: res.body[i],
                                image: image
                            })
                        })
                    }
                    // console.log(this.teamprojects)
                }
            })
            .catch((error) => {
                console.log(error)
            })
        }
    },
}
</script>
