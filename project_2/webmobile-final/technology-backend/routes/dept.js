var express = require('express');
var router = express.Router();
var db = require("../database")


/*
기본 폼

var sql = ""
var query = conn.query(sql,function (err, result) {
  if (err) {
    console.error(err);
    conn.release();
    throw err;
  }

  res.send("Success");
});

*/
/* GET users listing. */
router.get('/:id', function(req, res, next) {
  var dept_no = req.params.id;

  console.log(req.params);
  console.log("dept no : " + req.body);

  var pool = db.getPool();
  pool.getConnection((ex, conn) => {
    if(ex){
      console.log(ex);
    }
    else{
      var query = conn.query('select dept_name from dept where dept_no = ?',dept_no, function (err, result) {
        if (err) {
          console.error(err);
          throw err;
        }

        // res.json(result);
        res.send(result);

        conn.release();
      });
    }
  });
});

router.post('/create', function(req, res, next) {
  var pool = db.getPool();
  pool.getConnection((ex, conn) => {
    if(ex){
      console.log(ex);
    }
    else{
      var query = conn.query('insert into dept values(4, "https://source.unsplash.com/random/300x300")', function (err, result) {
        if (err) {
          console.error(err);
          throw err;
        }

        // res.json(result);
        res.send(result);

        conn.release();
      });
    }
  });
});

router.post('/', function(req, res, next) {
  console.log(req.params);
  console.log("dept no : " + req.body.dept_no);
  // console.log(req.param("dept_no"));
  var pool = db.getPool();
  pool.getConnection((ex, conn) => {
    if(ex){
      console.log(ex);
    }
    else{
      var query = conn.query('select * from dept where dept_no = 1', function (err, result) {
        if (err) {
          console.error(err);
          throw err;
        }

        // res.json(result);
        res.send(result);

        conn.release();
      });
    }
  });
});
module.exports = router;

//표준
