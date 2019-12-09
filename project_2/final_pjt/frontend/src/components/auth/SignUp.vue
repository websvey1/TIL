<template>
    <div class="div-signup">
        <h1>회원가입</h1>
        <input class="input-signup" type="text" v-model="userid" placeholder="ID"><br>
        <input class="input-signup" type="password" v-model="password" placeholder="Password"><br>
        <input class="input-signup" type="text" v-on:keyup.enter="Ingredient_save()" id="ingredient" v-model="ingredient" placeholder="재료"><br>
        <div class="md-chips" id="md-chips"></div>
        <button class="btn-signup" @click="SignUp()">가입</button>
        <router-link class="btn-signup" to="/User" tag="button">로그인</router-link>
    </div>

</template>

<script>
export default {
    name: 'SignUp',
    data() {
        return {
            userid: "",
            password: "",
            ingredient: "",
            ingredients: [],
        }
    },
    mounted() {
        document.getElementById('md-chips').onclick = (res) => {
            if (res.path[0].id) {
                this.Ingredient_delete(res.path[0].id)
            }
        };
    },
    methods: {
        SignUp: function() {
            this.$http.post('/api/users/create/', {userid: this.userid, password: this.password, ingredients: this.ingredients})
                .then((response) => {
                    if (response.data) {
                        alert('Success')
                        window.location.href = '/User';
                    } else {
                        alert('이미 사용중인 ID입니다.')
                    }
                })
                .catch(function (error) {
                    alert('error message: ' + error)
                })
        },
        Ingredient_save: function() {
            if (this.ingredient.split(' ') == this.ingredient) {
                $('.md-chips').append(`<div class="md-chip" id="${this.ingredient}">
                                        <span>${this.ingredient}</span>
                                        <button type="button" id="${this.ingredient}" class="md-chip-remove">
                                        </button>
                                    </div>`)
                this.ingredients.push(this.ingredient)
                this.ingredient = ""
            }
        },
        Ingredient_delete(ingredient_data) {
            var cnt = 0
            this.ingredients.some(element => {
                if (element === ingredient_data){
                    return true
                } else {
                    cnt += 1
                }
            });
            this.ingredients.splice(cnt, 1)
            $('.md-chip').remove('#' + `${ingredient_data}`)
        },
  },
}
</script>

<style lang="scss">
@import url(https://fonts.googleapis.com/css?family=Roboto);

$md-chip-height: 32px;
$md-chip-color: #e0e0e0;

.md-chip {
  display: inline-block;
  background: $md-chip-color;
  padding: 0 12px;
  border-radius: 32px;
  font-size: 13px;
  &.md-chip-hover:hover {
    background: #ccc;
  }
}

.md-chip-remove {
  display: inline-block;
  background: #aaa;
  border: 0;
  height: 20px;
  width: 20px;
  border-radius: 50%;
  padding: 0;
  margin: 0 -4px 0 4px;
  cursor: pointer;
  font: inherit;
  line-height: 20px;
  &:after { 
    color: $md-chip-color;
    content: 'x';
  }
  &:hover {
    background: #999;
  }
  &:active {
    background: #777;
  }
}

.md-chips {
  padding: 12px 0;
  .md-chip {
    margin: 0 5px 3px 0;
  } 
}

.div-signup {
    margin-top: 80px;
}
.input-signup {
    width: 40%;
    padding: 12px 20px;
    margin: 8px 0;
    display: inline-block;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
}
.btn-signup {
    width: 19.5%;
    background-color: green;
    color: white;
    padding: 14px 20px;
    margin: 8px 8px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}
.btn-signup:hover {
    opacity: 0.7;
}
</style>