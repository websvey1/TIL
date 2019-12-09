<template>
<div style="background-color: white;">
  <div class="container">
    <div id="cardtest">
    <ListTest/>
    </div>
  </div>
</div>
</template>

<script>
import CardTest from '@/components/CardTest'
import ListTest from '@/components/ListTest'

export default {
    name: 'PostTest',
    components:{
        CardTest,
        ListTest,
    },
    data() {
        return {
        }
    },
	methods: {
        showCalendar(){
            window.open("Calendar", "_blank","width=1100,height=700,left=200,top=25");
        }
	},
  created(){

  },
  beforeRouteLeave(to, from, next){

    next();
  },
  destroyed(){

  }
}
</script>

<style scoped>
  #cardtest {
    background-color: white;
    width: 85%;
    margin: 0 auto;
  }
</style>
