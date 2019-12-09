<template>
<v-layout v-if="!$store.state.isTrans" wrap>
  <v-btn flat color="warning" @click="showCalendar()">Calendar</v-btn>
  <v-flex v-if="isVisible(post)" v-for="post in $store.state.posts" xs12 px-2 style="margin-bottom: 35px;">
    <CardTest :post="post"></CardTest>
  </v-flex>
</v-layout>
<v-layout v-else wrap>
  <v-btn flat color="warning" @click="showCalendar()">Calendar</v-btn>
  <v-flex v-if="isVisible(post)" v-for="post in $store.state.trans_posts" xs12 px-2 style="margin-bottom: 45px;">
    <CardTest :post="post"></CardTest>
  </v-flex>
</v-layout>
</template>

<script>
import CardTest from './CardTest'

export default {
  name: "ListTest",
  components: {
    CardTest
  },
  data() {
    return {

    }
  },
  methods: {
    showCalendar(){
      window.open("Temp", "_blank","width=1100,height=700,left=200,top=25");
    },
    isVisible(post){
      if(post.visibility == 'true' || (this.$store.state.userInfo != null &&post.visibility == 'false' && post.email == this.$store.state.userInfo.email)){
          return true;
      }
      else{
        return false;
      }
    }
  },
  mounted(){

  }
}
</script>

<style media="screen">
</style>
