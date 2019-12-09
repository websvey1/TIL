const mongoose = require("mongoose");

const recipeSchema = new mongoose.Schema({
  name: { type: String, required: true },
  userid: { type: mongoose.Types.ObjectId, ref: "user", required: true },
  ingredients: { type: Array, required: true },
  info: { type: Array, required: true },
  picture: { type: String, required: true }
});

module.exports = mongoose.model("Recipe", recipeSchema);
