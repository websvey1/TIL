var express = require('express');
var router = express.Router();
var db = require("../database");

router.get('/', function(req, res, next){
   var pjtNum = req.body.pjtNum 
   console.log(pjtNum,'todolist');
  //  console.log(this.$store.state.pn)
    var pool = db.getPool();
    // var user_num = req.body.un
    // console.log(user_num);
    pool.getConnection((ex, conn) => {
        if (ex){
            console.log(ex);

        }
        else {
            var movies = conn.query('SELECT * FROM todolist', function (err, result) {
                if (err) {
                    console.log(err);
                    throw err;
                }
                res.send(result);
            });
        }
        conn.release()
    });
})
router.post('/:id', function(req, res, next){
    var pool = db.getPool();
    var back_pn = req.body.back_pn;
    var prime_key = req.params.id;
    console.log(back_pn, 'back_pn');
    // console.log(req.body);
    
    
    pool.getConnection((ex, conn) => {
        if (ex) {
            console.log(ex);
        }
        else{
            var query = conn.query('select * from todolist where todo_project=?;', back_pn,
                function(err, result) {
                    if (err) {
                        console.error(err);
                        conn.release();
                        throw err;
                    }
                    console.log('TTTT')
                    res.send(result);
                    conn.release();
                })
            }
            
        })
    })

router.put('/update', function(req, res, next){
    var pool = db.getPool();
    var prime_key = req.params.todo_num;
    // console.log(prime_key); // prime key가 안넘어옴
    var big = req.body;
    var myArray1 = req.body.myArray1;
    var myArray2 = req.body.myArray2;
    var myArray3 = req.body.myArray3;
    var back_pn = req.body.back_pn;
    var state_1 = 1;
    var state_2 = 2;
    var state_3 = 3;
    console.log(req.body)

    pool.getConnection((ex, conn) => {
        if(ex){
            console.log(ex);
        }
        else{

            // var query = conn.query('select * from todos');
            var query = conn.query('delete from todolist where todo_project='+ back_pn +';'); //수정해야함, 아이디 12만 지우도록 되어잇음
            var add_query = 'insert into todolist(todo_content, todo_state, todo_category, todo_project) values';
            
            for(var i = 0; i < myArray1.length; i++){ // 리스트의 길이만큼 for문
              add_query += '("' + myArray1[i].todo_content + '",' + state_1 +',' + myArray1[i].todo_category +',' + back_pn +')'
                                                        // 기본 쿼리문
                                                        console.log(add_query)
              if(i + 1 == myArray1.length){
                if(myArray2.length == 0 && myArray3 == 0){
                  add_query += ";"
                }
                else{
                  add_query += ","
                }
              }
              else{
                add_query += ","
              }
            }

            for(var i = 0; i < myArray2.length; i++){
              add_query += '("' + myArray2[i].todo_content + '",' + state_2 +',' + myArray2[i].todo_category+',' + back_pn +')'

              if(i + 1 == myArray2.length){
                if(myArray3 == 0){
                  add_query += ";"
                }
                else{
                  add_query += ","
                }
              }
              else{
                add_query += ","
              }
            }

            for(var i = 0; i < myArray3.length; i++){
              add_query += '("' + myArray3[i].todo_content + '",' + state_3 +',' + myArray3[i].todo_category +',' + back_pn+')'

              if(i + 1 == myArray3.length){
                add_query += ";"
              }
              else{
                add_query += ","
              }
            }
            console.log(add_query);
            

            var query = conn.query(add_query, (err, result) => {
                if (err) {
                    throw err;
                }
                res.send("success");
            })
        }
        conn.release();
    })
})

router.post('/delete', function(req, res, next){
  console.log(req.body);  
  var pool = db.getPool();
  // var back_pn = req.body.back_pn;
  var back_pn = req.params.id;
  console.log(back_pn, 'back_pn');  
  
  pool.getConnection((ex, conn) => {
      if (ex) {
          console.log(ex);
      }
      else{
          var query = conn.query('delete from todolist where todo_project=?;', back_pn, 
              function(err, result) {
                  if (err) {
                      console.error(err);
                      conn.release();
                      throw err;
                  }
                  console.log(query)
                  res.send(result);
                  conn.release();
              })
          }
          
      })
  })
module.exports = router;
