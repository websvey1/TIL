var express = require('express');
var router = express.Router();
var db = require("../database")

router.post('/read/:id', function(req, res, next) {
  var pool = db.getPool();

  var user_num = req.params.id;

  pool.getConnection((ex, conn) => {
    if(ex){
      console.log(ex);
    }
    else{
      var sql = "select u.user_num, u.user_id, u.user_email, u.user_name, u.user_created_at, u.user_updated_at, u.user_image from user as u where user_num = ?;"
      var query = conn.query(sql,[user_num],
      // var query = conn.query('select user_num, user_id, user_email, user_name, user_created_at, user_updated_at from user where user_id = "myeong" and user_password = "12345";',
        function (err, result) {
        if (err) {
          console.error(err);
          conn.release();
          throw err;
        }

        if(result.length == 0){
          res.send("fail")
        }
        else{
          var user = result[0];
          var user_num = result[0].user_num;

          var sql = "select t.tech_num, t.tech_name from favor as f inner join tech as t on f.favor_tech = t.tech_num where f.favor_user = ?";

          var query = conn.query(sql, user_num,
            function (err, result) {
              if(err){
                throw err;
              }

              user["favor"] = result
              console.log(user);
              res.send(user);
            })
        }
      });
    }

    conn.release();
  })
})
router.post('/login', function(req, res, next) {
  var pool = db.getPool();
  var id = req.body.id;
  var password = req.body.password;
  console.log(req.body);

  pool.getConnection((ex, conn) => {
    if(ex){
      console.log(ex);
    }
    else{
      var sql = "select u.user_num, u.user_id, u.user_email, u.user_name, u.user_created_at, u.user_updated_at, u.user_image from user as u where user_id = ? and user_password = ?;"
      var query = conn.query(sql,[id, password],
      // var query = conn.query('select user_num, user_id, user_email, user_name, user_created_at, user_updated_at from user where user_id = "myeong" and user_password = "12345";',
        function (err, result) {
        if (err) {
          console.error(err);
          conn.release();
          throw err;
        }

        if(result.length == 0){
          res.send("fail")
        }
        else{
          var user = result[0];
          var user_num = result[0].user_num;

          var sql = "select t.tech_num, t.tech_name from favor as f inner join tech as t on f.favor_tech = t.tech_num where f.favor_user = ?";

          var query = conn.query(sql, user_num,
            function (err, result) {
              if(err){
                throw err;
              }

              user["favor"] = result
              console.log(user);
              res.send(user);
            })
        }
      });
    }
    conn.release();
  });
});

router.post('/create', function(req, res, next) {
  var pool = db.getPool();
  var id = req.body.id;
  var password = req.body.password;
  var email = req.body.email;
  var name = req.body.name;
  var favor = req.body.favor;
  var image = req.body.image;

  pool.getConnection((ex, conn) => {
    if(ex){
      console.log(ex, 'this is create_log');
    }
    else{
      /////////////////////////////////////////////////////////////////////////////////////////////////
      var query = conn.query('select * from user where user_id = ?', id, function (err, result) {
        if (err) {
          console.error(err);
          conn.release();
          throw err;
        }
        
        if(result == ''){
          var sql = 'insert into user(user_id, user_password, user_email, user_name, user_image) values(?,?,?,?,?)';
          var sql_data = [id, password, email, name, image];
          var query = conn.query(sql,sql_data,function (err, result) {
            if (err) {
              console.error(err);
              conn.release();
              throw err;
            }
            var user_num = result.insertId;
            
            if(favor.length > 0){
              var sql = "insert into favor(favor_user, favor_tech) values"

              for(var i = 0; i < favor.length; i++){
                sql += "("+user_num+"," + favor[i] +")"
                if(i + 1 == favor.length){
                  sql += ";"
                }
                else{
                  sql += ","
                }
              }
              var querry = conn.query(sql,function (err, result) {
              if (err) {
                console.error(err);
                throw err;
              }

              res.send("Success");
              })
            }
          })
        }else{
          res.send("ID");
        }
      })
    }
    conn.release();
  });
});

router.put('/update', function(req, res, next) {
  var pool = db.getPool();
  var user_num = req.body.user_num;
  var user_id = req.body.user_id;
  var before_pw = req.body.before_pw;
  var after_pw = req.body.after_pw;
  var user_email = req.body.user_email;
  var user_name = req.body.user_name;
  var favor = req.body.favor;
  var image = req.body.image;

  console.log(req.body)
  console.log(after_pw)
  pool.getConnection((ex, conn) => {
    if(ex){
      console.log(ex);
    }
    else{
      var sql = "select * from user where user_num = ? and user_password = ?;"
      var query = conn.query(sql,[user_num,before_pw],function (err, result) {
        if (err) {
          console.error(err);
          conn.release();
          throw err;
        }

        if(result.length == 0){
          res.send("fail");
        }
        else{
          var sql = "delete from favor where favor_user = ?;"

          var query = conn.query(sql, user_num, function (err, result) {
            if (err) {
              console.error(err);
              throw err;
            }

            var sql = 'update user set user_password = ?, user_image = ? where user_num = ?;'
            var sql_data = [after_pw, image, user_num];
            var query = conn.query(sql,sql_data,function (err, result) {
              if (err) {
                console.error(err);
                throw err;
              }

              if(favor.length > 0){
                var sql = "insert into favor(favor_user, favor_tech) values"

                for(var i = 0; i < favor.length; i++){
                  sql += "("+user_num+"," + favor[i] +")"
                  if(i + 1 == favor.length){
                    sql += ";"
                  }
                  else{
                    sql += ","
                  }
                }

                var querry = conn.query(sql,function (err, result) {
                  if (err) {
                    console.error(err);
                    throw err;
                  }

                  res.send("success");
                })
              }

              else{
                res.send("success");
              }
            });
          });
        }
      });
    }
    conn.release();
  });
});

router.delete('/delete', function(req, res, next) {
  var pool = db.getPool();
  var id = req.body.id;
  var password = req.body.password;
  var email = req.body.password;
  var name = req.body.name;

  pool.getConnection((ex, conn) => {
    if(ex){
      console.log(ex);
    }
    else{
      var query = conn.query('insert into user(user_id, user_password, user_email, user_name) values("'+id+'","' +password+'","'+email+'","' +name + '")',
        function (err, result) {
        if (err) {
          console.error(err);
          conn.release();
          throw err;
        }

        res.send("Success");
      });
    }
    conn.release();
  });
});

router.get('/tech', function(req, res, next) {
  var pool = db.getPool();

  pool.getConnection((ex, conn) => {
    if(ex){
      console.log(ex);
    }
    else{
      var query = conn.query('select * from tech',
        function (err, result) {
        if (err) {
          console.error(err);
          conn.release();
          throw err;
        }

        res.send(result);
      });
    }
    conn.release();
  });
});
module.exports = router;

//표준
