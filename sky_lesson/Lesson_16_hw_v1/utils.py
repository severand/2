from models import *
from config import db
import json


def insert_all_users(input_data):
    for item in input_data:
        db.session.add(
            User(
                id=item['id'],
                first_name=item['first_name'],
                last_name=item['last_name'],
                age=item['age'],
                email=item['email'],
                role=item['role'],
                phone=item['phone']
            )
        )
    db.session.commit()


def insert_all_orders(input_data):
    for item in input_data:
        db.session.add(
            Order(
                id=item['id'],
                name=item['name'],
                description=item['description'],
                start_date=item['start_date'],
                end_date=item['end_date'],
                address=item['address'],
                price=item['price'],
                customer_id=item['customer_id'],
                executor_id=item['executor_id']
            )
        )
    db.session.commit()


def insert_all_offers(input_data):
    for item in input_data:
        db.session.add(
            Offer(
                id=item['id'],
                order_id=item['order_id'],
                executor_id=item['executor_id']
            )
        )
    db.session.commit()


def insert_data_uninersal(model, input_data):
    for row in input_data:
        db.session.add(
            model(
                **row
            )
        )
    db.session.commit()


def get_all(model):
    result = []
    for row in db.session.query(model).all():
        result.append(row.to_dict)
    return result


def get_all_by_id(model, user_id):
    try:
        return db.session.query(model).get(user_id).to_dict
    except Exception:
        return {}


def get_all_union(model, model2, user_id):
    data = db.session.query(model, model2).join(model2).filter(model.id == user_id).all()
    if len(data) == 0:
        return {}
    else:
        data = data[0]
        result = data[0].to_dict
        result.update(data[1].to_dict)
        return result


def update_universal(model, user_id, values):
    try:
        data = db.session.query(model).get(user_id)
        data.id = values.get('id')
        data.first_name = values.get('first_name')
        data.last_name = values.get('last_name')

        db.session.commit()

    except Exception:
        return {}


def update_universal_v2(model, user_id, values):
    try:
        db.session.query(model).filter(model.id == user_id).update(values)
        db.session.commit()
    except Exception as e:
        print(e)
        return {}


def delete_universal(model, user_id):
    try:
        db.session.query(model).filter(model.id == user_id).delete(values)
        db.session.commit()
    except Exception as e:
        print(e)
        return {}


def init_db():
    db.drop_all()
    db.create_all()

    with open('data/user.json') as file:
        d = file.read()
        s = d.replace('\'', '\"')
        data = json.loads(s)
        insert_all_users(data)

    with open('data/order.json') as file:
        d = file.read()
        s = d.replace('\'', '\"')
        data = json.loads(s)
        insert_all_orders(data)

    with open('data/offer.json') as file:
        d = file.read()
        s = d.replace('\'', '\"')
        data = json.loads(s)
        insert_all_offers(data)