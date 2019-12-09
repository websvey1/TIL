<template>
  <div>
    <div id="app">
      <div class="main2">
        <div class="calendar-holder">
          <team-calendar :events="events" />
        </div>

        <div class="form-holder">
          <h3>Schedule an event</h3>
          <team-event-form v-on:selectTeam="getCal"/>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import TeamCalendar from '@/components/TeamCalendar.vue'
import TeamEventForm from '@/components/TeamEventForm.vue'
import {mapState} from 'vuex';

export default {
  name: 'TeamCalendarPage',
  components: {
    TeamCalendar,
    TeamEventForm
  },
  data(){
    return {
      events: []
    }
  },
  async created() {
    if (this.$session.has('userInfo')) {
      // await this.getCal();
    } else {
      alert("로그인 해주세요.");
      this.$router.push("/");
    }
  },
  mounted(){
    // this.getCal();
  },
  computed:
    mapState(['teamPlan'])
  ,
  watch: {
    teamPlan(to, from){
      if(from == false && to == true){
        this.$store.state.teamPlan = false;
        this.events = [];
        this.getCal();
      }
    }
  },
  methods:{
    selectTeam(){

    },
    getCal(){
      var data = {
        num : this.$session.get('userInfo').user_num,
        team : this.$store.state.calendarTeam.team_num
      }
      this.events = [];
      this.$http.post(this.$store.state.testIp + '/plan/getTeamPlan', data)
      .then((response) => {
        var items = response.body;

        for(var i = 0; i < items.length; i++){
          this.events.push({title: items[i].cal_title, start: items[i].cal_start,
                  end: items[i].cal_end, cssClass: items[i].cal_color, description: items[i].cal_description, team: items[i].cal_teamNum});
        }
      })
      .catch((error) =>{
        console.log(error)
      })
    }
  }
}
</script>

<style>
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
  padding-top: 3%;
}

.form-holder {
  padding-left: 5%;
  width: 35%;
}
.form-holder > h3 {
  color: rgba(0, 0, 0, 0);
  text-transform: uppercase;
  font-size: 16px;
  text-align: left;
}
</style>
