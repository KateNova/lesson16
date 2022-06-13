from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from utils import get_users, get_orders, get_offers
# import and registration blueprint from package main
from main.views import main_blueprint


app = Flask(__name__)
app.register_blueprint(main_blueprint)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)


# создаем модель пользователь
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    email = db.Column(db.String(100))
    role = db.Column(db.String(100))
    phone = db.Column(db.String(100))


# создаем модель предложение
class Offer(db.Model):
    __tablename__ = 'offer'
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    executor = db.relationship("User")
    order = db.relationship("Order")


# создаем модель заказ
class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(100))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    address = db.Column(db.String(100))
    price = db.Column(db.Integer)
    executor_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    customer_id = db.Column(db.Integer, db.ForeignKey('user.id'))


# создаем все таблицы
db.drop_all()
db.create_all()

# получаем список словарей всех пользователей, предложений, заказов
users = get_users()
offers = get_offers()
orders = get_orders()

# пересобираем список пользователей из списка словарей в список экземпляра класса User
users_list = []
for user in users:
    # распаковываем словарь в аргументы инициализации экземпляра класса User
    users_list.append(User(**user))

orders_list = []
for order in orders:
    orders_list.append(Order(**order))

offers_list = []
for offer in offers:
    offers_list.append(Offer(**offer))

# открываем сессию и добавляем пользователей в базу данных
with db.session.begin():
    db.session.add_all(users_list)

with db.session.begin():
    db.session.add_all(orders_list)

with db.session.begin():
    db.session.add_all(offers_list)

if __name__ == "__main__":
    app.run()
