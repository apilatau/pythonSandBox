import Good
import uuid
from datetime import datetime


class Order:

    def __init__(self, goods: []):
        self.Goods = goods

    @property
    def id(self):
        return self.id

    @property
    def order_date(self):
        return self.order_date

    @property
    def client_id(self):
        return self.client_id

    @property
    def goods(self):
        return self.Goods

    @property
    def price(self):
        list_price = list()
        for item in self.Goods:
            list_price.append(item.price)
        return sum(list_price)

    @id.setter
    def id(self, value: uuid):
        self.id = value

    @order_date.setter
    def order_date(self, value: datetime):
        self.order_date = value

    @client_id.setter
    def client_id(self, value: uuid):
        self.client_id = value
