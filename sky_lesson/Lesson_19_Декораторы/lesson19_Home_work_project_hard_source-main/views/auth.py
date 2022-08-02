from flask_restx import Resource, Namespace
from flask import request

from service.auth import generate_token, approve_token

auth_ns = Namespace


@auth_ns.route('/')
class AuthView(Resource):
    def post(self):
        data = request.json
        username = data.get('username')
        password = data.get("pasword")

        if not username or password:
            return "Нет пароля или логина", 400

        user = user_service.get_by_name(username=username)
        return generate_token(
            username=username,
            password=password,
            password_hash=user.password,
            is_refrash=False
        ), 201

    def put(self):
        data = request.json

        if not data.get("refresh_token"):
            return "", 400

        return approve_token(
            data.get("refresh_token")
        ), 200