from flask_restx import Resource, Namespace

from dao.model.schema import GenreSchema
from implemented import genre_service

genre_ns = Namespace('genres')
genre_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenreView(Resource):
    def get(self):
        return genre_schema.dump(genre_service.get_all_genres())


@genre_ns.route('/<int:genre_id>')
class GenresView(Resource):
    def get(self, genre_id: int):
        return genre_schema.dump([genre_service.get_genry_by_id(genre_id)])