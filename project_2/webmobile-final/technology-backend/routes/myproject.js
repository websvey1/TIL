var express = require('express');
var router = express.Router();
var db = require("../database");

/////////////////////////////////////////// create //////////////////////////////////////////
router.post('/create', function(req, res, next) {
  var pool = db.getPool();

  var user = req.body.user;
  var title = req.body.title;
  var goal = req.body.goal;
  var status = req.body.status;
  var start_date = req.body.start_date;
  var end_date = req.body.end_date;
  var git_url = req.body.git_url;
  var content = req.body.content;
  var tech = req.body.tech;
  var share = req.body.share;
  var category = '0';
  var images = req.body.imgArray;
  console.log(req.body)

  pool.getConnection((ex, conn) => {
      if(ex){
        console.log(ex, 'ex');
      }
      else{
        console.log()
        var query = conn.query('insert into project(project_user, project_title, project_goal, project_start_date, project_end_date,' +
        'project_tech,project_content,project_status,project_git_url,project_share, project_category)' +
        'values("'+ user + '","' + title + '","' + goal + '","' + start_date + '","' + end_date + '","' + tech + '","' + content + '","' +
        status + '","' + git_url + '","' + share + '","' + category + '")',
          (err, result) => {
          if (err) {
            console.error(err,'err');
            throw err;
          }

          var project_num = result.insertId;
          var img_query = 'insert into image(image_url) values';

          if (images.length > 0) {
            for (var i=0; i < images.length; i++) {
              var img = images[i]
              // console.log(img)
              img_query += '("' + img + '")';
              if (i+1 == images.length) {
                img_query += ';'
              } else {
                img_query += ','
              }
            }

            var imgquery = conn.query(img_query, (err, result) => {
              if (err) {
                console.error(err);
                throw err;
              }
              var image_num = result.insertId;
              // console.log(image_num);

              var imgleng = images.length;
              var imgcnt = image_num + images.length
              // console.log(imgleng)

              var imgconn_query = 'insert into imageconnector(imageconn_image, imageconn_project, imageconn_category, imageconn_index) values';
              for (var j=0; image_num + j < imgcnt; j++) {
                var imgnum = image_num + j
                imgconn_query += '(' + imgnum + ',' + project_num + ', 0, 0)'
                if (imgnum == imgcnt - 1) {
                  imgconn_query += ';'
                } else {
                  imgconn_query += ','
                }
              }

              // console.log(imgconn_query)
              var imgconnquery = conn.query(imgconn_query, (err, result) => {
                if (err) {
                  console.error(err);
                  throw err;
                }
                res.send("Success");
              })
            })
          } else {
            res.send("Out of range");
          }
        });
      }
      conn.release();
  });
});


/////////////////////////////////////////// Read //////////////////////////////////////////
router.post('/getPjt', function(req, res, next) {
  var pool = db.getPool();

  pool.getConnection((ex, conn) => {
    if (ex) {
      console.log(ex);
    }
    else {
      var query = conn.query('select project_num, project_user from project where project_share = 0 and project_category = 0', function (err, result) {
        if (err) {
          console.log(err);
          throw err;
        }
        res.send(result);
      });
    }
    conn.release();
  });
})

/////////////////////////////// ProjectList.vue에서 제목이 포함된 project만을 가져오려고 사용하는 것 ///////////////////////////////
router.post('/searchNameProject', function(req, res, next) {
  var content = req.body.content;
  var pool = db.getPool();

  pool.getConnection((ex, conn) => {
    if (ex) {
      console.log(ex);
    }
    else {
      var query = conn.query('select project_num, project_user from project where project_share = 0 and project_category = 0 and project_title like concat("%", ?, "%")', content, function (err, result) {
        if (err) {
          console.log(err);
          throw err;
        }
        res.send(result);
      });
    }
    conn.release();
  });
})
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

/////////////////////////////// ProjectList.vue에서 제목이 포함된 project만을 가져오려고 사용하는 것 ///////////////////////////////
router.post('/searchContProject', function(req, res, next) {
  var content = req.body.content;
  var pool = db.getPool();

  pool.getConnection((ex, conn) => {
    if (ex) {
      console.log(ex);
    }
    else {
      var query = conn.query('select project_num, project_user from project where project_share = 0 and project_category = 0 and project_content like concat("%", ?, "%")', content, function (err, result) {
        if (err) {
          console.log(err);
          throw err;
        }
        res.send(result);
      });
    }
    conn.release();
  });
})
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
router.post('/userproject', function(req, res, next) {
  var pool = db.getPool();
  var userNum = req.body.userNum

  pool.getConnection((ex, conn) => {
    if (ex){
      console.log(ex)
    }
    else {
      var query = conn.query('select project_num from project where project_user = ? and project_category = 0', userNum, function(err, result) {
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

router.post('/getProject', function(req, res, next) {
  var pool = db.getPool();
  var pjtNum = req.body.pjtNum;

  pool.getConnection((ex, conn) => {
    if (ex){
      console.log(ex);
    }
    else {
      var query = conn.query('select p.*, u.user_id from project as p inner join user as u on p.project_user = u.user_num where project_num = ' + pjtNum + ';', function(err, result) {
        if (err) {
          console.log(err);
          throw err;
        }

        var project = {
          project: result,
          image: null
        }

        var query = conn.query('select i.image_num, i.image_url from project as pjt inner join imageconnector as ic on ic.imageconn_project = pjt.project_num inner join image as i on ic.imageconn_image = i.image_num where ic.imageconn_project =' + pjtNum + ';',
        function(err, result) {
          if (err) {
            console.error(err);
            conn.release();
            throw err;
          }

          console.log(result)
          if (result.length > 0) {
            project.image = result[0].image_url
          }
          else {
            project.image = 'https://source.unsplash.com/random/300x300'
          }

          res.send(project);
        })

      })
    }
    conn.release();
  })

})


router.get('/:id', function(req, res, next) {
  var pool = db.getPool();

  var project_num = req.params.id;
  // console.log(project_num);

  pool.getConnection((ex, conn) => {
    if (ex) {
      console.log(ex);
    }
    else {
      var query = conn.query('select * from project where project_num = ' + project_num + ';',
        function(err, result) {
          if (err) {
            console.error(err);
            conn.release();
            throw err;
          }

          // console.log(result);
          var project = {
            project: result,
            images: null,
          }

          var query = conn.query('select i.image_num, i.image_url from project as pjt inner join imageconnector as ic on ic.imageconn_project = pjt.project_num inner join image as i on ic.imageconn_image = i.image_num where ic.imageconn_project =' + project_num + ';',
          function(err, result) {
            if (err) {
              console.error(err);
              conn.release();
              throw err;
            }

            var image = []
            console.log(result);
            for (var i=0; i < result.length; i++){
              image.push({imgnum: result[i].image_num, imgurl: result[i].image_url});
            }
            project.images = image
            res.send(project);
          })
        })
      }
    conn.release();
  })
})

/////////////////////////////////////////// update //////////////////////////////////////////
router.post('/update/getProject', function(req, res, next) {
  var pool = db.getPool();
  var pjtNum = req.body.pjtNum

  pool.getConnection((ex, conn) => {
    if (ex){
      console.log(ex)
    }
    else {
      var query = conn.query('select * from project where project_category = 0 and project_num = ?', pjtNum,
      function(err, result) {
        if (err){
          console.error(err)
          throw err
        }

        var project = {
          project: result,
          images: null
        }

        var query = conn.query('select i.image_num, i.image_url from project as pjt inner join imageconnector as ic on ic.imageconn_project = pjt.project_num inner join image as i on ic.imageconn_image = i.image_num where ic.imageconn_project =' + pjtNum + ';',
        function(err, result) {
          if (err) {
            console.error(err);
            conn.release();
            throw err;
          }

          var image = []
          for (var i=0; i < result.length; i++){
            image.push({imgnum: result[i].image_num, imgurl: result[i].image_url});
          }

          project.images = image
          res.send(project);
        })
      })
    }
    conn.release()
  })
})

router.post('/delete/image', function(req, res, next) {
  var pool = db.getPool();
  var imgNum = req.body.imgNum;

  pool.getConnection((ex, conn) => {
    if (ex){
      console.log(ex)
    }
    else {
      var query = conn.query('delete from image where image_num = ?', imgNum,
      function(err, result) {
        if (err){
          console.error(err)
          throw err
        }
        res.send("Success")
      })
    }
    conn.release()
  })
})

router.post('/delete/project', function(req, res, next) {
  var pool = db.getPool();
  var pjtNum = req.body.pjtNum

  pool.getConnection((ex, conn) => {
    if (ex){
      console.log(ex)
    }
    else {
      var query = conn.query('delete from project where project_num = ?', pjtNum,
      function(err, result) {
        if (err){
          console.error(err)
          throw err
        }
        res.send('DeleteSucess')
      })
    }
    conn.release()
  })
})

router.post('/update/project', function(req, res, next) {
  var pool = db.getPool();
  var pjtNum = req.body.pjtNum;
  var project = req.body.project;
  console.log(project)

  pool.getConnection((ex, conn) => {
    if (ex) {
      console.log(ex)
    }
    else {
      var query = conn.query('update project set project_title = ?, project_goal = ?, project_status = ?, project_start_date = ?, project_end_date = ?, project_content = ?, project_tech = ?, project_share = ?, project_git_url = ?, project_updated_at = now() where project_num = ' + pjtNum + ';',
      [project.project_title, project.project_goal, project.project_status, project.project_start_date, project.project_end_date, project.project_content, project.project_tech, project.project_share, project.project_git_url],
      function(err, result) {
        if (err){
          console.err(err)
          throw err
        }
        res.send("UpdateProjectSuccess")
      })
    }
    conn.release()
  })
})

router.post('/update/images', function(req, res, next) {
  var pool = db.getPool();
  console.log(req.body)
  var pjtNum = req.body.pjtNum
  var imgUrl = req.body.imgUrl

  pool.getConnection((ex, conn) => {
    if (ex) {
      console.log(ex)
    }
    else {
      var query = conn.query('insert into image(image_url) values (?)', imgUrl, function(err, result) {
        if (err){
          console.error(err)
          throw err
        }

        var imgNum = result.insertId;
        console.log(imgNum)

        var query = conn.query('insert into imageconnector(imageconn_image, imageconn_project, imageconn_category, imageconn_index) values (?, ?, 0, 0)',
        [imgNum, pjtNum], function(err, result) {
          if(err) {
            console.error(err)
            throw err
          }

          var image = {
            imgnum: imgNum,
            imgurl: req.body.imgUrl
          }
          console.log(image)
          res.send(image)
        })
      })
    }
  })
})

////////////////// 개인 project에서, post 작성할 때- 해당 project가 개인 project인지 확인하기 위해서 /////////////////////
router.post('/getCategory', function(req, res, next) {
  var pool = db.getPool();
  var pjtNum = req.body.pjtNum

  pool.getConnection((ex, conn) => {
    if (ex){
      console.log(ex)
    }
    else {
      var query = conn.query('select project_category from project where project_num = ?', pjtNum, function(err, result) {
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
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////// MyPostPage에서 현재 Project Name 가져오기 위함 ////////////////////////////////////
router.post('/getProjectName', function(req, res, next){
  var pjtNum = req.body.pjtNum
  var pool = db.getPool()
  pool.getConnection((ex, conn) => {
    if (ex){
      console.log(ex)
    }
    else {
      var query = conn.query('select project_title from project where project_num = ?', pjtNum, function(err, result) {
        if (err){
          console.error(err)
          throw err
        }
        res.send(result)
      })
    }
    conn.release();
  })
})
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

/////////////////////////////// MyprojectRead에서 밑에 Post 부분에 들어갈 post들 가져오기 위함 ////////////////////////////
router.post('/getPost', function(req, res, next){
  var pjtNum = req.body.num
  var pool = db.getPool()
  // console.log(pjtNum)
  pool.getConnection((ex, conn) => {
    if (ex){
      console.log(ex)
    }
    else {
      var query = conn.query('select * from post as p inner join user as u on p.post_user = u.user_num where p.post_project = ?', pjtNum, function(err, result) {
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
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

module.exports = router;
