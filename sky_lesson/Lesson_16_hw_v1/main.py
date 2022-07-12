# -*- coding: utf-8 -*-
from flask import request
import json
from config import app
from models import User, Order, Offer
from utils import init_db, get_all, get_all_by_id, insert_data_uninersal, update_universal_v2, delete_universal


@app.route('/userss/')
def get_userss():
    """Выводит всех юзеров - рабочий """
    data = User().query.all()
    return "<br/>".join(
        [f"{d.id}  {d.first_name}  {d.last_name}  {d.age}  {d.email}  {d.role}  {d.phone}" for d in data])


@app.route('/userss/<int:id>')
def get_userss_by_id(id: int):
    """Выводит данные юзера по id"""
    data = User().query.get(id)
    if data is None:
        return "user is no found"
    return json.dumps(
        f"{data.id}  {data.first_name}  {data.last_name}  {data.age}  {data.email}  {data.role}  {data.phone}")


@app.route("/users/", methods=['GET', 'POST'])
def get_users():
    if request.method == 'GET':
        return app.response_class(
            print(get_all(User)),
            response=json.dumps(get_all(User), indent=4, ensure_ascii=False),
            status=200,
            minetype='application/json'
        )

    elif request.method == 'POST':
        if isinstance(request.json, list):
            insert_data_uninersal(User, request.json)
        elif isinstance(request.json, dict):
            insert_data_uninersal(User, [request.json])

        return app.response_class(
            response=json.dumps(request.json, indent=4, ensure_ascii=False),
            status=200,
            # minetype="application/json"
        )


@app.route("/orders/", methods=['GET', 'POST'])
def get_orders():
    if request.method == 'GET':
        return app.response_class(
            response=json.dumps(get_all(Order), indent=4, ensure_ascii=False),
            status=200,
            # minetype="application/json"
        )

    elif request.method == 'POST':
        if isinstance(request.json, list):
            insert_data_uninersal(Order, request.json)
        elif isinstance(request.json, dict):
            insert_data_uninersal(Order, [request.json])

        return app.response_class(
            response=json.dumps(request.json, indent=4, ensure_ascii=False),
            status=200,
            # minetype="application/json"
        )


@app.route("/offers/", methods=['GET', 'POST'])
def get_offers():
    if request.method == 'GET':
        return app.response_class(
            response=json.dumps(get_all(Offer), indent=4, ensure_ascii=False),
            status=200,
            # minetype="application/json"
        )

    elif request.method == 'POST':
        if isinstance(request.json, list):
            insert_data_uninersal(Offer, request.json)
        elif isinstance(request.json, dict):
            insert_data_uninersal(Offer, [request.json])

        return app.response_class(
            response=json.dumps(request.json, indent=4, ensure_ascii=False),
            status=200,
            # minetype="application/json"
        )


@app.route("/users/<int:user_id>", methods=['GET', 'POST'])
def get_user_by_id(user_id: int):
    if request.method == 'GET':
        data = get_all_by_id(User, user_id)
        return app.response_class(
            response=json.dumps(data, indent=4, ensure_ascii=False),
            status=200,
            # minetype="application/json"
        )

    elif request.method == 'PUT':
        update_universal_v2(User, user_id, request.json)
        return app.response_class(
            response=json.dumps(['ок'], indent=4, ensure_ascii=False),
            status=200,
            # minetype="application/json"
        )

    elif request.method == 'DELETE':
        delete_universal_v2(User, user_id)
        return app.response_class(
            response=json.dumps(['ок'], indent=4, ensure_ascii=False),
            status=200,
            # minetype="application/json"
        )


@app.route("/orders/<int:user_id>", methods=['GET', 'POST'])
def get_orders_by_id(user_id: int):
    if request.method == 'GET':
        data = get_all_by_id(Order, user_id)

        return app.response_class(
            response=json.dumps(data, indent=4, ensure_ascii=False),
            status=200,
            # minetype="application/json"
        )

    elif request.method == 'PUT':
        update_universal_v2(Order, user_id, request.json)
        return app.response_class(
            response=json.dumps(['ок'], indent=4, ensure_ascii=False),
            status=200,
            # minetype="application/json"
        )

    elif request.method == 'DELETE':
        delete_universal_v2(Order, user_id)
        return app.response_class(
            response=json.dumps(['ок'], indent=4, ensure_ascii=False),
            status=200,
            # minetype="application/json"
        )


@app.route("/offers/<int:user_id>", methods=['GET', 'POST'])
def get_offers_by_id(user_id: int):
    if request.method == 'GET':
        data = get_all_by_id(Offer, user_id)

        return app.response_class(
            response=json.dumps(data, indent=4, ensure_ascii=False),
            status=200,
            # minetype="application/json"
        )

    elif request.method == 'PUT':
        update_universal_v2(Offer, user_id, request.json)
        return app.response_class(
            response=json.dumps(['ок'], indent=4, ensure_ascii=False),
            status=200,
            # minetype="application/json"
        )

    elif request.method == 'DELETE':
        delete_universal_v2(Offer, user_id)
        return app.response_class(
            response=json.dumps(['ок'], indent=4, ensureascii=False),
            status=200,
            # minetype="application/json"
        )


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>Страница не найдена</h1><p>Поищите другую!</p>", 404


if __name__ == '__main__':
    init_db()
    app.run(debug=True)