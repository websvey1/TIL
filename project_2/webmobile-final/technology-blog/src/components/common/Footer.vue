<template>
  <v-app>
    <v-footer class="pa-3" height="auto" width="100%" style="margin-top:200px; background-color: rgb(255, 255, 255); border:1px solid rgb(200, 200, 200)">
      <v-layout wrap row justify-center xs12 align-end>
          <button @click="myFunction()">Git Lab</button>

          &nbsp; / &nbsp;

          <div>
            &copy; {{ new Date().getFullYear() }}
          </div>
      </v-layout>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  name: 'Footer',
  components: {

  },
  methods:{
      go: function () {
        window.location = "https://lab.ssafy.com/dpwl7484/webmobile-sub2/";
      },
      myFunction: function () {
          window.open("https://lab.ssafy.com/dpwl7484/webmobile-sub2/", "_blank","width=1000,height=600,left=250,top=100");
      }
    }
}
</script>
