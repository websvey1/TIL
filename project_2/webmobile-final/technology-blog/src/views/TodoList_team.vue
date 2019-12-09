<template>
<v-app>
<v-container style="padding-bottom:50px;">

  <v-layout row style="min-height:400px; margin-top:40px;">

    <v-flex xs12 class="Todo">
        <h2>해야할 일</h2>
        <draggable v-model="myArray1" group="people" @start="drag=true" @end="drag=false">
          <div v-for="element in myArray1" :key="element.id">
            <v-chip color="#C8E6C9">{{element.todo_content}} <v-icon style="margin-left:10px;"color="rgb(0, 0, 0, 0.5)">clear</v-icon></v-chip>

          </div>
      </draggable>
    </v-flex>

    <v-flex xs12 class="Todo">
     <h2>하고 있는 일</h2>
      <draggable v-model="myArray2" group="people" @start="drag=true" @end="drag=false">
        <div v-for="element in myArray2" :key="element.id">
          <v-chip color="rgb(191, 234, 255)">{{element.todo_content}} <v-icon style="margin-left:10px;"color="rgb(0, 0, 0, 0.5)">clear</v-icon></v-chip>
        </div>
      </draggable>
      </v-flex>

    <v-flex xs12 class="Todo">
      <h2>완성한 일</h2>
      <draggable v-model="myArray3" group="people" @start="drag=true" @end="drag=false">
        <div v-for="element in myArray3" :key="element.id">
          <v-chip color="#FFCDD2">{{element.todo_content}} <v-icon style="margin-left:10px;"color="rgb(0, 0, 0, 0.5)">clear</v-icon></v-chip>
        </div>
      </draggable>
    </v-flex>

  </v-layout>


  <!-- v-model이 binding 해주는 역할 bind=연결 -->
  <div style="display:flex; justify-content:center; margin-top:50px; margin-bottom:20px;">
    <v-btn class="v-btn theme--dark" @click="openDialog">추가</v-btn>
    <v-btn class="v-btn theme--dark" @click="updateTodo">저장</v-btn>
  </div>

  <v-dialog hide-overlay v-model="dialog" persistent max-width="400px">
    <v-card>
      <v-card-title style="display:flex; justify-content:center; padding-top:30px;">
        <h2> 할 일을 추가하세요! </h2>
      </v-card-title>
      <v-card-text style="text-align:center;" >
        <v-container grid-list-md style="display:flex; justify-content:center;">
          <v-layout wrap>
            <v-flex xs12>
              <input style="border: 1px solid rgb(0, 0, 0);" v-model="inputTodo"/>
            </v-flex>
          </v-layout>
        </v-container>
      </v-card-text>
      <v-card-actions style="display:flex; justify-content:center;">
        <v-btn color="blue darken-1" flat @click="createTodo">OK!</v-btn>
        <v-btn color="blue darken-1" flat @click="closeDialog">Cancel</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</v-container>
</v-app>
</template>

<script>
import draggable from 'vuedraggable'

export default {
    name: 'PostTest',
    components:{
      draggable
    },
    data() {
        return {
          myArray1:[],
          myArray2:[],
          myArray3:[],
          inputTodo:"",
          dialog: false,
        }
    },
    mounted(){
      // console.log("?")
      
      this.temp();
      // console.log("?")

    },
    computed:{
      async form () {
        return {
          myArray1:this.myArray1,
          myArray2:this.myArray2,
          myArray3:this.myArray3
        }
      }
    },
	  methods: {
      async temp(){
        var user_num = this.$session.get("userInfo").user_num;
        // this.$http.get(this.$store.state.testIp + "/todolist", {un : user_num}) // 호출
        this.$http.post(this.$store.state.testIp + "/todolist/" +user_num) // 호출
        .then(result=> {
          // console.log(result.data);
          //--
          var todos = result.data;
          console.log(todos);
          
          for(var i = 0; i < todos.length; i++){
            if(todos[i].todo_state == "1"){
              this.myArray1.push(todos[i])
            }
            else if(todos[i].todo_state == "2"){
              this.myArray2.push(todos[i])
            }
            else{
              this.myArray3.push(todos[i])
            }
          }
        })
      },

      async createTodo() {
        var user_num = this.$session.get("userInfo").user_num; // require login ㅍ해야함
        // console.log(this.$session.get("userInfo"))
        var content = this.inputTodo;             
        if (!content ==""){
          this.myArray1.push({          
          todo_content: content,        // 이부분이 maArray1로 들어가고, myArray1이 form으로 back으로 전송됨    
          todo_category: 0,
          todo_user: user_num 
          ,    
          })  
        this.inputTodo = "";
        }
        this.dialog = false;

      },

      async updateTodo() {
        var form = await this.form
        this.$http.put(this.$store.state.testIp + "/todolist/update", form) // 호출
        .then((req) => {
          // console.log(form)
          alert(req.data)
        })
      },
      openDialog(){
          this.dialog = true;
          console.log(this.dialog)
          console.log("true")
      },
      closeDialog(){
        this.dialog = false;
        console.log("false")
      }

      // async person() {
        
      //   var todos = result.data;
          
      //   for(var i = 0; i < todos.length; i++){
      //     if(todos[i].todo_state == "1"){
      //       this.myArray1.push(todos[i])
      //     }
      //     else if(todos[i].todo_state == "2"){
      //       this.myArray2.push(todos[i])
      //     }
      //     else{
      //       this.myArray3.push(todos[i])
      //     }
      //   }
      // }
	},
}
</script>

<style scoped>
.Todo {
  border: 2px solid rgba(94, 87, 87, 0.6);

  margin: 0 15px;
  padding : 2px;
  text-align: center;
}
.Todo > h2{
  font-size: 25pt;
  padding:30px 0;
}
</style>
