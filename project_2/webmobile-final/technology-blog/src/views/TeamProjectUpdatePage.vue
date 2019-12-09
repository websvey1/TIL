<template>
<div class="container">
<v-layout wrap align-center justify-center row fill-height>
  <v-flex xs12 ma-5 text-xs-left>
    <v-layout wrap>
      <v-flex xs10>
        <div style="margin: 8px 16px 1px">
          <v-text-field xs12 label="Title" placeholder="프로젝트명을 입력해 주세요." v-model='project.project_title' counter="20" :maxlength="20"></v-text-field>
        </div>
      </v-flex>
      <v-flex xs2 style="margin-top: 3.5px;">
        <v-text-field
            :value="project.project_captain"
            label="프로젝트 팀장"
            disabled
        ></v-text-field>
      </v-flex>
    </v-layout>

    <v-layout wrap>
      <v-flex xs10>
        <div style="margin: 8px 16px 1px">
          <v-text-field xs12 label="Goal" placeholder="프로젝트 목표를 입력해 주세요." v-model='project.project_goal' counter="20" :maxlength="20"></v-text-field>
        </div>
      </v-flex>
      <v-flex xs2 style="margin-top: 3.5px;">
        <v-select v-model="project.project_status"
          :items="status_items"
          label="프로젝트 상태"
        ></v-select>
      </v-flex>
    </v-layout>

    <v-layout wrap>
      <v-flex xs5>
        <fieldset style="margin-right:4px; height:80%">
          <legend>&nbsp;Date&nbsp;</legend>
          <v-layout wrap>
          <v-flex style="width: 17%; margin-left: 17px;">
            <v-menu
              ref="menu1"
              v-model="menu1"
              :close-on-content-click="false"
              :return-value.sync="project.project_start_date"
              transition="scale-transition"
              offset-y
              full-width
              min-width="290px"
              style="display: inline-block;"
            >
              <template v-slot:activator="{ on }">
                <v-text-field
                  v-model="project.project_start_date"
                  label="프로젝트 시작일"
                  prepend-icon="event"
                  readonly
                  v-on="on"
                ></v-text-field>
              </template>
              <v-date-picker v-model="project.project_start_date" no-title scrollable locale="ko-kr">
                <v-spacer></v-spacer>
                <v-btn text color="primary" @click="menu1 = false">Cancel</v-btn>
                <v-btn text color="primary" @click="$refs.menu1.save(project.project_start_date)">OK</v-btn>
              </v-date-picker>
            </v-menu>
          </v-flex>
        
          <span id="date_div" style="width:30px; margin-left: 10px; margin-top: 20px;">~</span>

          <v-flex style="width: 20%; margin-right: 18px;">
            <v-menu
              ref="menu2"
              v-model="menu2"
              :close-on-content-click="false"
              :return-value.sync="project.project_end_date"
              transition="scale-transition"
              offset-y
              full-width
              min-width="290px"
            >
              <template v-slot:activator="{ on }">
                <v-text-field
                  v-model="project.project_end_date"
                  label="프로젝트 마감일"
                  prepend-icon="event"
                  readonly
                  v-on="on"
                ></v-text-field>
              </template>
              <v-date-picker v-model="project.project_end_date" no-title scrollable locale="ko-kr">
                <v-spacer></v-spacer>
                <v-btn text color="primary" @click="menu2= false">Cancel</v-btn>
                <v-btn text color="primary" @click="$refs.menu2.save(project.project_end_date)">OK</v-btn>
              </v-date-picker>
            </v-menu>
          </v-flex>
          </v-layout>
        </fieldset>
      </v-flex>

      <v-flex xs7>
        <fieldset style="margin-right:4px; height:80%">
        <legend>&nbsp;git URL&nbsp;</legend>
        <div style="margin-left: 10px; margin-right: 10px; padding-bottom: 30px;">
           <v-text-field v-model="project.project_git_url"
            label="git url을 입력해 주세요." counter="20" :maxlength="20"
          ></v-text-field>
        </div>
        </fieldset>
      </v-flex>
    </v-layout>

    <fieldset style="margin-top: -18px; margin-bottom: 5px; height:100%">
      <legend>PICTURE</legend>
        <label style="margin-left: 20px;"><span style="font-size: 18px; font-weight: 500;">Files&nbsp;&nbsp;</span>
          <input type="file" id="files" ref="files" @change="onFilePicked"
          style="border: 2px solid rgb(231, 241, 247); padding: 1px 1px 0px 0.5px; border-radius: 3px;"/>
        </label>

        <v-btn
          small
          style="border-radius: 15px; margin-left:16px;"
          v-on:click="addFiles()"
          color="blue lighten-2"
        >
          Add Files
          <v-icon right dark style="margin-left: -0.1px;">add</v-icon>
        </v-btn>
        <div style="height: 10px"></div>

        <div v-for="(image, key) in updateimgs" :key="key" class="file-listing" style="margin-left: 20px; margin-bottom: 5px;">
          <img :src="image.imgurl" width="30px" height="30px">
          <v-btn class="remove-file" v-on:click="removeImage( key, image )" dark small style="border-radius: 15px;">Remove</v-btn>
        </div>
        <div v-for="(newfile, key) in newfiles" :key="key" class="file-listing" style="margin-left: 20px; margin-bottom: 5px;">
          <img :src="newfile" width="30px" height="30px">
          <v-btn class="remove-file" v-on:click="removeFile( key )" dark small style="border-radius: 15px;">Remove</v-btn>
        </div>
    </fieldset>

    <fieldset>
      <legend>CONTENT</legend>
      <div style="margin:16px;">
        <markdown-editor v-model="project.project_content" ref="markdownEditor">
        </markdown-editor>
      </div>
    </fieldset> 

    <v-layout wrap>
      <v-flex xs9>
        <fieldset style="margin-right:4px; height:85%">
          <legend>&nbsp;Technology&nbsp;</legend>
          <div style="margin:16px;" id="hashtag">
              <v-text-field v-model="project.project_tech" counter="20" :maxlength="20"
                label="프로젝트 주요 기술"
              ></v-text-field>
          </div>
        </fieldset>
      </v-flex>
      <v-flex xs3>
        <fieldset style="margin-left:4px; height:85%">
          <legend>&nbsp;Share&nbsp;</legend>
          <div style="margin:16px;">
            <v-radio-group v-model="project.project_share">
              <v-radio label="Public" color="primary" value="0"></v-radio>
              <v-radio label="Private" color="error" value="1"></v-radio>
            </v-radio-group>
          </div>
        </fieldset>
      </v-flex>
    </v-layout>

    <div style="text-align:center;" id="write-btn">
      <v-btn class="v-btn theme--dark" @click="updateTeamProject">확인</v-btn>
      <v-btn class="v-btn theme--dark" @click="goHome">취소</v-btn>
    </div>

  </v-flex>
</v-layout>
</div>
</template>

<script>
import { log } from 'util';
import { async } from 'q';
export default {
    name: 'TeamProjectUpdatePage',
    data() {
        return{
            img: {
                imageName: '',
                imageUrl: '',
                imageFile: '',
            },
            menu1: false,
            menu2: false,
            project: null,
            updateimgs: null,
            files: [],
            status_items: [
                {
                    text: '계획',
                    value: '계획'
                },
                {
                    text: '진행중',
                    value: '진행중'
                },
                {
                    text: '완료',
                    value: '완료'
                }
            ],
            newimg: '',
            newfiles: [],
            delfiles: []
        }
    },
    mounted() {
      this.getProject()
      // console.log(this.updateimgs)
    },
    methods: {
        goHome(){
            this.$router.push("/myproject")
        },
        getProject() {
            var data = {
                pjtNum: this.$route.params.num
            }
            this.$http.post(this.$store.state.testIp + '/teamProject/update/getProject', data)
            .then((res)=> {
                this.project = res.body.project[0]
                this.updateimgs = res.body.images
                // console.log(res)
                // console.log(this.project)
            })
        },
        addFiles(){
            this.$refs.files.click()
        },
        onFilePicked(e) {
          const files = e.target.files
          if (files[0] !== undefined) {
            this.img.imageName = files[0].name
            if (this.img.imageName.lastIndexOf('.') <= 0) {
              return
            }
            const fr = new FileReader()
            fr.readAsDataURL(files[0])
            fr.addEventListener('load', () => {
              this.img.imageUrl = fr.result
              this.img.imageFile = files[0]
              this.imgur()
            })
          } else {
            this.img.imageName = ''
            this.img.imageFile = ''
            this.img.imageUrl = ''
          }
        },

        imgur() {
          var file = this.img.imageFile
          var url = ''
          if(file != ''){
            var xmlHttpRequest = new XMLHttpRequest();
            xmlHttpRequest.open('POST', 'https://api.imgur.com/3/image/', false);
            xmlHttpRequest.setRequestHeader("Authorization", "Client-ID cec4916437ef1c8");
            xmlHttpRequest.onreadystatechange = (function() {
              if (xmlHttpRequest.readyState == 4) {
                if (xmlHttpRequest.status == 200) {
                  var result = JSON.parse(xmlHttpRequest.responseText);
                  this.img.imageUrl = result["data"]["link"]
                  url = this.img.imageUrl
                } else {
                  console.log("upload failed");
                }
              }
            }).bind(this);
            xmlHttpRequest.send(file);
          }
          this.newimg = url
          this.newfiles.push(this.newimg)
        },

        removeFile( key ){
            // console.log(key)
            this.newfiles.splice( key, 1 );
        },

        removeImage ( key, image ){
          this.updateimgs.splice(key, 1);
          var delimg = image
          this.delfiles.push(delimg)
          // console.log(this.delfiles)
        },

        async updateTeamProject(){
          var id = this.$route.params.id
          var num = this.$route.params.num

          var data = {
            pjtNum: this.project.project_num,
            project: this.project,
          }

          await this.$http.post(this.$store.state.testIp + '/teamProject/update/project', data)
            .then(async (res) => {
              console.log(res)
              for (var i=0; i < this.newfiles.length; i++){
                var data = {
                  pjtNum: num,
                  imgUrl: this.newfiles[i]
                }
                await this.$http.post(this.$store.state.testIp + '/teamProject/update/images', data)
                .then(async (res) => {
                  console.log(res.body)
                })
              }
            })
            .then(async () => {
              for (var j=0; j < this.delfiles.length; j++) {
                var data = {
                  imgNum: this.delfiles[j].imgnum
                }
                await this.$http.post(this.$store.state.testIp + '/myproject/delete/image', data)
                  .then(async (res) => {
                    console.log(res)
                })
              }
            })
            .then(async () => {
                alert("글 수정 완료");
                this.$router.push(`/teamProject/${id}/project/${num}`)
            })
        }

    }
}
</script>
