var express = require("express");
var router = express.Router();

var Ingredient = require("../models/ingredient");

router.get("/detail/:ingredient_id", function(req, res) {
  Ingredient.findOne({ _id: req.params.ingredient_id }, function(
    err,
    ingredient
  ) {
    if (err) return res.status(500).json({ error: err });
    if (!ingredient)
      return res.status(404).json({ error: "ingredient not found" });
    res.jsoon(ingredient);
  });
});

module.exports = router;
