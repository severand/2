from flask_restx import Resource, Namespace

from dao.model.schema import DirectorSchema
from implemented import director_service

director_ns = Namespace('directors')
director_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorView(Resource):
    def get(self):
        return director_schema.dump(director_service.get_directors())


@director_ns.route('/<int:director_id>')
class DirectorsView(Resource):
    def get(self, director_id: int):
        return director_schema.dump([director_service.get_director_by_id(director_id)])