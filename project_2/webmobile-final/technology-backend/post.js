var express = require('express');
var router = express.Router();
var db = require("../database")

router.get('/:id', function(req, res, next){
  var pool = db.getPool();

  var post_num = req.params.id;

  console.log(post_num);
  pool.getConnection((ex, conn) => {
    if (ex) {
      console.log(ex);
    } else {
      var query = conn.query('select p.post_num, p.post_title, p.post_content, p.post_share, p.post_created_at, p.post_updated_at,p.post_category, i.image_url, u.user_id, u.user_name from post as p inner join imageconnector as ic on p.post_num = ic.imageconn_post inner join image as i on ic.imageconn_image = i.image_num inner join user as u on p.post_user = u.user_num where imageconn_index = 0 and post_num = '+post_num+ ';',
        function(err, result) {
          if (err) {
            console.error(err);
            conn.release();
            throw err;
          }

          console.log(result);
          var post = {
            post:result[0],
            tags:null
          }

          var query = conn.query('select * from tag where tag_post = ' + post_num +';',
            function(err, result){
              if (err) {
                console.error(err);
                conn.release();
                throw err;
              }

              post.tags = result

              console.log(post);
              res.send(post);
            }
          )
        })
    }
    conn.release();
  })
});

router.get('/', function(req, res, next) {
  var pool = db.getPool();

  pool.getConnection((ex, conn) => {
    if (ex) {
      console.log(ex);
    } else {
      var query = conn.query('select p.post_num, p.post_title, p.post_content, p.post_share, p.post_created_at, p.post_category, i.image_url, u.user_id, u.user_name from post as p inner join imageconnector as ic on p.post_num = ic.imageconn_post inner join image as i on ic.imageconn_image = i.image_num inner join user as u on p.post_user = u.user_num where imageconn_index = 0;',
        function(err, result) {
          if (err) {
            console.error(err);
            conn.release();
            throw err;
          }

          res.send(result);
        })
    }
    conn.release();
  })
});

router.post('/create', function(req, res, next) {
  var pool = db.getPool();

  var user = req.body.user;
  var title = req.body.title;
  var content = req.body.content;
  var share = req.body.share;
  var category = req.body.category;
  var imageUrl = req.body.imageUrl;
  var tags = req.body.tags;




  pool.getConnection((ex, conn) => {
    if (ex) {
      console.log(ex);
    } else {
      var query = conn.query('insert into post(post_user, post_title, post_content, post_share, post_category) values (' + user + ', "' + title + '", "' + content + '", ' + share + ', ' + category + ');',
        (err, result) => {
          if (err) {
            console.error(err);
            throw err;
          }

          var post_num = result.insertId;

          var query = conn.query('insert into image(image_url) values("' + imageUrl + '");', (err, result) => {
            if (err) {
              console.error(err);
              throw err;
            }
            var image_num = result.insertId;

            var query = conn.query('insert into imageconnector(imageconn_image,imageconn_post,imageconn_category,imageconn_index) values(' + image_num + ',' + post_num + ',0, 0)', (err, result) => {
              if (err) {
                console.error(err);
                throw err;
              }

              if (tags.length > 0) {
                var tag_query = 'insert into tag(tag_post, tag_name) values';
                for (var i = 0; i < tags.length; i++) {
                  tag_query += '(' + post_num + ', "' + tags[i] + '")'
                  if (i + 1 == tags.length) {
                    tag_query += ';'
                  } else {
                    tag_query += ','
                  }
                }


                var query = conn.query(tag_query, (err, result) => {
                  if (err) {
                    console.error(err);
                    throw err;
                  }

                  res.send("Success");
                })
              } else {
                res.send("Success");
              }
            })
          })
        });
    }
    conn.release();

  })
})



module.exports = router;
