<template>
    <v-btn @click="trans()">
        translate
    </v-btn>
</template>

<script>
import router from '@/router'

export default {
    name: "Translate",
    data(){
        return{

        }
    },
    methods:{
        trans(){
            if(this.$session.has("trans")){
                this.$session.remove("trans")
                router.push("/");
            }else{
                this.$session.set("trans", true)
                console.log(this.$session.get("trans"))
                router.push("/");
            }
        }
    }
}
</script>
