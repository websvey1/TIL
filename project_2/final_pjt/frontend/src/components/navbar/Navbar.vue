<template>
    <ul class="navbar">
        <li><router-link to="/">NAMBIGATION</router-link></li>
        <li v-if="!data" style="float:right"><router-link class="active" to="/User">User</router-link></li>
        <li v-else style="float:right"><Logout/></li>
    </ul>
</template>

<script>
import Logout from '../auth/Logout'

export default {
    name: "Navbar",
    components: {
        Logout,
    },
    data() {
        return {
            data: "",
        }
    },
    created() {
        this.data = JSON.parse(sessionStorage.getItem('userinfo'))
    },

}
</script>

<style>
.navbar {
    
}
ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  background-color: green;
  position: fixed;
  top: 0;
  width: 100%;
}

li {
  float: left;
}

li a {
  display: block;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

/* Change the link color to #111 (black) on hover */
li a:hover {
  opacity: 0.5;
}
</style>