import Order
import uuid


class OrderRepository:

    def __init__(self):
        self.Orders = list()

    def add(self, order: Order):
        self.Orders.append(order)

    def get(self, order_id: uuid):
        for order_item in self.Orders:
            if order_item.id == order_id:
                return order_item
        return None

    def list_orders(self, n_latest:int = None):
        if n_latest is not None:
            for index in range(n_latest, len(self.Orders)):
                print(self.Orders[index])
        else:
            for index in range(1, len(self.Orders)):
                print(self.Orders[index])

    def delete(self, order_id: uuid):
        deleting_order = self.get(self, order_id)
        self.Orders.remove(deleting_order)


