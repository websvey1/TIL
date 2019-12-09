var express = require('express');
var router = express.Router();
var db = require("../database");

router.post('/personal', function(req, res, next){
    var user_num = req.body.data.num;
    var data = req.body.body;
    // console.log(data)

    var pool = db.getPool();

    pool.getConnection((ex, conn) => {
        if(ex){
            console.log(ex);
        }else{
            var query = conn.query('insert into calendar(user_num, cal_title, cal_start, cal_end, cal_color, cal_description, cal_category) values(?, ?, ?, ?, ?, ?, 0)', [user_num, data.title, data.start, data.end, data.cssClass, data.description], function (err, result) {
                if (err) {
                  console.error(err);
                  throw err;
                }

                res.send(data);

                conn.release();
            });
        }
    });
});

router.post('/team', function(req, res, next){
    var user_num = req.body.data.num;
    var data = req.body.body;
    // console.log(data)

    var pool = db.getPool();

    pool.getConnection((ex, conn) => {
        if(ex){
            console.log(ex);
        }else{
            var query = conn.query('insert into calendar(user_num, cal_title, cal_start, cal_end, cal_color, cal_description, cal_category, cal_teamNum) values(?, ?, ?, ?, ?, ?, 1, ?)', [user_num, data.title, data.start, data.end, data.cssClass, data.description, data.teamNum], function (err, result) {
                if (err) {
                  console.error(err);
                  throw err;
                }

                res.send(data);

                conn.release();
            });
        }
    });
});

router.post('/getPlan', function(req, res, next){
    var user_num = req.body.num;
    var pool = db.getPool();

    pool.getConnection((ex, conn) => {
        if(ex){
            console.log(ex);
        }else{
            var query = conn.query('select cal_title, cal_start, cal_end, cal_color, cal_description from calendar where user_num = ? and cal_category = 0', user_num, function (err, result) {
                if (err) {
                  console.error(err);
                  throw err;
                }
                // console.log(result)
                res.send(result);

                conn.release();
            });
        }
    });
});

router.post('/getTeamPlan', function(req, res, next){
    var user_num = req.body.num;
    var team_num = req.body.team;
    var pool = db.getPool();

    pool.getConnection((ex, conn) => {
        if(ex){
            console.log(ex);
        }else{
            var query = conn.query('select cal_title, cal_start, cal_end, cal_color, cal_description, cal_teamNum from calendar where cal_teamNum = ? and cal_category = 1', team_num, function (err, result) {
                if (err) {
                  console.error(err);
                  throw err;
                }
                // console.log(result)
                res.send(result);

                conn.release();
            });
        }
    });
});

router.post('/getCalId', function(req, res, next){
    var user_num = req.body.num;
    var title = req.body.title;
    var start = req.body.start;
    var end = req.body.end;
    var description = req.body.description;
    var cssClass = req.body.cssClass;

    var pool = db.getPool();

    pool.getConnection((ex, conn) => {
        if(ex){
            console.log(ex);
        }else{
            var query = conn.query('select * from calendar where user_num = ? and cal_title = ? and cal_start = ? and cal_end = ? and cal_color = ? and cal_description = ?', [user_num, title, start, end, cssClass, description], function (err, result) {
                if (err) {
                  console.error(err);
                  throw err;
                }

                res.send(result);
                conn.release();
            });
        }
    });
});

router.post('/modifyPersonal', function(req, res, next){
    console.log(req.body)
    var id = req.body.id;
    var title = req.body.title;
    var start = req.body.start;
    var end = req.body.end;
    var cssClass = req.body.cssClass;
    var description = req.body.description;

    var pool = db.getPool();

    pool.getConnection((ex, conn) => {
        if(ex){
            console.log(ex);
        }else{
            var query = conn.query('update calendar set cal_title = ?, cal_start = ?, cal_end = ?, cal_color = ?, cal_description = ? where cal_id = ?', [title, start, end, cssClass, description, id], function (err, result) {
                if (err) {
                  console.error(err);
                  throw err;
                }

                res.send(result);

                conn.release();
            });
        }
    });
});

router.post('/delete', function(req, res, next){
    var id = req.body.id;

    var pool = db.getPool();

    pool.getConnection((ex, conn) => {
        if(ex){
            console.log(ex);
        }else{
            var query = conn.query('delete from calendar where cal_id = ?', id, function (err, result) {
                if (err) {
                  console.error(err);
                  throw err;
                }

                res.send(result);

                conn.release();
            });
        }
    });
});

module.exports = router;
