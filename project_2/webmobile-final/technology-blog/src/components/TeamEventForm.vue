<template>
<form @submit.prevent="handleSubmit">
  <div class="input2">
    <v-select :error-messages="['Please select a team']" label="　Team" :items="teamList" v-model="team" item-text="team_name" return-object></v-select>
  </div>
  <div class="input-holder">
    <input type="text" placeholder="Event title" v-model="event.title" />
  </div>
  <div class="input-holder">
    <date-picker :placeholder="'Start date'" v-model="event.start" />
  </div>
  <div class="input-holder">
    <date-picker :placeholder="'End date'" v-model="event.end" />
  </div>
  <div class="input-holder">
    <textarea placeholder="Event description" rows="4" v-model="event.data.description"></textarea>
  </div>
  <h4 class="header">Select event theme</h4>
  <div class="theme">
    <color-picker @colorPicked="selectColor" :color="event.cssClass" />
  </div>
  <div class="input-holder2">
    <button type="submit">Schedule</button>
  </div>
</form>
</template>

<script>
import DatePicker from 'vuejs-datepicker';
import format from 'date-fns/format';
import ColorPicker from './ColorPicker';

export default {
  name: 'TeamEventForm',
  components: {
    DatePicker,
    ColorPicker
  },
  data() {
    return {
      team:'',
      event: {
        team: '',
        title: '',
        start: '',
        end: '',
        cssClass: '',
        data: {
          description: ''
        }
      },
      teamList: []
    }
  },
  watch:{
    team (v){
      this.$store.state.calendarTeam = v;
      this.$emit('selectTeam');
    }
  },
  mounted(){
    this.getTeam();
  },
  methods: {
    getTeam(){
      var data = {
        num: this.$session.get('userInfo').user_num
      }

      this.$http.post(this.$store.state.testIp + '/team/getTeamList', data)
      .then((response) => {
        this.teamList = response.data;
        // for(var i = 0; i < response.body.length; i++){
        //   this.teamList.push(response.body[i].team_name)
        // }
      })
      .catch((error) => {
        console.log(error)
      })
    },
    async handleSubmit() {
      if(this.team.team_name == ''){
        alert("Please select a team")
        return
      }
      var data = {
        num: this.$session.get('userInfo').user_num,
        teamName: this.team.team_name
      }
      this.$http.post(this.$store.state.testIp + '/team/getTeamNum', data)
      .then((response) => {
        // console.log(response.body[0].team_num)
        const start = format(this.event.start, 'YYYY-MM-DD');
        const end = format(this.event.end, 'YYYY-MM-DD');
        if(start > end){
          alert("Start date should be earlier than End date")
          this.resetValues();
          return
        }
        const event = {
          ...this.event,
          start,
          end
        }
        var config = {
          // body: JSON.stringify(event),
          body: {
            title: event.title,
            start: event.start,
            end: event.end,
            cssClass: event.cssClass,
            description: event.data.description,
            teamNum: response.body[0].team_num
          },
          headers: {
            'Access-Control-Allow-Origin': '*',
            'content-type': 'application/json'
          },
          data: {
            num: this.$session.get('userInfo').user_num
          }
        }

        this.$http.post(this.$store.state.testIp + '/plan/team', config)
          .then((response) => {
            this.$store.state.teamPlan = true;
            this.resetValues();
          })
          .catch((error) => {
            console.log(error)
          })
      })
      .catch((error) => {
        console.log(error)
      })
    },
    selectColor(color) {
      this.event = {
        ...this.event,
        cssClass: color
      }
    },
    resetValues() {
      this.event = {
        team: '',
        title: '',
        start: '',
        end: '',
        cssClass: '',
        data: {
          description: ''
        }
      }
    }
  }
}
</script>

<style>
form {
  display: fix;
  flex-direction: column;
  /* margin-left: 30px; */
}

.input-holder {
  margin: 10px 0;
  display: flex;
  /* justify-content: flex-start; */
  width: 77%;
  border: 1px solid rgba(0, 0, 0, 0.2);
}
.input2{
  width: 77%;
  /* border: 1px solid rgba(0, 0, 0, 0.2); */
}

.input-holder input,
.input-holder textarea {
  padding: 12px 15px;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 0;
  width: 100%;
  opacity: 0.8;
  font-size: 15px;
  font-weight: normal;
  color: black !important;
}

.input-holder input:focus,
.input-holder textarea:focus,
.input-holder button:focus {
  border: 1.5px solid rgb(0, 0, 0);
  outline: none;
  box-shadow: 0 2px 3px 1px rgba(0, 0, 0, 0.2);
}

.vdp-datepicker {
  width: 100%;
}

.vdp-datepicker>div>input {
  width: 100%;
}

.input-holder2>button {
  justify-self: center;
  padding: 12px 25px;
  border-radius: 0;
  text-transform: uppercase;
  font-weight: 600;
  background: rgb(97, 97, 97);
  color: white;
  border: none;
  font-size: 14px;
  letter-spacing: -0.1px;
  cursor: pointer;
}

.theme {
  padding-top: 5%;
  padding-bottom: 10%;
}
</style>
