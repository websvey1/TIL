const mongoose = require("mongoose");

const commentSchema = new mongoose.Schema({
  recipeid: { type: mongoose.Types.ObjectId, ref: "recipe", required: true },
  userid: { type: mongoose.Types.ObjectId, ref: "user", required: true },
  content: { type: String, required: true },
  createdAt: { type: Date, default: Date.now() }
});

module.exports = mongoose.model("Comment", commentSchema);
