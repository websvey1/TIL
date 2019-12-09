<template>
    <a class="a-logout" @click="Logout()">로그아웃</a>
</template>

<script>
export default {
    name: 'Logout',
    data() {
        return {
            data: ""
        }
    },
    created() {
        this.data = JSON.parse(sessionStorage.getItem('userinfo'))
    },
    methods: {
        Logout: function() {
            sessionStorage.removeItem("userinfo");
            window.location.href = '/';
        },
    }
}
</script>

<style>
.a-logout {
    cursor: pointer;
}
</style>