<template>
  <div>
    <Header/>
    <v-app>
      <v-content>
        <router-view/>
      </v-content>
    </v-app>
    <Footer/>
  </div>
</template>

<script>
import Header from './components/common/Header'
import Footer from './components/common/Footer'

export default {
  name: 'App',
  components: {
    Footer,
    Header,
  },
  data () {
    return {

    }
  },
  created(){

  },
  mounted(){
    this.firstCheck();
    this.messageCheck();
  },
  methods:{
    firstCheck(){
      if(this.$session.has('userInfo')){
        var data = {
          id : this.$session.get('userInfo').user_num
        }
        this.$http.post(this.$store.state.testIp + '/team/checkNew', data)
        .then((response) => {
          if(response.body[0].total > 0){
            this.$store.state.exist = true
          }else{
            this.$store.state.exist = false
          }
        })
        .catch((error) => {
          console.log(error)
        })
      }
    },
    messageCheck() {
      if (this.$session.has('userInfo')){
        var data = {
          id : this.$session.get('userInfo').user_num
        }
        this.$http.post(this.$store.state.testIp + '/another/checkNew', data)
        .then((response) => {
          console.log(response.body)
        })
        .catch((error) => {
          console.log(error)
        })
      }
    }
  }
}
</script>

<style>

</style>
