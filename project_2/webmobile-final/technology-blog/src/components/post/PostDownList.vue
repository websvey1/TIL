<template>
<v-layout wrap v-if="posts.length > 0">
  <v-flex v-for="post in posts" xs12 mt-1 px-2>
    <PostDownCard :post="post"></PostDownCard>
  </v-flex>
</v-layout>
<v-layout v-else wrap>
  <v-flex xs12 px-2 mt-4 style="margin-bottom: 35px;">
    <h1 style="margin-top:50px;text-align:center;">POST가 없습니다.</h1>
  </v-flex>
</v-layout>
<!--
<v-layout v-else wrap style="display:flex; justify-content:center; margin:0 20%; padding: 70px 0;">
    <img src="@/assets/crying.png" style="width:30%; position:relative;"/>
    <h1 style="margin:50px 0;">검색한 내용에 해당하는 POST가 없습니다.</h1>
</v-layout>
-->
</template>

<script>
import PostDownCard from '@/components/post/PostDownCard'

export default {
  name: "PostDownList",
  components: {
    PostDownCard
  },
  data() {
    return {

    }
  },
  props:{
    posts:{}
  },
  created(){

  },
  methods: {

  },
  mounted() {
    alert(posts.length)
  }
}
</script>

<style media="screen">

</style>
