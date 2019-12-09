var express = require('express');
var router = express.Router();
var db = require("../database");

router.post('/getUser', function(req, res, next){
    var pool = db.getPool();

    pool.getConnection((ex, conn) => {
        if(ex){
            console.log(ex);
        }else{
            var query = conn.query('select user_name, user_id from user', function (err, result) {
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

router.post('/makeTeam', function(req, res, next){
    var name = req.body.name;
    var pool = db.getPool();

    pool.getConnection((ex, conn) => {
        if(ex){
            console.log(ex);
        }else{
            var query = conn.query('insert into team(team_name, team_created_at, team_updated_at) values(?, now(), now())', name, function (err, result) {
                if (err) {
                  console.error(err);
                  throw err;
                }
                var num = result.insertId;
                res.send(num + "");
            });
            conn.release();
        }
    });
});

router.post('/makeMember', function(req, res, next){
    var teamNum = req.body.teamNum;
    var members = req.body.member;
    var pool = db.getPool();
    console.log("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    console.log(members)

    pool.getConnection((ex, conn) => {
        if(ex){
            console.log(ex);
        }else{
            for(var i = 0; i < members.length; i++){
                // 1st. user table로 가서, 지금 가져온 members에 있는 이름의 user의 user_num을 가져옴
                // 2nd. 이 user_num과 teamNum을 이용하여 member table에 집어넣음
                var query = conn.query('select user_num from user where user_name = ?', members[i], function (err, result) {
                    if (err) {
                      console.error(err);
                      throw err;
                    }

                    var query = conn.query('insert into blog.member(member_user, member_team, member_auth) values(?, ?, 0)', [result[0].user_num, teamNum], function (err, result) {
                        if (err) {
                          console.error(err);
                          throw err;
                        }
                    });
                });
            }
            res.send("success")
            conn.release();
        }
    });
});

router.post('/getTeamList', function(req, res, next){
    var userNum = req.body.num;
    var pool = db.getPool();

    pool.getConnection((ex, conn) => {
        if(ex){
            console.log(ex);
        }else{
            var query = conn.query('select * from user as u inner join blog.member as m on u.user_num = m.member_user inner join team as t on m.member_team = t.team_num where u.user_num = ?', userNum, function(err, result){
                if(err){
                    console.log(err)
                    throw err
                }
                // console.log(result);
                res.send(result);
            })
            conn.release();
        }
    });
});

router.post('/isMember',function(req, res, next){
    var user_num = req.body.user_num;
    var team_num = req.body.team_num;
    var pool = db.getPool();

    pool.getConnection((ex, conn) => {
        if(ex){
            console.log(ex);
        }else{
          var sql = 'select count(*) from blog.member where member_user = ? and member_team = ?'
          var sql_data = [user_num, team_num];
            var query = conn.query(sql, sql_data, function(err, result){
                if(err){
                    console.log(err)
                    throw err
                }
                // console.log(result)
                var r = result[0]["count(*)"];

                if(r == '0'){
                  res.send('f');
                }
                else{
                  res.send('s');
                }
            })
            conn.release();
        }
    });
});

router.post('/getMember', function(req, res, next){
    var teamNum = req.body.teamNum;
    var pool = db.getPool();
    console.log(teamNum);

    pool.getConnection((ex, conn) => {
        if(ex){
            console.log(ex);
        }else{
            var query = conn.query('select * from team as t inner join blog.member as m on t.team_num = m.member_team inner join user as u on m.member_user = u.user_num where t.team_num = ?', teamNum, function(err, result){
                if(err){
                    console.log(err)
                    throw err
                }
                // console.log(result)
                res.send(result);
            })
            conn.release();
        }
    });
});

router.post('/getAuth', function(req, res, next){
    var num = req.body.num;
    var teamNum = req.body.teamNum;
    var pool = db.getPool();

    pool.getConnection((ex, conn) => {
        if(ex){
            console.log(ex);
        }else{
            var query = conn.query('select member_auth from blog.member where member_user = ? and member_team = ?', [num, teamNum], function(err, result){
                if(err){
                    console.log(err)
                    throw err
                }
                res.send(result);
            })
            conn.release();
        }
    });
});

router.post('/getTeamNum', function(req, res, next){
    var num = req.body.num;
    var teamName = req.body.teamName;
    var pool = db.getPool();

    pool.getConnection((ex, conn) => {
        if(ex){
            console.log(ex);
        }else{
            var query = conn.query('select team_num from team as t inner join blog.member as m on t.team_num = m.member_team where t.team_name = ? and m.member_user = ?', [teamName, num], function(err, result){
                if(err){
                    console.log(err)
                    throw err
                }
                res.send(result);
            })
            conn.release();
        }
    });
});

router.post('/changeAuth', function(req, res, next){
    var num = req.body.num;
    var teamNum = req.body.teamNum;
    var pool = db.getPool();

    pool.getConnection((ex, conn) => {
        if(ex){
            console.log(ex);
        }else{
            var query = conn.query('update blog.member set member_auth = 1 where member_user = ? and member_team = ?', [num, teamNum], function(err, result){
                if(err){
                    console.log(err)
                    throw err
                }
                res.send(result);
            })
            conn.release();
        }
    });
});

router.post('/deleteTeam', function(req, res, next){
    var num = req.body.num;
    var teamNum = req.body.teamNum;
    var pool = db.getPool();

    pool.getConnection((ex, conn) => {
        if(ex){
            console.log(ex);
        }else{
            var query = conn.query('delete from blog.member where member_user = ? and member_team = ?', [num, teamNum], function(err, result){
                if(err){
                    console.log(err)
                    throw err
                }
                res.send(result);
            })
            conn.release();
        }
    });
});

router.post('/getLatestTeam', function(req, res, next){
    var teamNum = req.body.teamNum;
    // console.log(teamNum)
    // console.log(req.body)
    var pool = db.getPool();

    pool.getConnection((ex, conn) => {
        if(ex){
            console.log(ex);
        }else{
            var query = conn.query('select team_name from team where team_num = ?', teamNum, function(err, result){
                if(err){
                    console.log(err)
                    throw err
                }

                res.send(result);
            })
            conn.release();
        }
    });
});

router.post('/checkNew', function(req, res, next){
    var id = req.body.id;
    var pool = db.getPool();

    pool.getConnection((ex, conn) => {
        if(ex){
            console.log(ex);
        }else{
            var query = conn.query('select count(member_auth) as total from blog.member where member_user = ? and member_auth = 0', id, function(err, result){
                if(err){
                    console.log(err)
                    throw err
                }

                res.send(result);
            })
            conn.release();
        }
    });
});

module.exports = router;
