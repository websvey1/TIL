const mongoose = require("mongoose");

const ingredientSchema = new mongoose.Schema({
  name: { type: String, required: true, unique: true },
  picture: { type: String, required: true }
});

module.exports = mongoose.model("Ingedient", ingredientSchema);
