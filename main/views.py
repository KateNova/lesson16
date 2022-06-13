from flask import Blueprint, jsonify, request
from utils import object_to_dict
from datetime import datetime as dt

main_blueprint = Blueprint("main_blueprint", __name__)


@main_blueprint.route("/users/", methods=['GET'])
def get_all_users():
    from app import User
    users = User.query.all()
    users_list = []
    # создание json списка
    for user in users:
        users_list.append(object_to_dict(user))
    return jsonify(users_list)


@main_blueprint.route("/users/<int:xid>", methods=['GET'])
def get_user_by_id(xid):
    from app import User
    user = User.query.get(xid)
    return jsonify(object_to_dict(user))


@main_blueprint.route("/users/", methods=['POST'])
def create_user():
    from app import User, db
    # добавляем пользователя в базу данных
    try:
        with db.session.begin():
            # распаковываем значения из словаря в аргументы экземпляра класса User
            db.session.add(User(**request.json))
        return jsonify({"content": "Создали пользователя"})
    except:
        return jsonify({"content": "Что-то пошло не так"})


@main_blueprint.route("/users/<int:xid>", methods=['PUT'])
def update_user(xid):
    from app import User, db
    # запрос на пользователя по id
    try:
        with db.session.begin():
            user = User.query.get(xid)
            for k, v in request.json.items():
                setattr(user, k, v)
            db.session.add(user)
        return jsonify({"content": "Обновили пользователя"})
    except:
        return jsonify({"content": "Что-то пошло не так"})


@main_blueprint.route("/users/<int:xid>", methods=['DELETE'])
def delete_user(xid):
    from app import User, db
    # запрос на пользователя по id
    try:
        with db.session.begin():
            user = User.query.get(xid)
            db.session.delete(user)
        return jsonify({"content": "Удалили пользователя"})
    except:
        return jsonify({"content": "Что-то пошло не так"})


@main_blueprint.route("/orders/", methods=['GET'])
def get_all_orders():
    from app import Order
    orders = Order.query.all()
    orders_list = []
    # создание json списка
    for order in orders:
        orders_list.append(object_to_dict(order))
    return jsonify(orders_list)


@main_blueprint.route("/orders/<int:xid>", methods=['GET'])
def get_order_by_id(xid):
    from app import Order
    order = Order.query.get(xid)
    return jsonify(object_to_dict(order))


@main_blueprint.route("/orders/", methods=['POST'])
def create_order():
    from app import Order, db
    # добавляем заказ в базу данных
    try:
        with db.session.begin():
            # получаем данные из запроса
            order = request.json
            # приводим строковую запись даты к типу datetime.date
            order['start_date'] = dt.strptime(order['start_date'], '%m/%d/%Y')
            order['end_date'] = dt.strptime(order['end_date'], '%m/%d/%Y')
            # распаковываем значения из словаря в аргументы экземпляра класса Order
            db.session.add(Order(**order))
        return jsonify({"content": "Создали заказ"})
    except:
        return jsonify({"content": "Что-то пошло не так"})


@main_blueprint.route("/orders/<int:xid>", methods=['PUT'])
def update_order(xid):
    from app import Order, db
    # запрос на заказ по id
    try:
        with db.session.begin():
            # получаем данные из запроса
            order_dict = request.json
            # приводим строковую запись даты к типу datetime.date
            order_dict['start_date'] = dt.strptime(order_dict['start_date'], '%m/%d/%Y')
            order_dict['end_date'] = dt.strptime(order_dict['end_date'], '%m/%d/%Y')
            # делаем запрос на заказ по id
            order = Order.query.get(xid)
            # запускаем цикл по словарю = одному заказу
            for k, v in order_dict.items():
                # вызываем функцию, которая устанавливает значение одноименного с ключем атрибута
                setattr(order, k, v)
            db.session.add(order)
        return jsonify({"content": "Обновили заказ"})
    except:
        return jsonify({"content": "Что-то пошло не так"})


@main_blueprint.route("/orders/<int:xid>", methods=['DELETE'])
def delete_order(xid):
    from app import Order, db
    # запрос на заказ по id
    try:
        with db.session.begin():
            order = Order.query.get(xid)
            db.session.delete(order)
        return jsonify({"content": "Удалили заказ"})
    except:
        return jsonify({"content": "Что-то пошло не так"})


@main_blueprint.route("/offers/", methods=['GET'])
def get_all_offers():
    from app import Offer
    offers = Offer.query.all()
    offers_list = []
    # создание json списка
    for offer in offers:
        offers_list.append(object_to_dict(offer))
    return jsonify(offers_list)


@main_blueprint.route("/offers/<int:xid>", methods=['GET'])
def get_offer_by_id(xid):
    from app import Offer
    offer = Offer.query.get(xid)
    return jsonify(object_to_dict(offer))


@main_blueprint.route("/offers/", methods=['POST'])
def create_offer():
    from app import Offer, db
    # добавляем предложение в базу данных
    try:
        with db.session.begin():
            # распаковываем значения из словаря в аргументы экземпляра класса Offer
            db.session.add(Offer(**request.json))
        return jsonify({"content": "Создали предложение"})
    except:
        return jsonify({"content": "Что-то пошло не так"})


@main_blueprint.route("/offers/<int:xid>", methods=['PUT'])
def update_offer(xid):
    from app import Offer, db
    # запрос на предлоежние по id
    try:
        with db.session.begin():
            offer = Offer.query.get(xid)
            for k, v in request.json.items():
                setattr(offer, k, v)
            db.session.add(offer)
        return jsonify({"content": "Обновили предложение"})
    except:
        return jsonify({"content": "Что-то пошло не так"})


@main_blueprint.route("/offers/<int:xid>", methods=['DELETE'])
def delete_offer(xid):
    from app import Offer, db
    # запрос на предложение по id
    try:
        with db.session.begin():
            offer = Offer.query.get(xid)
            db.session.delete(offer)
        return jsonify({"content": "Удалили предложение"})
    except:
        return jsonify({"content": "Что-то пошло не так"})
