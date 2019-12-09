var express = require('express');
var router = express.Router();
var db = require("../database");

router.post('/getUsers', function(req, res, next) {
    var pool = db.getPool();

    pool.getConnection((ex, conn) => {
        if (ex){
            console.log(ex);
        }
        else{
            var query = conn.query('select user_num from user', function(err, result){
                if(err) {
                    console.error(err);
                    throw err;
                }
                res.send(result);
            })
        }
        conn.release();
    })
})

router.post('/getSelectUsers', function(req, res, next) {
    var category = req.body.category;
    var text = req.body.text;
    var pool = db.getPool();

    if(category == 0){
        console.log("ID")
        pool.getConnection((ex, conn) => {
            if (ex){
                console.log(ex);
            }
            else{
                var query = conn.query('select user_num from user where user_id like concat("%", ? ,"%")', text, function(err, result){
                    if(err) {
                        console.error(err);
                        throw err;
                    }
                    res.send(result);
                })
            }
            conn.release();
        })
    }else if(category == 1){
        console.log("E-MAIL")
        pool.getConnection((ex, conn) => {
            if (ex){
                console.log(ex);
            }
            else{
                var query = conn.query('select user_num from user where user_email like concat("%", ? ,"%")', text, function(err, result){
                    if(err) {
                        console.error(err);
                        throw err;
                    }
                    res.send(result);
                })
            }
            conn.release();
        })
    }else{
        console.log("관심기술")
    }
})

router.post('/getInfo', function(req, res, next) {
    var userNum = req.body.userNum;
    var pool = db.getPool();
    
    pool.getConnection((ex, conn) => {
        if (ex){
            console.log(ex);
        }
        else {
            var userTech = null;

            var query = conn.query(
            'select t.tech_name from user as u inner join favor as f on f.favor_user = u.user_num inner join tech as t on f.favor_tech = t.tech_num where u.user_num =' + userNum + ';',
            function(err, result) {
                if (err){
                    console.error(err);
                    throw err;
                }

                var info = {
                    userN: '',
                    userId: '',
                    userEmail: '',
                    userTech: [],
                    userProject: '',
                    userPost: ''
                }
                
                if (result == '[]') {
                    info.userTech = null
                }
                else {
                    for (var i=0; i < result.length; i++){
                        info.userTech.push(result[i].tech_name)
                    }

                    var query = conn.query('select project_num from project where project_share = 0 and project_category = 0 and project_user =' + userNum + ';',
                    function(err, result) {
                        if (err){
                            console.error(err);
                            throw err;
                        }
                        info.userProject = result.length
                        
                        var query = conn.query('select p.project_num from user as u inner join blog.member as m on u.user_num = m.member_user inner join team as t on m.member_team = t.team_num inner join project as p on p.project_team = t.team_num where m.member_auth = 1 and p.project_category = 1 and p.project_share = 0 and u.user_num = ?', userNum,
                        function(err, result) {
                            if (err) {
                                console.error(err);
                                throw err;
                            }
                            var teampjt = result.length
                            info.userProject = info.userProject + teampjt

                            var query = conn.query('select p.post_num from post as p inner join project as pjt on p.post_project = pjt.project_num left join team as t on pjt.project_team = t.team_num where pjt.project_share = 0 and p.post_share = 0 and p.post_user = ?',userNum,
                            function(err, result) {
                                if (err){
                                    console.error(err);
                                    throw err;
                                }
    
                                info.userPost = result.length
    
                                var query = conn.query('select user_num, user_id, user_email, user_image from user where user_num = ' + userNum + ';',
                                function(err, result) {
                                    if (err){
                                        console.error(err);
                                        throw err;
                                    }
                                    info.userN = result[0].user_num
                                    info.userId = result[0].user_id
                                    info.userEmail = result[0].user_email
                                    info["user_image"] = result[0].user_image;
                                    
                                    res.send(info)
                                })
                            })
                        })
                    })
                }
            })
        }
        conn.release();
    })
})

router.post('/readuser', function(req, res, next) {
    var userNum = req.body.userNum;
    var pool = db.getPool();

    pool.getConnection((ex, conn) => {
        if (ex){
            console.log(ex);
        }
        else {
            var query = conn.query(
            'select t.tech_name from user as u inner join favor as f on f.favor_user = u.user_num inner join tech as t on f.favor_tech = t.tech_num where u.user_num =' + userNum + ';',
            function(err, result) {
                if (err){
                    console.error(err);
                    throw err;
                }
                var info = {
                    usernum: '',
                    userId: '',
                    userEmail: '',
                    userTech: [],
                    userImage: ''
                }
                if (result == '[]') {
                    info.userTech = null
                }
                else {
                    for (var i=0; i < result.length; i++){
                        info.userTech.push(result[i].tech_name)
                    }

                    var query = conn.query('select user_num, user_id, user_email, user_image from user where user_num = ' + userNum + ';',
                    function(err, result) {
                        if (err){
                            console.error(err);
                            throw err;
                        }
                        info.usernum = result[0].user_num
                        info.userId = result[0].user_id
                        info.userEmail = result[0].user_email
                        info.userImage = result[0].user_image
                        console.log(info.userImage)
                        res.send(info)
                        // console.log(info)
                    })
                }
            })
        }
        conn.release();
    })
})

router.post('/getproject', function(req, res, next) {
    var userNum = req.body.userNum;
    var pool = db.getPool();

    pool.getConnection((ex, conn) => {
        if (ex){
            console.log(ex);
        }
        else {
            var query = conn.query('select project_num, project_title, project_goal, project_status, project_tech from project where project_category = 0 and project_share = 0 and project_user = ?', userNum, 
            function(err, result) {
                if (err){
                    console.error(err)
                    throw err
                }
                // console.log(result)
                res.send(result)
            })
        }
    conn.release()
    })
})

router.post('/teamproject', function(req, res, next) {
    var userNum = req.body.userNum;
    var pool = db.getPool()

    pool.getConnection((ex, conn) => {
        if (ex){
            console.log(ex);
        }
        else {
            var query = conn.query('select t.team_num, t.team_name, p.project_num, p.project_user, p.project_title, p.project_goal, p.project_status, p.project_tech from user as u inner join blog.member as m on u.user_num = m.member_user inner join team as t on m.member_team = t.team_num inner join project as p on p.project_team = t.team_num where m.member_auth = 1 and p.project_category = 1 and p.project_share = 0 and u.user_num = ?', userNum, function(err, result) {
                if (err){
                    console.error(err)
                    throw err
                }
                res.send(result)
            })
        }
        conn.release()
    })
})

router.post('/member', function(req, res, next) {
    var teamNum = req.body.teamNum
    var pool = db.getPool()

    pool.getConnection((ex, conn) => {
        if (ex){
            console.log(ex);
        }
        else {
            var query = conn.query('select t.team_num, t.team_name, u.user_id from blog.member as m inner join team as t on m.member_team = t.team_num inner join user as u on u.user_num = m.member_user where t.team_num = ?', teamNum,
            function(err, result) {
                if (err){
                    console.error(err)
                    throw err
                }
                // console.log(result)
                var member = []
                for (var i=0; i < result.length; i++){
                    member.push(result[i].user_id)
                }
                // console.log(member)
                res.send(member)
            })
        }
    conn.release()
    })
})

router.post('/getpost', function(req, res, next) {
    var userNum = req.body.userNum
    var pool = db.getPool()

    pool.getConnection((ex, conn) => {
        if (ex){
            console.log(ex);
        }
        else {
            var query = conn.query('select p.*, pjt.project_title, t.team_name from post as p inner join project as pjt on p.post_project = pjt.project_num left join team as t on pjt.project_team = t.team_num where pjt.project_share = 0 and p.post_share = 0 and p.post_user = ?', userNum,
            function(err, result) {
                if (err){
                    console.error(err)
                    throw err
                }
                res.send(result)
            })
        }
    conn.release()
    })
})

router.post('/gettag', function(req, res, next) {
    var userNum = req.body.userNum
    var postNum = req.body.postNum
    var pool = db.getPool()

    pool.getConnection((ex, conn) => {
        if (ex){
            console.log(ex);
        }
        else {
            var query = conn.query('select p.post_num, t.tag_name from post as p left join tag as t on t.tag_post = p.post_num where post_share = 0 and post_user = ? and post_num = ?', [userNum, postNum],
            function(err, result) {
                if (err){
                    console.error(err)
                    throw err
                }
                var tag = []

                if (result.length > 0) {
                    for (var i=0; i < result.length; i ++){
                        tag.push(result[i].tag_name)
                    }
                }
                res.send(tag)
            })
        }
    conn.release()
    })
})

router.post('/check', function(req, res, next) {
    var loginId = req.body.loginId
    var user = req.body.user
    var pool = db.getPool()

    pool.getConnection((ex, conn) => {
        if (ex){
            console.log(ex)
        }
        else {
            var query = conn.query('select follow_num from follow where follower_user = ? and following_user = ?',
            [loginId, user], function(err, result) {
                if (err){
                    console.error(err)
                    throw err
                }
                res.send(result)
            })
        }
        conn.release()
    })
})

router.post('/follow', function(req, res, next) {
    var followingUser = req.body.followingUser
    var followerUser = req.body.followerUser
    var pool = db.getPool()
    console.log(followingUser)
    console.log(followerUser)

    pool.getConnection((ex, conn) => {
        if (ex){
            console.log(ex);
        }
        else {
            var query = conn.query('insert into follow(follower_user, following_user) values(?, ?)', [followerUser, followingUser], 
            function(err, result) {
                if (err){
                    console.error(err)
                    throw err
                }
                res.send(result)
            })
        }
        conn.release()
    })
})

router.post('/nofollow', function(req, res, next){
    var followingUser = req.body.followingUser
    var followerUser = req.body.followerUser
    var pool = db.getPool()
    
    pool.getConnection((ex, conn) => {
        if (ex){
            console.log(ex)
        }
        else {
            var query = conn.query('delete from follow where follower_user = ? and following_user = ?', [followerUser, followingUser],
            function(err, result) {
                if (err) {
                    console.error(err)
                    throw err
                }
                res.send("Success")
            })
        }
        conn.release();
    })
})

router.post('/usertech', function(req, res, next) {
    var userNum = req.body.userNum
    var pool = db.getPool()

    pool.getConnection((ex, conn) => {
        if (ex){
            console.log(ex)
        }
        else {
            var query = conn.query(
            'select t.tech_name from user as u inner join favor as f on f.favor_user = u.user_num inner join tech as t on f.favor_tech = t.tech_num where u.user_num =' + userNum + ';',
            function(err, result) {
                if (err){
                    console.error(err);
                    throw err;
                }
                var tech = []

                if (result == '[]') {
                    tech = null
                }
                else {
                    for (var i=0; i < result.length; i++){
                        tech.push(result[i].tech_name)
                    }
                }
                res.send(tech)
            })
        }
        conn.release()
    })
})

router.post('/userfollower', function(req, res, next) {
    var pool = db.getPool()
    var userNum = req.body.userNum

    pool.getConnection((ex, conn) => {
        if (ex){
            console.log(ex)
        }
        else{
            var query = conn.query('select u.* from follow as f inner join user as u on follower_user = u.user_num where following_user = ?', userNum,
            function(err, result) {
                if (err) {
                    console.error(err)
                    throw err
                }
                res.send(result)
            })
        }
        conn.release();
    })
})

router.post('/userfollowing', function(req, res, next) {
    var pool = db.getPool()
    var userNum = req.body.userNum

    pool.getConnection((ex, conn) => {
        if (ex){
            console.log(ex)
        }
        else{
            var query = conn.query('select u.* from follow as f inner join user as u on following_user = u.user_num where follower_user = ?', userNum,
            function(err, result) {
                if (err) {
                    console.error(err)
                    throw err
                }
                res.send(result)
            })
        }
        conn.release();
    })
})

router.post('/message', function(req, res, next) {
    var pool = db.getPool()
    var sender = req.body.message.sender.value
    var receiver = req.body.message.receiver.value
    var title = req.body.message.msg_title
    var content = req.body.message.msg_content

    pool.getConnection((ex, conn) => {
        if (ex){
            console.log(ex)
        }
        else {
            var query = conn.query('insert into message(send_user, receive_user, message_content, message_title, message_read, created_at) values(?, ?, ?, ?, 0, now())', 
            [sender, receiver, content, title], function(err, result) {
                if(err){
                    console.error(err)
                    throw err
                }
                res.send("Success")
            })
        }
        conn.release();
    })
})

router.post('/checkNew', function(req, res, next) {
    var userNum = req.body.id
    var pool = db.getPool()

    pool.getConnection((ex, conn) => {
        if (ex){
            console.log(ex)
        }
        else {
            var query = conn.query('select * from message as m inner join user as u on m.send_user = u.user_num where m.receive_user = ?', userNum,
            function(err, result) {
                if(err){
                    console.error(err)
                    throw err
                }
                res.send(result)
            })
        }
        conn.release()
    })
})

router.post('/checkRead', function(req, res, next) {
    var userNum = req.body.id
    var pool = db.getPool()

    pool.getConnection((ex, conn) => {
        if (ex){
            console.log(ex)
        }
        else {
            var query = conn.query('select count(*) as total from message where receive_user = ? and message_read = 0', userNum, function(err, result) {
                if(err){
                    console.error(err)
                    throw err
                }
                res.send(result)
            })
        }
        conn.release()
    })
})

router.post('/messageread', function(req, res, next) {
    var msgNum = req.body.msg
    var pool = db.getPool()

    pool.getConnection((ex, conn) => {
        if (ex){
            console.log(ex)
        }
        else {
            var query = conn.query('update message set message_read = 1 where message_num = ?', msgNum,
            function(err, result) {
                if(err){
                    console.error(err)
                    throw err
                }
                res.send("Read")
            })
        }
        conn.release()
    })

})

router.post('/messagedelete', function(req, res, next) {
    var msgNum = req.body.msg
    var pool = db.getPool()

    pool.getConnection((ex, conn) => {
        if (ex){
            console.log(ex)
        }
        else {
            var query = conn.query('delete from message where message_num = ?', msgNum,
            function(err, result) {
                if(err){
                    console.error(err)
                    throw err
                }
                res.send("Delete")
            })
        }
        conn.release()
    })
})
module.exports = router;
