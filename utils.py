import json
from datetime import datetime as dt


def get_users():
    """
    :return: список словарей с данными пользователей
    """
    with open("users.json", "r", encoding="utf-8") as f:
        users = json.load(f)
    return users


def get_orders():
    """
    :return: список словарей с заказами
    """
    with open("orders.json", "r", encoding="utf-8") as f:
        orders = json.load(f)
    # преобразование формата даты
    for order in orders:
        order['start_date'] = dt.strptime(order['start_date'], '%m/%d/%Y')
        order['end_date'] = dt.strptime(order['end_date'], '%m/%d/%Y')
    return orders


def get_offers():
    """
        :return: список словарей с предложениями
    """
    with open("offers.json", "r", encoding="utf-8") as f:
        offers = json.load(f)
    return offers


def object_to_dict(obj):
    # приведение экземпляров клсса User к списку словарей при помощи метода __dict__
    new_dict = obj.__dict__
    # удаление значения ключа, появившегося в результате выполнения метода __dict__
    new_dict.pop('_sa_instance_state')
    return new_dict
