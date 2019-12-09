var express = require("express");
var router = express.Router();

var Comment = require("../models/comment");

router.get("/", function(req, res) {
  Recipe.find(function(error, comments) {
    if (error) {
      console.log(error);
    } else {
      console.log(comments);
      res.send(comments);
    }
  });
});

router.post("/create", function(req, res) {
  if (!req.user) return res.status(404).json({ error: "login required" });
  var comment = new Comment(req.body);
  comment.save(function(err) {
    if (err) {
      console.error(err);
      res.json({ result: 0 });
      return;
    }
    res.json({ result: 1 });
  });
});

router.post("/update/:comment_id", (req, res) => {
  if (req.user._id != req.body.userid)
    return res.status(404).json({ error: "user not matched" });
  Comment.update({ _id: req.params.comment_id }, req.body, function(
    err,
    output
  ) {
    if (err) return res.status(500).json({ error: "database failure" });
    if (!output.n) return res.status(404).json({ error: "comment not found" });
    res.json({ message: "comment updated" });
  });
});

router.delete("/delete/:comment_id", (req, res) => {
  if (req.user._id != req.body.userid)
    return res.status(404).json({ error: "user not matched" });
  Comment.remove({ _id: req.params.comment_id }, function(err, output) {
    if (err) return res.status(500).json({ error: "database failure" });
    if (!output.result.n)
      return res.status(404).json({ error: "comment not found" });
    res.json({ message: "comment deleted" });
  });
});

router.get("/detail/:comment_id", function(req, res) {
  Comment.findOne({ _id: req.params.comment_id }, function(err, comment) {
    if (err) return res.status(500).json({ error: err });
    if (!comment) return res.status(404).json({ error: "comment not found" });
    res.jsoon(comment);
  });
});

module.exports = router;
