var express = require("express");
var router = express.Router();

var Recipe = require("../models/recipe");

router.get("/", function(req, res) {
  Recipe.find(function(error, recipes) {
    if (error) {
      console.log(error);
    } else {
      console.log(recipes);
      res.send(recipes);
    }
  });
});

// router.post("/create", function(req, res) {
//   var recipe = new Recipe();
//   recipe.name = req.body.name;
//   recipe.userid = req.body.userid;
//   recipe.ingredients = [[0], [0]];
//   recipe.info = [[1], [1]];
//   recipe.picture = "hi";

//   recipe.save(function(err) {
//     if (err) {
//       console.error(err);
//       res.json({ result: 0 });
//       return;
//     }

//     res.json({ result: 1 });
//   });
// });

router.post("/create", function(req, res) {
  if (!req.user) return res.status(404).json({ error: "login required" });
  var recipe = new Recipe(req.body);
  recipe.save(function(err) {
    if (err) {
      console.error(err);
      res.json({ result: 0 });
      return;
    }
    res.json({ result: 1 });
  });
});

router.post("/update/:recipe_id", (req, res) => {
  if (req.user._id != req.body.userid)
    return res.status(404).json({ error: "user not matched" });
  Recipe.update({ _id: req.params.recipe_id }, req.body, function(err, output) {
    if (err) return res.status(500).json({ error: "database failure" });
    if (!output.n) return res.status(404).json({ error: "recipe not found" });
    res.json({ message: "recipe updated" });
  });
});

router.delete("/delete/:recipe_id", (req, res) => {
  if (req.user._id != req.body.userid)
    return res.status(404).json({ error: "user not matched" });
  Recipe.remove({ _id: req.params.recipe_id }, function(err, output) {
    if (err) return res.status(500).json({ error: "database failure" });
    if (!output.result.n)
      return res.status(404).json({ error: "recipe not found" });
    res.json({ message: "recipe deleted" });
  });
});

router.get("/detail/:recipe_id", function(req, res) {
  Recipe.findOne({ _id: req.params.recipe_id }, function(err, recipe) {
    if (err) return res.status(500).json({ error: err });
    if (!recipe) return res.status(404).json({ error: "recipe not found" });
    res.jsoon(recipe);
  });
});

module.exports = router;
