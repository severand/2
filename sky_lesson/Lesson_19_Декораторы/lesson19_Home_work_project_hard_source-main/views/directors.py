from flask_restx import Resource, Namespace
from flask import request

from dao.model.director import DirectorSchema
from implemented import director_service

from service.decorators import auth_required, admin_required

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    @auth_required
    def get(self):
        rs = director_service.get_all()
        res = DirectorSchema(many=True).dump(rs)
        return res, 200

    @admin_required
    def post(self):
        """Новый режиссер"""
        req_json = request.json
        director = director_service.create(req_json)
        return "", 201, {"location": f"/directors/{direcor.id}"}


@director_ns.route('/<int:rid>')
class DirectorView(Resource):
    @auth_required
    def get(self, rid):
        r = director_service.get_one(rid)
        sm_d = DirectorSchema().dump(r)
        return sm_d, 200

    @auth_required
    def put(self, rid: int):
        """Изменения"""
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = rid
        director_service.update(req_json)
        return "", 204

    @admin_required
    def delete(self, rid: int):
        "Удаление"
        director_service.delete(rid)
        return "", 204