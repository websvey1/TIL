<template>
  <div id="app">
    <Navbar/>
      <v-content>
        <router-view></router-view>
      </v-content>
  </div>
</template>

<script>
import Navbar from './components/navbar/Navbar'

export default {
  name: 'app',
  components: {
    Navbar,
  }
}
</script>

<style>
body {
  margin: 0px;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
