const mongoose = require("mongoose");

const scoreSchema = new mongoose.Schema({
  recipeid: { type: mongoose.Types.ObjectId, ref: "recipe", required: true },
  userid: { type: mongoose.Types.ObjectId, ref: "user", required: true },
  score: { type: Number, required: true }
});

module.exports = mongoose.model("Score", scoreSchema);
