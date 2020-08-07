"""CRUD operations."""

from model import db, User, Movie, Rating, connect_to_db
# instructions omit mention of need to import dateime
import datetime

# Functions start here!
# note patterrn in set up of user and movie and rating and way name function, parameters, default values, add, commit and return items, with Uppercase for table name
# note that rating's parameters include user and movie, tables that are related.
# test calling
# load this file using ipython in venv
# create entry by calling function with required parameters
# add and commit are already in the database
# create_user('john','john.doe@email.com')
# create_movie("My First Movie","My first movie is the story of...","2018, 10,31", "w
#    ...: ww.yahoo.com")
# create_rating("john","My First Movie","5")

# when ready drop db, createdb, db.create_all
# Go to seed_database.py discussion to 
# populate with data/movies.json

# create 10 random users and ratings on random moves with random scores
# once both crud and seed_database.py files are complete
# from virtual environment, lod seed_database
# python3 seed_database.py
# check with ipython -i model.py
# note that the instructions have a typo on check
#  In [5]: for user_rating in rating.user.ratings: 
#  ...:     print(user_rating.score)  
#  not ratings.user

"""CRUD operations."""

from model import db, User, Movie, Rating, connect_to_db


def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user


def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""

    movie = Movie(title=title,
                  overview=overview,
                  release_date=release_date,
                  poster_path=poster_path)

    db.session.add(movie)
    db.session.commit()

    return movie


def create_rating(user, movie, score):
    """Create and return a new rating."""

    rating = Rating(user=user, movie=movie, score=score)

    db.session.add(rating)
    db.session.commit()

    return rating

# get all movies
def get_movies():
    """Return all movies."""

    return Movie.query.all()

# return movie by id
def get_movie_by_id(movie_id):

    return Movie.query.get(1)

# get all Users
def get_users():
    """Return all movies."""

    return Users.query.all()

if __name__ == '__main__':
    from server import app
    connect_to_db(app)
