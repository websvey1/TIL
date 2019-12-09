<template style="min-height:100%;">
    <div style="background-color: white; padding-top:30px;">
        <div class="container">
            <!-- Login 시, 각 user의 name에 따라 ~~님의 팀으로 되도록 바꾸어 주어야 함! -->
            <h1 class="teamName" style="margin-left: 2.5em">{{ this.$session.get('userInfo').user_name }}님의 팀</h1>

            <v-btn class="teamBtn" @click="showModal = true" outline color="indigo" style="float: right; margin-right: 5em" round>Team 추가</v-btn>

            <v-dialog v-model="showModal" persistent max-width="600px">
                <v-card>
                    <v-card-title>
                        <span class="headline">Team 추가하기</span>
                    </v-card-title>
                    <v-card-text>
                        <v-container grid-list-xl>
                            <v-layout wrap>
                                <v-flex xs12>
                                    <v-text-field label="Team Name *" v-model="teamName" ref="teamName" :rules="teamRules" required></v-text-field>
                                </v-flex>
                                <v-flex xs12>
                                    <v-autocomplete v-model="members" :disabled="isUpdating" :items="people" filled chips color="blue-grey lighten-2"
                                        label="Member *" item-text="name" item-value="name" :rules="memberRules" required multiple>
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
                        <v-btn color="blue darken-1" flat @click="addTeam">Add</v-btn>
                        <v-btn color="blue darken-1" flat @click="close">CANCEL</v-btn>
                    </v-card-actions>
                </v-card>
            </v-dialog>
        </div>
            <!-- 이 밑에 div로 새로 파서, 지금 user가 속해있는 팀 list 뿌려줘야 함 -->
        <div>
            <TeamList ref="teamList"/>
        </div>
    </div>
</template>

<script>
import TeamList from '@/components/TeamList'

export default {
    name: 'TeamChoose',
    components: {
        TeamList,
    },
    data() {
        return{
            teamName: '',
            showModal: false,
            isUpdating: false,
            teamRules: [v => !!v || 'Team Name을 입력해 주세요.'],
            memberRules: [v => !!v || 'Member를 입력해 주세요.'],
            members: [],
            people: [],
        }
    },
    watch:{
      members(v){
        // console.log(v);
      }
    },
    async created() {
        if (this.$session.has('userInfo')) {
            await this.start()
        } else {
            alert("로그인 해주세요.");
            this.$router.push("/");
        }
    },
    mounted(){
    },
    methods:{
        start(){
            // 1st. DB에 가서, 존재하는 모든 Name 가져오기
            this.$http.post(this.$store.state.testIp + '/team/getUser',{})
            // this.$http.post(this.$store.state.testIp + '/team/getUser',{})
            .then((response) => {

                var items = response.body;

                for(var i = 0; i < items.length; i++){
                    this.people.push({name: items[i].user_name, id: items[i].user_id});
                }
                console.log('모든 user 가져오기 완료.')
            })
            .catch((error) =>{
                console.log(error)
            })
        },
        async addTeam(){
            if(this.teamName == ''){
                alert("Team Name을 입력하세요.")
                return
            }else if(this.members == ''){
                alert("Team Member를 등록하세요.")
                return
            }

            var temp = {
                name: this.teamName
            }
            // 1st. DB에 가서, Team 만들기
            /////////////////////////// Team 만들기 /////////////////////////////////

            await this.$http.post(this.$store.state.testIp + '/team/makeTeam', temp)
            .then(async (response) => {
                // 2nd. Team Num 받아와서, member table에 각 user들 이 Team Num값으로 집어넣기
                console.log('Team 생성 완료.')
                var mem = {
                    teamNum: response.data,
                    member: this.members
                }
            ////////////////////////// Member table에 user들 넣기 /////////////////////////
                await this.$http.post(this.$store.state.testIp + '/team/makeMember', mem)
                .then(async (response) =>{
                    console.log('member 입력 완료.')
                    await this.$refs.teamList.update(mem.teamNum);
                    this.close();
                })
                .catch((error) => {
                    console.log(error)
                })
            })
            .catch((error) => {
                console.log(error)
            })
        },
        close(){
            this.resetValues();
            this.showModal = !this.showModal
        },
        resetValues(){
            this.teamName = '';
            this.members = []
        }
    }
}
</script>

<style>
.teamName{
    display: inline-block;
}
.teamBtn{
    display: inline-block;
}
</style>
