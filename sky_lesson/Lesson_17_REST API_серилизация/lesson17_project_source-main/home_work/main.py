from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api, Namespace, Resource

from config import app
from config import db

from models import Movie, Director, Genre
import schema

# db.init_app(app)


api = Api(app)

movies_ns = api.namespace('movies')
directors_ns = api.namespace('directors')
genres_ns = api.namespace('genres')

movie_schema = schema.MovieSchema()
movies_schema = schema.MovieSchema(many=True)

director_schema = schema.DirectorSchema()
directors_schema = schema.DirectorSchema(many=True)

genre_schema = schema.GenreSchema()
genres_schema = schema.GenreSchema(many=True)


@movies_ns.route('/<int:movie_id>')
class MovieView(Resource):
    def get(self, movie_id: int):
        movie = db.session.query(Movie).filter(Movie.id == movie_id).one()

        if movie is None:
            return "Movie is no found", 404

        return movie_schema.dump(movie), 200

    def put(self, movie_id: int):
        update_row = db.session.query(Movie).filter(Movie.id == movie_id).update(request.json)
        if update_row == 1:
            db.session.commit()
            return None, 204

        return None, 400

    def delete(self, movie_id: int):
        delete_row = db.session.query(Movie).filter(Movie.id == movie_id).delete()
        if delete_row == 1:
            db.session.commit()
            return None, 204

        return None, 400


@movies_ns.route('/')
class MoviesView(Resource):

    def get(self):
        movies_query = db.session.query(Movie)

        args = request.args

        print(args)

        director_id = args.get('director_id')
        if director_id is not None:
            movies_query = movies_query.filter(Movie.director_id == director_id)

        genre_id = args.get('genre_id')
        if genre_id is not None:
            movies_query = movies_query.filter(Movie.genre_id == genre_id)

        movies = movies_query.all()

        return movies_schema.dump(movies), 200

    def post(self):
        movies = movies_schema.load(request.json)
        db.session.add(Movie(**movies))
        db.session.commit()

        return None, 201


@directors_ns.route('/<int:director_id>')
class DirectorView(Resource):
    def get(self, director_id: int):
        director = db.session.query(Director).filter(Director.id == director_id).one()

        if director is None:
            return "Director is no found", 404

        return director_schema.dump(director), 200


@directors_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        directors = db.session.query(Director).all()

        return directors_schema.dump(directors), 200


@genres_ns.route('/<int:genre_id>')
class GenreView(Resource):
    def get(self, genre_id: int):
        genre = db.session.query(Genre).filter(Genre.id == genre_id).one()

        if genre is None:
            return "Genre is no found", 404

        return genre_schema.dump(genre), 200


@genres_ns.route('/')
class GenresView(Resource):
    def get(self):
        genres = db.session.query(Genre).all()

        return genres_schema.dump(genres), 200


if __name__ == '__main__':
    app.run(debug=True)