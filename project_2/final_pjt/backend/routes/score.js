var express = require("express");
var router = express.Router();

var Score = require("../models/score");

router.get("/", function(req, res) {
  Recipe.find(function(error, scores) {
    if (error) {
      console.log(error);
    } else {
      console.log(scores);
      res.send(scores);
    }
  });
});

router.post("/create", function(req, res) {
  if (!req.user) return res.status(404).json({ error: "login required" });
  var score = new Score(req.body);
  score.save(function(err) {
    if (err) {
      console.error(err);
      res.json({ result: 0 });
      return;
    }
    res.json({ result: 1 });
  });
});

router.post("/update/:score_id", (req, res) => {
  if (req.user._id != req.body.userid)
    return res.status(404).json({ error: "user not matched" });
  Score.update({ _id: req.params.score_id }, req.body, function(err, output) {
    if (err) return res.status(500).json({ error: "database failure" });
    if (!output.n) return res.status(404).json({ error: "score not found" });
    res.json({ message: "score updated" });
  });
});

router.delete("/delete/:score_id", (req, res) => {
  if (req.user._id != req.body.userid)
    return res.status(404).json({ error: "user not matched" });
  Score.remove({ _id: req.params.comment_id }, function(err, output) {
    if (err) return res.status(500).json({ error: "database failure" });
    if (!output.result.n)
      return res.status(404).json({ error: "score not found" });
    res.json({ message: "score deleted" });
  });
});

// router.get("/detail/:comment_id", function(req, res) {
//   Comment.findOne({ _id: req.params.comment_id }, function(err, comment) {
//     if (err) return res.status(500).json({ error: err });
//     if (!comment) return res.status(404).json({ error: "comment not found" });
//     res.jsoon(comment);
//   });
// });

module.exports = router;
