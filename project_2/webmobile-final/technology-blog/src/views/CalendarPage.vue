<template>
  <div >
    <div id="app">
      <div class="main2" >
        <div class="calendar-holder">
          <calendar :events="events" />
        </div>

        <div class="form-holder">
          <event-form />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Calendar from '@/components/Calendar.vue'
import EventForm from '@/components/EventForm.vue'
import {mapState} from 'vuex';

export default {
  name: 'CalendarPage',
  components: {
    Calendar,
    EventForm
  },
  data(){
    return {
      events: []
    }
  },
  async created() {
    if (this.$session.has('userInfo')) {
      await this.getCal();
    } else {
      alert("로그인 해주세요.");
      this.$router.push("/");
    }
  },
  mounted(){
  //  this.getCal();
  },
  computed:
    mapState(['plan'])
  ,
  watch: {
    plan(to, from){
      if(from == false && to == true){
        this.$store.state.plan = false;
        this.events = [];
        this.getCal();
      }
    }
  },
  methods:{
    getCal(){
       var data = {
        num : this.$session.get('userInfo').user_num
    }
    this.$http.post(this.$store.state.testIp + '/plan/getPlan', data)
      .then((response) => {
        var items = response.body;

        for(var i = 0; i < items.length; i++){
          this.events.push({title: items[i].cal_title, start: items[i].cal_start,
                  end: items[i].cal_end, cssClass: items[i].cal_color, description: items[i].cal_description});
        }
      })
      .catch((error) =>{
        console.log(error)
      })
    }
  }
}
</script>

<style scoped>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    /* text-align: center; */
    color: #2c3e50;
    background-color: rgb(255, 255, 255);
  }
  .main2 {
    padding: 0 5% 10% 10%;
    display: flex;
    align-items: center;
  }

  .calendar-holder {
    width: 65%;
  }

  .form-holder {
    padding-left: 5%;
    width: 35%;
  }
  .form-holder > h3 {
    color: rgb(0, 0, 0);
    text-transform: uppercase;
    font-size: 16px;
    text-align: left;
  }

</style>
