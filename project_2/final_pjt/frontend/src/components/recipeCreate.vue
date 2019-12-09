<template></template>

<script>
import axios from "axios";
export default {
  name: "recipeCreate",
  methods: {
    create() {
      await axios
      .post('http://192.168.31.140:8080/')
      .then()
      .catch(error => {
        console.log(error);
      })

    }
  }
};
</script>

<style>
</style>