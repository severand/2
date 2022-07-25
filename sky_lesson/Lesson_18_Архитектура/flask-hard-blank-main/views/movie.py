# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service

# Пример

from flask_restx import Resource, Namespace
from flask import request

from dao.model.schema import MovieSchema
from implemented import movie_service

movie_ns = Namespace('movies')
movie_schema_one = MovieSchema()
movie_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        if len(request.args) > 0:
            return movie_schema.dump(movie_service.get_movie_by(
                **request.args
            ))

        else:
            return movie_schema.dump(movie_service.get_movies()), 200

    def post(self):
        if movie_service.add_file(request.json):
            return "", 200
        else:
            return "", 503


@movie_ns.route('/<int:movie_id>')
class MoviesView(Resource):
    def get(self, movie_id: int):
        """Фильм по id"""
        return movie_schema.dump([movie_service.get_movie_by_id(movie_id)])

    def put(self, movie_id: int):
        movie_service.update_film(request.json)
        return "", 201

    def delete(self, movie_id: int):
        movie_service.delete_film(movie_id)
        return "", 201