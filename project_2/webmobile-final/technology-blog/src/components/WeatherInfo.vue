<template>
<!-- <v-layout wrap fixed bottom> -->
<!-- <v-flex xs12> -->
<!-- <div v-show="!isLoading" class="loading">{{ errorMsg }}</div> -->

<v-btn fixed fab flat style="width: 100%;
    bottom: 220px;
    height: 0px;" disabled>
  <div v-show="isLoading" class="app" v-bind:style="styleObject">
    <div class="header">
      <custom-icon name="cloud" base-class="custom-icon"></custom-icon>
      {{cloud}}

      <custom-icon name="droplet" base-class="custom-icon"></custom-icon>
      {{humidity}}

      <custom-icon name="wind" base-class="custom-icon"></custom-icon>
      {{wind}}
    </div>

    <v-layout row>
      <div class="temperature">
        {{ temperature }}
      </div>
      <div>
        <div class="weatherIcon">
          <custom-icon :name="weatherIconName" base-class="custom-icon"></custom-icon>
        </div>
        <div class="description">
          {{ description }}
        </div>
      </div>
    </v-layout>
    <div class="city">
      {{ geocity }}
    </div>
  </div>
</v-btn>
</template>

<script>
import customIcon from 'vue-icon/lib/vue-feather.esm'

export default {
  name: 'Weather',
  components: {
    customIcon
  },
  data() {
    return {
      dataObj: null,
      latitude: 0.0,
      longitude: 0.0,
      cloud: null,
      humidity: null,
      wind: null,
      temperature: null,
      city: '',
      geocity: '',
      description: '',
      errorMsg: 'Loading...',
      baseClass: 'v-icon',
      styleObject: {
        background: ''
      },
      isLoading: false,
      apikey: '4b82281a523a9d0e0d3e30b2d69ba86c',
      geokey: 'AIzaSyDdXAXSBfUzZ6ZubYxYKVd8f54TGZZy67s',
    }
  },
  computed: {
    weatherIconName: function() {
      if (this.dataObj != null) {
        var weatherID = this.dataObj.weather[0].id;
        this.styleObject.background = "rgba(255, 255, 255,0)";
        if (weatherID >= 200 && weatherID <= 232) {
          // this.styleObject.background = 'linear-gradient(45deg, #00ECBC, #007ADF)';
          return 'cloud-lightning';
        } else if (weatherID >= 300 && weatherID <= 321) {
          // this.styleObject.background = 'linear-gradient(45deg, #89F7FE, #66A6FF)';
          return 'cloud-drizzle';
        } else if (weatherID >= 500 && weatherID <= 531) {
          // this.styleObject.background = 'linear-gradient(45deg, #00C6FB, #005BEA)';
          return 'cloud-rain';
        } else if (weatherID >= 600 && weatherID <= 622) {
          // this.styleObject.background = 'linear-gradient(45deg, #7DE2FC, #B9B6E5)';
          return 'cloud-snow';
        } else if (weatherID >= 701 && weatherID <= 781) {
          // this.styleObject.background = 'linear-gradient(45deg, #D7D2CC, #304352)';
          return 'cloud';
        } else if (weatherID == 800) {
          // this.styleObject.background = 'linear-gradient(45deg, #FEF253, #FF7300)';
          return 'sun';
        } else if (weatherID >= 801 && weatherID <= 804) {
          // this.styleObject.background = 'linear-gradient(45deg, #17ead9, #6078ea)';
          return 'cloud';
        } else {
          // this.styleObject.background = 'linear-gradient(45deg, #17ead9, #6078ea)'
          return 'alert-circle'
        }
      }
      // this.styleObject.background = 'linear-gradient(45deg, #17ead9, #6078ea)'
      return 'alert-circle';
    }
  },
  methods: {
    getLocation: function() {
      if (!navigator.geolocation) {
        this.errorMsg = "Geolocation is not supported by your browser";
        this.city = this.errorMsg;
        // console.warn(this.errorMsg);
        return;
      }
      var options = {
        timeout: 10000
      };
      navigator.geolocation.getCurrentPosition(this.success, this.error, options);
    },
    success: function(position) {
      // console.log(position);
      this.latitude = position.coords.latitude;
      this.longitude = position.coords.longitude;
      this.latitude = parseFloat(this.latitude).toFixed(2);
      this.longitude = parseFloat(this.longitude).toFixed(2);
      // console.log(this.latitude)
      // console.log(this.longitude)
      this.getWeather();
    },
    error: function(err) {
      this.errorMsg = "Unable to retrieve your location";
      this.city = this.errorMsg;

      // console.warn(`ERROR(${err.code}): ${err.message}`);
      // console.warn(this.errorMsg);
    },
    getWeather: function() {
      var reqURL = 'https://cors-anywhere.herokuapp.com/http://api.openweathermap.org/data/2.5/weather?lat=' + this.latitude + '&lon=' + this.longitude + '&lan=kr' + '&APPID=' + this.apikey;
      this.$http.get(reqURL, {
        headers: {
          'x-requested-with': 'XMLHttpRequest'
        }
      }).then(function(response) {
        // console.log(response)
        this.dataObj = response.data;
        this.cloud = (this.dataObj.clouds.all) + '%';
        this.wind = (this.dataObj.wind.speed.toFixed(1)) + 'm/s';
        this.humidity = (this.dataObj.main.humidity) + '%';
        this.temperature = (this.dataObj.main.temp - 273.15).toFixed(0) + 'º';
        this.city = this.dataObj.name + ', ' + this.dataObj.sys.country;
        this.description = this.dataObj.weather[0].main;
        this.isLoading = true;

        // this.getCity();
      }, function(response) {
        // console.log('error');
        // console.log(response);
        this.errorMsg = "Unable to retrive weather information.";
      });
    },
    getCity: function() {
      // var geoURL = 'https://maps.googleapis.com/maps/api/geocode/json?sensor=false&key=AIzaSyDdXAXSBfUzZ6ZubYxYKVd8f54TGZZy67s&language=ko&latlng=36.46,127.12'
      var geoURL = 'https://maps.googleapis.com/maps/api/geocode/json?sensor=false&key=' + this.geokey + '&language=ko&latlng=' + this.latitude + ',' + this.longitude;
      this.$http.get(geoURL).then(function(res) {
        // console.log(res);
        // console.log(res.body);

        var newarr = new Array();
        var geo = res.body.results[0].formatted_address;
        geo = geo.split(' ');
        // console.log(geo)

        this.geocity = res.body.plus_code.compound_code;
        var arr = new Array();
        var arr = this.geocity.split(' ');

        this.geocity = arr[arr.length - 1]
        var special = '특별시';
        var metro = '광역시';

        if (this.geocity.indexOf(metro) !== -1 || this.geocity.indexOf(special) !== -1) {
          this.geocity = geo[1] + ' ' + geo[2]
          // console.log(this.geocity);
        } else {
          this.geocity = geo[2] + ' ' + geo[3]
          // console.log(this.geocity);
        }

        // console.log(this.geocity);

      })
    },
  },
  created() {
    this.getLocation();
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css?family=Open+Sans');

.loading {
  font-family: 'Open Sans', sans-serif;
  -webkit-font-smoothing: antialiased;
  color: rgba(0, 0, 0, 1);
  width: 100vw;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.app {
  font-family: 'Open Sans', sans-serif;
  -webkit-font-smoothing: antialiased;
  /* color: rgba(255, 255, 255, 0.9); */
  color: #666;
  text-transform: uppercase;
  font-weight: 700;
  height: 100vh;
  width: 100vw;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  /* background: linear-gradient(45deg, #17ead9, #6078ea); */
  border-radius: 5px;
  /* box-shadow: 0 19px 38px rgba(0, 0, 0, .3), 0 15px 12px rgba(0, 0, 0, .22); */
}

@media (min-width: 450px) {
  .app {
    width: 100%;
    height: 220px;
    border-radius: 5px;
  }
}

#weather {
  position: fixed;
  width: 100%;
}


.header {
  width: 90%;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  padding-top: 10px;
  text-transform: lowercase;
}

.header svg {
  vertical-align: top;
  margin-right: -10px;
}

.temperature {
  font-size: 5em;
  padding-left: 10px;
  padding-top: 20px;
}

.city {
  font-size: 2em;
  padding-bottom: 20px;
}

.description {
  font-size: 1.7em;
  text-transform: lowercase;
}

.description::first-letter {
  text-transform: uppercase;
}

.weatherIcon {
  padding-top: 20px;
}

.weatherIcon svg {
  width: 3em;
  height: 3em;
  margin-left: 10px;
}

.v-icon,
.custom-icon {
  width: 25px;
  height: 25px;
}
</style>
