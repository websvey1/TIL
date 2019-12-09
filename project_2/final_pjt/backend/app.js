var createError = require("http-errors");
var express = require("express");
var path = require("path");
var cookieParser = require("cookie-parser");
var logger = require("morgan");

// mongoose module 가져오기
var mongoose = require("mongoose");

// router connect
var indexRouter = require("./routes/index");
var usersRouter = require("./routes/users");
var commentRouter = require("./routes/comment");
var scoreRouter = require("./routes/score");
var recipeRouter = require("./routes/recipe");
var ingredientRouter = require("./routes/ingredient");

var app = express();

// view engine setup
app.set("views", path.join(__dirname, "views"));
app.set("view engine", "pug");

app.use(logger("dev"));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, "public")));

app.use("/", indexRouter);
app.use("/api/users", usersRouter);
app.use("/api/recipe", recipeRouter);
app.use("/api/score", scoreRouter);
app.use("/api/ingredient", ingredientRouter);
app.use("/api/comment", commentRouter);

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get("env") === "development" ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render("error");
});

// db connect
mongoose.connect("mongodb://localhost:27017/testDB", { useNewUrlParser: true });

var db = mongoose.connection;

// connection fail
db.on("error", function() {
  console.log("Connection Failed!");
});

// connection success
db.once("open", function() {
  console.log("Connected!");
});

module.exports = app;
