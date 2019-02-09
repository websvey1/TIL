from flask import Flask, render_template, url_for, request, redirect
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, Movie

app = Flask(__name__) ##

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_flask.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
@app.route('/movies/')
def index():
    movies = Movie.query.all()
    return render_template('index.html', movies=movies)
    
@app.route('/movies/new/')
def new():
    return render_template('new.html')

@app.route('/movies/create/')
def create():
    title = request.args.get('title')
    title_en = request.args.get('title_en')
    audience = request.args.get('audience')
    open_date = request.args.get('open_date')
    genre = request.args.get('genre')
    watch_grade =request.args.get('watch_grade') 
    score = request.args.get('score')
    poster_url = request.args.get('poster_url')
    description = request.args.get('description')
    
    movies = Movie(title=title, title_en=title_en, audience=audience,
    open_date=open_date, genre=genre, watch_grade=watch_grade, score=score,
    poster_url=poster_url, description=description)
    
    db.session.add(movies)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/movies/<int:id>/')
def show(id):
    movies = Movie.query.get(id)
    return render_template('show.html', movies=movies)

@app.route('/movies/<int:id>/edit/')
def edit(id):
    movies= Movie.query.get(id)
    return render_template('edit.html', movies=movies)

@app.route('/movies/<int:id>/update/')
def update(id):
    movies=Movie.query.get(id)
    movies.title = request.args.get('title')
    movies.title_en = request.args.get('title_en')
    movies.audience = request.args.get('audience')
    movies.open_date = request.args.get('open_date')
    movies.genre = request.args.get('genre')
    movies.watch_grade = request.args.get('watch_grade')
    movies.score = request.args.get('score')
    movies.poster_url = request.args.get('poster_url')
    movies.description = request.args.get('description')
    
    db.session.commit()
    return redirect(f'/movies/{movies.id}/')
    
@app.route('/movies/<int:id>/delete/')
def delete(id):
    movies=Movie.query.get(id)
    db.session.delete(movies)
    db.session.commit()
    return redirect(f'/movies/')
    
    
    









    
    
if __name__ == "__main__":
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)
