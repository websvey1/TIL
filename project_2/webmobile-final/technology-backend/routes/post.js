var express = require('express');
var router = express.Router();
var db = require("../database")
var limit = 5;

router.get('/', function(req, res, next) {
  var pool = db.getPool();

  pool.getConnection((ex, conn) => {
    if (ex) {
      console.log(ex);
    } else {
      // var query = conn.query('select p.post_num, p.post_title, p.post_content, p.post_share, p.post_created_at, p.post_category, i.image_url, u.user_id, u.user_name from post as p left join imageconnector as ic on p.post_num = ic.imageconn_post left join image as i on ic.imageconn_image = i.image_num left join user as u on p.post_user = u.user_num where imageconn_index = 0 order by p.post_num desc;',
      var query = conn.query('select p.post_num, p.post_title, p.post_content, p.post_share, p.post_created_at, p.post_category, pjt.project_title, i.image_url, u.user_id, u.user_name, u.user_image from post as p left join imageconnector as ic on p.post_num = ic.imageconn_post left join image as i on ic.imageconn_image = i.image_num left join user as u on p.post_user = u.user_num left join project as pjt on p.post_project = pjt.project_num where pjt.project_share = 0 order by p.post_num desc;',
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

////////////////////////// CRUD //////////////////////////////////////
router.post('/create', function(req, res, next) {
  var pool = db.getPool();
  // PostWritePage.vue의 compited에서 선언한 form의 변수를 불러옴

  var user = req.body.user;
  var title = req.body.title;
  var content = req.body.content;
  var share = req.body.share;
  var category = req.body.category;
  var imageUrl = req.body.imageUrl;
  var created_at = req.body.created_at;
  var tags = req.body.tags;
  var project = req.body.project;

  console.log(req.body);


  pool.getConnection((ex, conn) => {
    if (ex) {
      console.log(ex);
    } else {
      var sql = 'insert into post(post_user, post_title, post_content, post_share, post_created_at, post_updated_at, post_category, post_project) values (?,?,?,?,?,?,?,?);'
      var sql_data = [user, title, content, share, created_at, created_at, category, project];
      var query = conn.query(sql, sql_data, (err, result) => {
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
router.get('/readById/:id', function(req, res, next) {
  var pool = db.getPool();

  var post_num = req.params.id;

  pool.getConnection((ex, conn) => {
    if (ex) {
      console.log(ex);
    } else {
      var query = conn.query('select p.post_num,p.post_user, p.post_title, p.post_content, p.post_share, p.post_created_at, p.post_updated_at,p.post_category, p.post_project, project_title, ic.imageconn_num, i.image_num,i.image_url, u.user_num,u.user_id, u.user_name from post as p left join imageconnector as ic on p.post_num = ic.imageconn_post left join image as i on ic.imageconn_image = i.image_num left join user as u on p.post_user = u.user_num left join project on project_num = p.post_project where post_num = ' + post_num + ';',
        // var query = conn.query('select * from post as p left join imageconnector as ic on p.post_num = ic.imageconn_post left join image as i on ic.imageconn_image = i.image_num left join user as u on p.post_user = u.user_num where imageconn_index = 0 and post_num = '+post_num+ ';',
        function(err, result) {
          if (err) {
            console.error(err);
            conn.release();
            throw err;
          }

          var post = {
            post: result[0],
            tags: null
          }

          // console.log(result[0]);
          var query = conn.query('select * from tag where tag_post = ' + post_num + ';',
            function(err, result) {
              if (err) {
                console.error(err);
                throw err;
              }

              post.tags = result

              // console.log(post);
              res.send(post);
            }
          )
        })
    }
    conn.release();
  })
});
router.put('/updateById/:id', function(req, res, next) {
  var pool = db.getPool();

  var post_num = req.params.id;

  var title = req.body.title;
  var content = req.body.content;
  var share = req.body.share;
  var category = req.body.category;
  var updated_at = req.body.updated_at;
  var tags = req.body.tags;
  var project = req.body.project;

  var image_num = req.body.image_num;

  pool.getConnection((ex, conn) => {
    if (ex) {
      console.log(ex);
    } else {
        var sql = 'update post set post_title = ?, post_content = ?, post_updated_at= ?, post_share = ?, post_category = ?, post_project = ? where post_num = ?;'
        var sql_data = [title, content, updated_at, share, category, project, post_num];
        var query = conn.query(sql, sql_data, function(err, result) {
          if (err) {
            throw err;
          }

          var sql = 'delete from tag where tag_post = "' + post_num + '";'
          var query = conn.query(sql, function(err, result) {
            if (err) {
              throw err;
            }

            var imageUrl = req.body.imageUrl;

            var sql = 'update image set image_url = "' + imageUrl + '"  where image_num = ' + image_num + ';'
            var query = conn.query(sql, function(err, result) {
              if (err) {
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
                    throw err;
                  }

                  res.send("Success");
                })
              } else {
                res.send("Success");
              }
            })
          })
        })
    }
    conn.release();
  })
});
router.delete('/deleteById/:id', function(req, res, next) {
  var pool = db.getPool();

  var post_num = req.params.id;

  pool.getConnection((ex, conn) => {
    if (ex) {
      console.log(ex);
    } else {
      var sql = 'delete from post where post_num = "' + post_num + '";'
      var query = conn.query(sql, function(err, result) {
        if (err) {
          console.error(err);
          conn.release();
          throw err;
        }

        var sql = 'select imageconn_image from imageconnector where imageconn_post = ' + post_num + ';'
        var query = conn.query(sql, function(err, result) {
          if (err) {
            console.error(err);
            throw err;
          }

          var image_nums = result;

          var sql = 'delete from image where ';
          for (var i = 0; i < image_nums.length; i++) {
            sql += 'image_num = ' + image_nums[i].imageconn_image;
            if (i + 1 == image_nums.length) {
              sql += ';';
            } else {
              sql += ' or ';
            }
          }
          var query = conn.query(sql, function(err, result) {
            if (err) {
              console.error(err);
              throw err;
            }

            res.send("Success");
          })
        })
      })
    }
    conn.release();
  })
});
//////////////////////////////////////////////////////////////////////

router.get('/list/:id', function(req, res, next) {
  var pool = db.getPool();

  var user_num = req.params.id;
  // var post_category = req.body.post_category;
  pool.getConnection((ex, conn) => {
    if (ex) {
      console.log(ex);
    } else {
      // var sql = 'select p.post_num, p.post_title, p.post_content, p.post_share, p.post_created_at, p.post_category, i.image_url, u.user_id, u.user_name from post as p left join imageconnector as ic on p.post_num = ic.imageconn_post left join image as i on ic.imageconn_image = i.image_num left join user as u on p.post_user = u.user_num where imageconn_index = 0 and p.post_user = ?  order by p.post_num desc;'
      var sql = 'select p.post_num, p.post_title, p.post_content, p.post_share, p.post_created_at, p.post_category, i.image_url, u.user_id, u.user_name from post as p left join imageconnector as ic on p.post_num = ic.imageconn_post left join image as i on ic.imageconn_image = i.image_num left join user as u on p.post_user = u.user_num where p.post_user = ?  order by p.post_num desc;'
      var query = conn.query(sql, user_num, function(err, result) {
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

router.post('/teamAllList/:page', function(req, res, next){
  var pjtNum = req.body.pjtNum;
  var start = req.params.page * limit;
  var pool = db.getPool();

  pool.getConnection((ex, conn) => {
    if (ex) {
      console.log(ex);
    } else {
      // var sql = 'select p.post_num, p.post_title, p.post_content, p.post_share, p.post_created_at, p.post_category, i.image_url, u.user_id, u.user_name from post as p left join imageconnector as ic on p.post_num = ic.imageconn_post left join image as i on ic.imageconn_image = i.image_num left join user as u on p.post_user = u.user_num where imageconn_index = 0 and p.post_user = ? and p.post_category = ? order by p.post_num desc;'
      var sql = 'select p.post_num, p.post_project, p.post_title, p.post_content, p.post_share, p.post_created_at, p.post_category, pjt.project_title, i.image_url, u.user_id, u.user_name from post as p left join imageconnector as ic on p.post_num = ic.imageconn_post left join image as i on ic.imageconn_image = i.image_num left join user as u on p.post_user = u.user_num left join project as pjt on p.post_project = pjt.project_num where p.post_project = ? order by p.post_num desc limit ?, ?;'
      var query = conn.query(sql, [pjtNum, start, limit], function(err, result) {
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
})

router.post('/alllist/:page', function(req, res, next) {
  var pool = db.getPool();

  var post_category = req.body.post_category;
  console.log(req.body,'req body')
  var start = req.params.page * limit;
  if (post_category == '2') {
    pool.getConnection((ex, conn) => {
      if (ex) {
        console.log(ex);
      } else {
        // var sql = 'select p.post_num, p.post_title, p.post_content, p.post_share, p.post_created_at, p.post_category, i.image_url, u.user_id, u.user_name from post as p left join imageconnector as ic on p.post_num = ic.imageconn_post left join image as i on ic.imageconn_image = i.image_num left join user as u on p.post_user = u.user_num where imageconn_index = 0 and p.post_user = ? and p.post_category = ? order by p.post_num desc;'
        var sql = 'select p.post_num, p.post_title, p.post_content, p.post_share, p.post_created_at, p.post_category, pjt.project_title, i.image_url, u.user_id, u.user_name, u.user_image from post as p left join imageconnector as ic on p.post_num = ic.imageconn_post left join image as i on ic.imageconn_image = i.image_num left join user as u on p.post_user = u.user_num left join project as pjt on p.post_project = pjt.project_num where pjt.project_share = 0 order by p.post_num desc limit ?, ?;'
        var query = conn.query(sql, [start, limit], function(err, result) {
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
  } else if (post_category == '0' || post_category == '1') {
    pool.getConnection((ex, conn) => {
      if (ex) {
        console.log(ex);
      } else {
        // var sql = 'select p.post_num, p.post_title, p.post_content, p.post_share, p.post_created_at, p.post_category, i.image_url, u.user_id, u.user_name from post as p left join imageconnector as ic on p.post_num = ic.imageconn_post left join image as i on ic.imageconn_image = i.image_num left join user as u on p.post_user = u.user_num where imageconn_index = 0 and p.post_user = ? and p.post_category = ? order by p.post_num desc;'
        var sql = 'select p.post_num, p.post_title, p.post_content, p.post_share, p.post_created_at, p.post_category, pjt.project_title, i.image_url, u.user_id, u.user_name, u.user_image from post as p left join imageconnector as ic on p.post_num = ic.imageconn_post left join image as i on ic.imageconn_image = i.image_num left join user as u on p.post_user = u.user_num left join project as pjt on p.post_project = pjt.project_num where p.post_category = ? and pjt.project_share = 0  order by p.post_num desc limit ?, ?;'
        var sql_data = [post_category, start, limit]
        var query = conn.query(sql, sql_data, function(err, result) {
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
  }
});

router.post('/totalPageNum', function(req, res, next) {
  var pool = db.getPool();

  var post_category = req.body.post_category;
  if (post_category == '0') {
    pool.getConnection((ex, conn) => {
      if (ex) {
        console.log(ex);
        conn.release();
      } else {
        var sql = 'select count(post_num) from post left join project on post_project = project_num where post_category = 0 and project_share = 0;'
        var query = conn.query(sql, function(err, result) {
          if (err) {
            console.error(err);
            throw err;
          }
          var page = result[0]["count(post_num)"];
          if (page % limit == 0) {
            res.send(parseInt(page / limit) + "");
          } else {
            res.send(parseInt(page / limit + 1) + "");
          }
        })
      }
      conn.release();
    })
  } else if (post_category == '1') {
    pool.getConnection((ex, conn) => {
      if (ex) {
        console.log(ex);
        conn.release();
      } else {
        var sql = 'select count(post_num) from post left join project on post_project = project_num where post_category = 1 and project_share = 0;'
        var query = conn.query(sql, function(err, result) {
          if (err) {
            console.error(err);
            throw err;
          }
          var page = result[0]["count(post_num)"];
          if (page % limit == 0) {
            res.send(parseInt(page / limit) + "");
          } else {
            res.send(parseInt(page / limit + 1) + "");
          }
        })
      }
      conn.release();
    })
  } else if (post_category == '2') {
    pool.getConnection((ex, conn) => {
      if (ex) {
        console.log(ex);
        conn.release();
      } else {
        var sql = 'select count(post_num) from post left join project on post_project = project_num where project_share = 0'
        var query = conn.query(sql, function(err, result) {
          if (err) {
            console.error(err);
            throw err;
          }
          var page = result[0]["count(post_num)"];
          if (page % limit == 0) {
            res.send(parseInt(page / limit) + "");
          } else {
            res.send(parseInt(page / limit + 1) + "");
          }
        })
      }
      conn.release();
    })
  }
});

router.post('/teamPageNum', function(req, res, next){
  var pool = db.getPool();

  var pjtNum = req.body.pjtNum;

  pool.getConnection((ex, conn) => {
    if (ex) {
      console.log(ex);
      conn.release();
    } else {
      var sql = 'select count(post_num) from post where post_project = ?;'
      var query = conn.query(sql, pjtNum, function(err, result) {
        if (err) {
          console.error(err);
          throw err;
        }
        var page = result[0]["count(post_num)"];
        if (page % limit == 0) {
          res.send(parseInt(page / limit) + "");
        } else {
          res.send(parseInt(page / limit + 1) + "");
        }
      })
    }
    conn.release();
  })
})

router.post('/search/:page', function(req, res, next) {
  var pool = db.getPool();

  var post_category = req.body.post_category;
  var search_content = req.body.search_content;

  var start = req.params.page * limit;

  console.log(req.body);

  if(post_category == '0' || post_category == '1'){
    // 제목
    if (search_content.category =='0') {
      console.log("0");
      pool.getConnection((ex, conn) => {
        if (ex) {
          console.log(ex);
        } else {
          var sql = 'select p.post_num, p.post_title, p.post_content, p.post_share, p.post_created_at, p.post_category, i.image_url, u.user_id, u.user_name, u.user_image from (select * from post where post_title like concat ("%",?,"%")) as p left join imageconnector as ic on p.post_num = ic.imageconn_post left join image as i on ic.imageconn_image = i.image_num left join user as u on p.post_user = u.user_num left join project as pjt on p.post_project = pjt.project_num where p.post_category = ? and pjt.project_share = 0 order by p.post_num desc limit ?, ?;'
          var query = conn.query(sql, [search_content.text, post_category, start, limit], function(err, result) {
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
    }

    // 내용
    if (search_content.category=='1') {
      console.log("1");
      pool.getConnection((ex, conn) => {
        if (ex) {
          console.log(ex);
        } else {
          var sql = 'select p.post_num, p.post_title, p.post_content, p.post_share, p.post_created_at, p.post_category, i.image_url, u.user_id, u.user_name, u.user_image from (select * from post where post_content like concat ("%",?,"%")) as p left join imageconnector as ic on p.post_num = ic.imageconn_post left join image as i on ic.imageconn_image = i.image_num left join user as u on p.post_user = u.user_num  left join project as pjt on p.post_project = pjt.project_num where p.post_category = ? and pjt.project_share = 0 order by p.post_num desc limit ?, ?;'
          var query = conn.query(sql, [search_content.text, post_category, start, limit], function(err, result) {
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
    }

    // 제목 + 내용
    if (search_content.category=='2') {
      console.log("2");
      pool.getConnection((ex, conn) => {
        if (ex) {
          console.log(ex);
        } else {
          var sql = 'select p.post_num, p.post_title, p.post_content, p.post_share, p.post_created_at, p.post_category, i.image_url, u.user_id, u.user_name, u.user_image from (select * from post where post_title like concat ("%",?,"%") or post_title like concat ("%",?,"%")) as p left join imageconnector as ic on p.post_num = ic.imageconn_post left join image as i on ic.imageconn_image = i.image_num left join user as u on p.post_user = u.user_num  left join project as pjt on p.post_project = pjt.project_num  where  and pjt.project_share = 0 p.post_category = ? order by p.post_num desc limit ?, ?;'
          var query = conn.query(sql, [search_content.text, search_content.text, post_category, start, limit], function(err, result) {
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
    }

    // ID
    if  (search_content.category=='3') {
      console.log("3");
      pool.getConnection((ex, conn) => {
        if (ex) {
          console.log(ex);
        } else {
          console.log("뭐지 씨발????????????");
          var sql = 'select p.post_num, p.post_title, p.post_content, p.post_share, p.post_created_at, p.post_category, i.image_url, u.user_id, u.user_name, u.user_image from post as p left join imageconnector as ic on p.post_num = ic.imageconn_post left join image as i on ic.imageconn_image = i.image_num inner join (select * from user where user_id like concat ("%",?,"%")) as u on p.post_user = u.user_num  left join project as pjt on p.post_project = pjt.project_num where p.post_category = ?  and pjt.project_share = 0 order by p.post_num desc limit ?, ?;'
          var query = conn.query(sql, [search_content.text, post_category, start, limit], function(err, result) {
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
    }

    // TAG
    if (search_content.category == '4') {
      pool.getConnection((ex, conn) => {
        if (ex) {
          console.log(ex);
        } else {
          var sql = 'select p.post_num, p.post_title, p.post_content, p.post_share, p.post_created_at, p.post_category, i.image_url, u.user_id, u.user_name, u.user_image from (select * from post where post_category = ?) as p left join imageconnector as ic on p.post_num = ic.imageconn_post left join image as i on ic.imageconn_image = i.image_num left join user as u on p.post_user = u.user_num inner join (select * from tag where tag_name like concat("%",?,"%")) as t on p.post_num = t.tag_post order left join project as pjt on p.post_project = pjt.project_num where pjt.project_share = 0 order by p.post_num desc limit ?, ?;'
          var sql_data = [post_category, search_content.text, start, limit];
          var query = conn.query(sql, sql_data, function(err, result) {
            if (err) {
              console.error(err);
              throw err;
            }
            var page = result[0]["count(post_num)"];
            if (page % limit == 0) {
              res.send(parseInt(page / limit) + "");
            } else {
              res.send(parseInt(page / limit + 1) + "");
            }
          })
        }
        conn.release();
      })
    }
  }
  else if(post_category =='2'){
    // 제목
    console.log("==============================");
    console.log("search page category 2");
    console.log(req.body);
    console.log("==============================");

    if (search_content.category =='0') {
      pool.getConnection((ex, conn) => {
        if (ex) {
          console.log(ex);
        } else {
          console.log(limit);
          var sql = 'select p.post_num, p.post_title, p.post_content, p.post_share, p.post_created_at, p.post_category, i.image_url, u.user_id, u.user_name, u.user_image from (select * from post where post_title like concat ("%",?,"%")) as p left join imageconnector as ic on p.post_num = ic.imageconn_post left join image as i on ic.imageconn_image = i.image_num left join user as u on p.post_user = u.user_num  left join project as pjt on p.post_project = pjt.project_num where pjt.project_share = 0 order by p.post_num desc limit ?, ?;'
          var query = conn.query(sql, [search_content.text, start, limit], function(err, result) {
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
    }

    // 내용
    if (search_content.category=='1') {
      console.log("1");
      pool.getConnection((ex, conn) => {
        if (ex) {
          console.log(ex);
        } else {
          var sql = 'select p.post_num, p.post_title, p.post_content, p.post_share, p.post_created_at, p.post_category, i.image_url, u.user_id, u.user_name, u.user_image from (select * from post where post_content like concat ("%",?,"%")) as p left join imageconnector as ic on p.post_num = ic.imageconn_post left join image as i on ic.imageconn_image = i.image_num left join user as u on p.post_user = u.user_num  left join project as pjt on p.post_project = pjt.project_num where pjt.project_share = 0 order by p.post_num desc limit ?, ?;'
          var query = conn.query(sql, [search_content.text, start, limit], function(err, result) {
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
    }

    // 제목 + 내용
    if (search_content.category=='2') {
      console.log("2");
      pool.getConnection((ex, conn) => {
        if (ex) {
          console.log(ex);
        } else {
          var sql = 'select p.post_num, p.post_title, p.post_content, p.post_share, p.post_created_at, p.post_category, i.image_url, u.user_id, u.user_name, u.user_image from (select * from post where post_title like concat ("%",?,"%") or post_title like concat ("%",?,"%")) as p left join imageconnector as ic on p.post_num = ic.imageconn_post left join image as i on ic.imageconn_image = i.image_num left join user as u on p.post_user = u.user_num  left join project as pjt on p.post_project = pjt.project_num where pjt.project_share = 0 order by p.post_num desc limit ?, ?;'
          var query = conn.query(sql, [search_content.text, search_content.text, start, limit], function(err, result) {
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
    }

    // ID
    if  (search_content.category=='3') {
      pool.getConnection((ex, conn) => {
        if (ex) {
          console.log(ex);
        } else {
          var sql = 'select p.post_num, p.post_title, p.post_content, p.post_share, p.post_created_at, p.post_category, i.image_url, u.user_id, u.user_name, u.user_image from post as p left join imageconnector as ic on p.post_num = ic.imageconn_post left join image as i on ic.imageconn_image = i.image_num inner join (select * from user where user_name like concat ("%",?,"%")) as u on p.post_user = u.user_num  left join project as pjt on p.post_project = pjt.project_num where pjt.project_share = 0 order by p.post_num desc limit ?, ?;'
          var query = conn.query(sql, [search_content.text, start, limit], function(err, result) {
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
    }

    // TAG
    if (search_content.category == '4') {
      pool.getConnection((ex, conn) => {
        if (ex) {
          console.log(ex);
        } else {
          var sql = 'select p.post_num, p.post_title, p.post_content, p.post_share, p.post_created_at, p.post_category, i.image_url, u.user_id, u.user_name, u.user_image from post as p left join imageconnector as ic on p.post_num = ic.imageconn_post left join image as i on ic.imageconn_image = i.image_num left join user as u on p.post_user = u.user_num inner join (select * from tag where tag_name like concat("%",?,"%")) as t on p.post_num = t.tag_post  left join project as pjt on p.post_project = pjt.project_num where pjt.project_share = 0 order by p.post_num desc limit ?, ?;'
          var sql_data = [search_content.text, start, limit];
          var query = conn.query(sql, sql_data, function(err, result) {
            if (err) {
              console.error(err);
              throw err;
            }
            var page = result[0]["count(post_num)"];
            if (page % limit == 0) {
              res.send(parseInt(page / limit) + "");
            } else {
              res.send(parseInt(page / limit + 1) + "");
            }
          })
        }
        conn.release();
      })
    }
  }

});
router.post('/totalPageNumForSearch', function(req, res, next) {
  var pool = db.getPool();

  var post_category = req.body.post_category;
  var search_content = req.body.search_content;

  if (post_category == '0' || post_category == '1') {
    pool.getConnection((ex, conn) => {
      if (ex) {
        console.log(ex);
        conn.release();
      } else {
        // 제목
        if (search_content.category == '0') {
          pool.getConnection((ex, conn) => {
            if (ex) {
              console.log(ex);
            } else {
              var sql = 'select count(post_num) from post left join project as pjt on post_project = pjt.project_num where pjt.project_share = 0 and post_title like concat ("%",?,"%") and post_category = ?;'
              var sql_data = [search_content.text, post_category];
              var query = conn.query(sql, sql_data, function(err, result) {
                if (err) {
                  console.error(err);
                  throw err;
                }
                var page = result[0]["count(post_num)"];
                if (page % limit == 0) {
                  res.send(parseInt(page / limit) + "");
                } else {
                  res.send(parseInt(page / limit + 1) + "");
                }
              })
            }
            conn.release();
          })
        }

        // 내용
        if (search_content.category == '1') {
          pool.getConnection((ex, conn) => {
            if (ex) {
              console.log(ex);
            } else {
              var sql = 'select count(post_num) from post left join project as pjt on post_project = pjt.project_num where pjt.project_share = 0 and  post_content like concat ("%",?,"%") and post_category = ?;'
              var sql_data = [search_content.text, post_category];
              var query = conn.query(sql,sql_data, function(err, result) {
                if (err) {
                  console.error(err);
                  throw err;
                }
                var page = result[0]["count(post_num)"];
                if (page % limit == 0) {
                  res.send(parseInt(page / limit) + "");
                } else {
                  res.send(parseInt(page / limit + 1) + "");
                }
              })
            }
            conn.release();
          })
        }

        // 제목 + 내용
        if (search_content.category == '2') {
          console.log("여기냐 씨발?");
          pool.getConnection((ex, conn) => {
            if (ex) {
              console.log(ex);
            } else {
              var sql = 'select count(post_num) from post left join project as pjt on post_project = pjt.project_num where pjt.project_share = 0 and  (post_category = ?) and (post_content like concat ("%",?,"%") or post_title like concat ("%",?,"%"));'
              var sql_data = [post_category, search_content.text,     search_content.text ];
              var query = conn.query(sql,sql_data, function(err, result) {
                if (err) {
                  console.error(err);
                  throw err;
                }
                var page = result[0]["count(post_num)"];
                if (page % limit == 0) {
                  res.send(parseInt(page / limit) + "");
                } else {
                  res.send(parseInt(page / limit + 1) + "");
                }
              })
            }
            conn.release();
          })
        }

        // ID
        if (search_content.category == '3') {
          pool.getConnection((ex, conn) => {
            if (ex) {
              console.log(ex);
            } else {
              var sql = 'select count(post_num) from post as p inner join (select * from user where user_id like concat ("%",?,"%")) as u on p.post_user = u.user_num left join project as pjt on post_project = pjt.project_num where pjt.project_share = 0 and  p.post_category = ?;'
              var sql_data = [search_content.text, post_category];
              var query = conn.query(sql, sql_data,function(err, result) {
                if (err) {
                  console.error(err);
                  throw err;
                }
                var page = result[0]["count(post_num)"];
                if (page % limit == 0) {
                  res.send(parseInt(page / limit) + "");
                } else {
                  res.send(parseInt(page / limit + 1) + "");
                }
              })
            }
            conn.release();
          })
        }

        // TAG
        if (search_content.category == '4') {
          pool.getConnection((ex, conn) => {
            if (ex) {
              console.log(ex);
            } else {
              var sql = 'select count(post_num) from (select * from post where post_category = ? )as p inner join (select * from tag where tag_name like concat("%",?,"%")) as t on p.post_num = t.tag_post left join project as pjt on post_project = pjt.project_num where pjt.project_share = 0;'
              var sql_data = [post_category,search_content.text];
              var query = conn.query(sql, sql_data, function(err, result) {
                if (err) {
                  console.error(err);
                  throw err;
                }
                var page = result[0]["count(post_num)"];
                if (page % limit == 0) {
                  res.send(parseInt(page / limit) + "");
                } else {
                  res.send(parseInt(page / limit + 1) + "");
                }
              })
            }
            conn.release();
          })
        }
      }
    })
  } else if (post_category == '2') {
    if (search_content.category == '0') {
      pool.getConnection((ex, conn) => {
        if (ex) {
          console.log(ex);
        } else {
          var sql = 'select count(post_num) from post left join project as pjt on post_project = pjt.project_num where pjt.project_share = 0 and post_title like concat ("%",?,"%");'
          var sql_data = search_content.text;
          var query = conn.query(sql, sql_data, function(err, result) {
            if (err) {
              console.error(err);
              throw err;
            }
            var page = result[0]["count(post_num)"];
            if (page % limit == 0) {
              res.send(parseInt(page / limit) + "");
            } else {
              res.send(parseInt(page / limit + 1) + "");
            }
          })
        }
        conn.release();
      })
    }

    // 내용
    if (search_content.category == '1') {
      pool.getConnection((ex, conn) => {
        if (ex) {
          console.log(ex);
        } else {
          var sql = 'select count(post_num) from post left join project as pjt on post_project = pjt.project_num where pjt.project_share = 0 and  post_content like concat ("%",?,"%");'
          var sql_data = search_content.text;
          var query = conn.query(sql,sql_data, function(err, result) {
            if (err) {
              console.error(err);
              throw err;
            }
            var page = result[0]["count(post_num)"];
            if (page % limit == 0) {
              res.send(parseInt(page / limit) + "");
            } else {
              res.send(parseInt(page / limit + 1) + "");
            }
          })
        }
        conn.release();
      })
    }

    // 제목 + 내용
    if (search_content.category == '2') {
      pool.getConnection((ex, conn) => {
        if (ex) {
          console.log(ex);
        } else {
          var sql = 'select count(post_num) from post left join project as pjt on post_project = pjt.project_num where pjt.project_share = 0 and  (post_content like concat ("%",?,"%") or post_title like concat ("%",?,"%"));'
          var sql_data = [search_content.text, search_content.text];
          var query = conn.query(sql,sql_data, function(err, result) {
            if (err) {
              console.error(err);
              throw err;
            }
            var page = result[0]["count(post_num)"];
            if (page % limit == 0) {
              res.send(parseInt(page / limit) + "");
            } else {
              res.send(parseInt(page / limit + 1) + "");
            }
          })
        }
        conn.release();
      })
    }

    // ID
    if (search_content.category == '3') {
      pool.getConnection((ex, conn) => {
        if (ex) {
          console.log(ex);
        } else {
          var sql = 'select count(post_num) from post as p inner join (select * from user where user_id like concat ("%",?,"%")) as u on p.post_user = u.user_num left join project as pjt on post_project = pjt.project_num where pjt.project_share = 0;'
          var sql_data = search_content.text;
          var query = conn.query(sql,sql_data, function(err, result) {
            if (err) {
              console.error(err);
              throw err;
            }
            var page = result[0]["count(post_num)"];
            if (page % limit == 0) {
              res.send(parseInt(page / limit) + "");
            } else {
              res.send(parseInt(page / limit + 1) + "");
            }
          })
        }
        conn.release();
      })
    }

    // TAG
    if (search_content.category == '4') {
      pool.getConnection((ex, conn) => {
        if (ex) {
          console.log(ex);
        } else {
          var sql = 'select count(post_num) from post as p inner join (select * from tag where tag_name like concat("%",?,"%")) as t on p.post_num = t.tag_post left join project as pjt on post_project = pjt.project_num where pjt.project_share = 0;'
          var sql_data = [search_content.text];
          var query = conn.query(sql, sql_data, function(err, result) {
            if (err) {
              console.error(err);
              throw err;
            }
            var page = result[0]["count(post_num)"];
            if (page % limit == 0) {
              res.send(parseInt(page / limit) + "");
            } else {
              res.send(parseInt(page / limit + 1) + "");
            }
          })
        }
        conn.release();
      })
    }
  } else {
    res.send("error");
  }
});

router.post('/listById/:id/:page', function(req, res, next) {
  var pool = db.getPool();

  var post_category = req.body.post_category;
  var start = req.params.page * limit;
  var flag = false;
  var user_num = req.params.id;

  if (post_category == '2') {
    var sql = 'select p.post_num, p.post_title, p.post_content, p.post_share, p.post_created_at, p.post_category, pjt.project_title, i.image_url, u.user_id, u.user_name from post as p left join imageconnector as ic on p.post_num = ic.imageconn_post left join image as i on ic.imageconn_image = i.image_num left join user as u on p.post_user = u.user_num left join project as pjt on pjt.project_num = p.post_project where u.user_num = ? order by p.post_num desc limit ?, ?;'
    var sql_data = [user_num, start, limit];
    flag = true;
  }
  else if(post_category == '0' || post_category == '1'){
    var sql = 'select p.post_num, p.post_title, p.post_content, p.post_share, p.post_created_at, p.post_category, pjt.project_title, i.image_url, u.user_id, u.user_name from post as p left join imageconnector as ic on p.post_num = ic.imageconn_post left join image as i on ic.imageconn_image = i.image_num left join user as u on p.post_user = u.user_num left join project as pjt on pjt.project_num = p.post_project where u.user_num = ? and p.post_category = ? order by p.post_num desc limit ?, ?;'
    var sql_data = [user_num, post_category, start, limit];
    flag = true;
  }
  else{
    res.send("fail");
  }

  if(flag){
    pool.getConnection((ex, conn) => {
      if (ex) {
        console.log(ex);
      } else {
        var query = conn.query(sql, sql_data, function(err, result) {
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
  }
});
router.post('/totalPageNumById/:id', function(req, res, next) {
  var pool = db.getPool();

  var user_num = req.params.id;
  var post_category = req.body.post_category;
  var flag = false;

  var sql;
  var sql_data;

  if (post_category == '0') {
    sql = 'select count(post_num) from post where post_user = ? and post_category = 0;'
    sql_data = [user_num];
    flag = true;
  } else if (post_category == '1') {
    sql = 'select count(post_num) from post where post_user = ? and post_category = 1;'
    sql_data = [user_num];
    flag = true;
  } else if (post_category == '2') {
    var sql = 'select count(post_num) from post where post_user = ?'
    sql_data = [user_num];
    flag = true;
  } else {
    res.send("error");
  }

  if(flag){
    pool.getConnection((ex, conn) => {
      if (ex) {
        console.log(ex);
      } else {
        var query = conn.query(sql, sql_data, function(err, result) {
          if (err) {
            console.error(err);
            throw err;
          }
          var page = result[0]["count(post_num)"];
          if (page % limit == 0) {
            res.send(parseInt(page / limit) + "");
          } else {
            res.send(parseInt(page / limit + 1) + "");
          }
        })
      }
      conn.release();
    })
  }
});

router.post('/project/list/:id', function(req, res, next) {
  var pool = db.getPool();

  var user_num = req.params.id;

  pool.getConnection((ex, conn) => {
    if (ex) {
      console.log(ex);
    } else {
      var sql = 'select project_num, project_title, project_status, project_category,team_name from (select * from project where project_team in (select m.member_team from blog.member as m where m.member_user = ?) or project_user = ?) as p left join team as t on p.project_team = t.team_num;'
      var query = conn.query(sql, [user_num, user_num], function(err, result) {
        if (err) {
          console.error(err);
          conn.release();
          throw err;
        }

        res.send(result)
      })
    }
    conn.release();
  })
});
module.exports = router;
