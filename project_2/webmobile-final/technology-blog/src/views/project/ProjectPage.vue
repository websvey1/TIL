<template>
<div style="background-color: white;">
  <v-layout v-if="!search" wrap row pa-3>
    <v-flex fill-height d-flex>
      <div class="container">
        <div style="width: 91%; margin: 0 auto;">
          <div style="width:210px; display:inline-block; margin-bottom: 18px;">
            <v-select v-model="categoryForPostlist" :items="categorysForPostlist" item-text="text" :menu-props="{ top: true, offsetY: true }" label="Category" return-object></v-select>
          </div>

          <div style="float:right; display: inline-block; margin-top: -5px; ">
            <div style="display: inline-block; margin: 5px; max-width: 130px;">
              <v-select v-model="categoryForSearch" :items="categorysForSearch" item-text="text" :menu-props="{ top: true, offsetY: true }" label="Category" return-object></v-select>
            </div>
            <div style="display: inline-block; margin: 5px; max-width: 200px;">
              <v-text-field xs12 label="검색어를 입력해 주세요." v-model='textForSearch'></v-text-field>
            </div>
            <div style="display: inline-block; margin: 5px 0px; vertical-align: center;">
              <v-btn fab dark small color="black" @click="searchPosts" style="margin-top: 12px;">
                <v-icon dark>fas fa-search</v-icon>
              </v-btn>
            </div>
          </div>
        </div>
        <div style="width: 100%; margin: 0 auto;">
       <ProjectList ref="project"></ProjectList>
       </div>
      </div>
    </v-flex>
  </v-layout>

  <v-layout v-else wrap row pa-3>
    <v-flex fill-height d-flex>
      <div class="container">
        <div style="width: 89%; margin: 0 auto;">
          <div style="width:210px; display:inline-block; margin-bottom: 18px;">
            <v-select v-model="categoryForPostlist" :items="categorysForPostlist" item-text="text" :menu-props="{ top: true, offsetY: true }" label="Category" return-object></v-select>
          </div>

          <div style="float:right; display: inline-block; margin-top: -5px; ">
            <div style="display: inline-block; margin: 5px; max-width: 130px;">
              <v-select v-model="categoryForSearch" :items="categorysForSearch" item-text="text" :menu-props="{ top: true, offsetY: true }" label="Category" return-object></v-select>
            </div>
            <div style="display: inline-block; margin: 5px; max-width: 200px;">
              <v-text-field xs12 label="검색어를 입력해 주세요." v-model='textForSearch'></v-text-field>
            </div>
            <div style="display: inline-block; margin: 5px 0px; vertical-align: center;">
              <v-btn fab dark small color="black" @click="searchPosts" style="margin-top: 12px;">
                <v-icon dark>fas fa-search</v-icon>
              </v-btn>
              <v-btn class="v-btn theme--dark" @click="allPosts">전체글 보기</v-btn>
            </div>
          </div>
        </div>
        <div style="width: 100%; margin: 0 auto;">
       <ProjectList ref="project"></ProjectList>
       </div>
      </div>
    </v-flex>
  </v-layout>
</div>
</template>

<script>
import ProjectList from '@/components/ProjectList'
import ProjectCard from '@/components/ProjectCard'

export default {
    name: 'ProjectPage',
    components: {
        ProjectList,
        ProjectCard
    },
    data() {
        return {
          search:false,
          searchResult:'',
          searchContent:{
            category:'',
            text:''
          },

          categorysForSearch: [
            {text:'제목', value:'0'},
            {text:'내용', value:'1'},
            // {text:'제목 + 내용', value:'2'},
            // {text:'ID', value:'3'},
            // {text:'TAG', value:'4'},
          ],

          textForSearch: '',
          categoryForSearch: {text:'제목', value:'0'} ,

          categorysForPostlist: [
            {text: 'Personal Project', value: '0'},{text: 'Team Project', value: '1'}
          ],
          categoryForPostlist:{text: 'Personal Project', value: '0'},

          categorysForPostlistBySearch: [
            {text: 'Personal Project', value: '0'},{text: 'Team Project', value: '1'}
          ],
          categoryForPostlistBySearch:{text: 'Personal Project', value: '0'},

          page: 1,
          length: 1,
          totalVisible: 7
        }
    },
    watch:{
      categoryForPostlist(){
        this.textForSearch = ''
        this.$refs.project.selectProject(this.categoryForPostlist.value, this.categoryForSearch.value, this.textForSearch);
      }
    },
    methods: {
      searchPosts(){
        if(this.textForSearch == ''){
                alert("검색할 단어 혹은 문구를 입력해주세요.")
            }
        else{
          this.$refs.project.selectProject(this.categoryForPostlist.value, this.categoryForSearch.value, this.textForSearch);
        }
        
      },
      allPosts(){
        if(this.search){
         this.search = false;
       }
        this.$refs.project.selectProject(this.categoryForPostlist.value, '', '');
      }
    }

 }
 </script>

 <style scoped>
 #page {
   background-color: white;
   width: 90%;
   height: 100%;
   margin: 0 auto;
 }
 </style>
