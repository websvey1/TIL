<template>
    <div style="margin-top:80px;">
        
    </div>
</template>

<script>
export default {
    name: 'MainHomePage',
    components: {
    },
    data() {
        return {
            data: ""
        }
    },
    created() {
        this.data = JSON.parse(sessionStorage.getItem('userinfo'))
    },
}
</script>

<style>

</style>