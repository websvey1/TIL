var express = require("express");
var router = express.Router();

var User = require("../models/user");
const crypto = require('crypto');

// 모든 user 정보를 불러온다
router.get("/", function(req, res, next) {
    User.find(function(error, users) {
        if (error) {
        console.log(error);
        } else {
        console.log(users);
        res.send(users);
        }
    });
});

// 회원가입
router.post('/create', function(req, res, next) {
    User.findOne({userid: req.body.userid}, function(err, output){
        if (!output) {
            const newUser = new User(req.body)
            let cipher = crypto.createCipher('aes192', 'key')
            cipher.update(newUser.password, 'utf8', 'base64')
            let cipheredOutput = cipher.final('base64')
            newUser.password = cipheredOutput
          
            User.create(newUser)
                .then(result => {
                    res.send(result);
                })
                .catch(err => {
                    res.status(500).send(err);
                });
        } else {
            return res.send(false)
        }
    })
})

// 로그인
router.post('/login', function(req, res, next) {
    const userinfo = req.body
    let cipher = crypto.createCipher('aes192', 'key')
    cipher.update(userinfo.password, 'utf8', 'base64')
    let cipherPw  = cipher.final('base64')
    User.findOne({userid: userinfo.userid, password: cipherPw}, function(err, user){
        
        if(err) {// 구문 error
            return res.status(500).json({error: err})
        };
        
        if(!user) {// User가 없으면 error
            return res.status(404).json({error: 'user not found'})
        }
    
        res.json(user);
    })
})

router.delete('/delete/:userid', function(req, res, next) {
    User.remove(req.params, function(err, output){
        if (err) {
            return res.status(500).json({error: err})
        }
    })
})

module.exports = router;
