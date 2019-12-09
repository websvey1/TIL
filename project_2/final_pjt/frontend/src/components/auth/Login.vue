<template>
    <div class="div-login">
        <h1>로그인</h1>
        <input class="input-login" type="text" v-model="userid" placeholder="ID"><br>
        <input class="input-login" type="password" v-model="password" placeholder="Password"><br>
        <button class="btn-login" @click="Login()">로그인</button>
        <router-link class="btn-login" to="/User/SignUp" tag="button">회원가입</router-link>
    </div>
</template>

<script>
export default {
    name: 'Login',
    data() {
        return {
            userid: "",
            password: "",
        }
    },
    methods: {
        Login: function() {
            this.$http.post('/api/users/login/', {userid: this.userid, password: this.password})
                .then((response) => {
                    sessionStorage.setItem('userinfo', JSON.stringify({userid: response.data.userid, ingredients: response.data.ingredients}))
                    alert('Login')
                    window.location.href = '/';
                })
                .catch(function (error) {
                    alert('error message: ' + error)
                })
        }
    },
}
</script>

<style>
.div-login {
    margin-top: 80px;
}
.input-login {
    width: 40%;
    padding: 12px 20px;
    margin: 8px 0;
    display: inline-block;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
}
.btn-login {
    width: 19.5%;
    background-color: green;
    color: white;
    padding: 14px 20px;
    margin: 8px 8px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}
.btn-login:hover {
    opacity: 0.7;
}
</style>