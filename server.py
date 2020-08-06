"""Server for movie ratings app."""

# increased flask
from flask import (Flask, render_template, request, flash, session,
                   redirect)

# created import allowing connection to database
from model import connect_to_db

# imported module to allow to create,read,update and delete database
import crud

app = Flask(__name__)

# imported Jinja secret key settings
from jinja2 import StrictUndefined
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


# created basic homepage route at index
@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')

# app route for all movies
@app.route('/movies')
def all_movies():
    """View all movies."""

    movies = crud.get_movies()

    return render_template('all_movies.html', movies=movies)

# app route for movie details
@app.route('/movies/<movie_id>')
def show_movie(movie_id):
  #Show details on a particular movie.

    movie = crud.get_movie_by_id(movie_id)

    return render_template('movie_details.html', movie=movie)

if __name__ == '__main__':
# added connection to database
	connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
