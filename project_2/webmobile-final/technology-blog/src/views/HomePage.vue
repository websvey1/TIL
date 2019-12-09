<template>
<div class="body">
  <v-img height="100%" width="auto" src="https://blog.newrelic.com/wp-content/uploads/good-programmer-banner-final.jpg">
      <div style="color:white; font-size:30px;padding:5% 5%;">
      개인 프로젝트 및 팀 프로젝트의 계획 및
      <br/>
      진행 상황 등을 관리하는 플랫폼을 제공합니다.
      <br/>
      <br/>
      자유롭게 이용하세요!<br/>
      </div>
  </v-img>
    <div class="container">
        <div class="website">
            <div class="main-page" style="position:relative; z-index:2;">

                <PostList></PostList>
            </div>
        </div>
    </div>
</div>
</template>


<script>
import PostList from '@/components/post/PostList'
import Weather from '@/components/WeatherInfo'

export default {
    name: 'HomePage',
    components: {
        PostList,
        Weather,
    },
    data() {
        return {
            drawer: null,
            items: [{
                title: 'Home',
                icon: 'home',
                link: '/'
            },
            {
                title: 'Project',
                icon: 'widgets',
                link: '/project'
            }
            ]
        }
    },
    created(){

    },
    mounted(){

    },
    beforeRouteLeave(to, from, next){
      next();
    },
    methods: {

    },
}
</script>

<style scoped>
    #SSAFY {
    font-family: 'Lato', sans-serif;
    font-size: 60px;
    color:rgb(63, 63, 63)
    }
</style>
