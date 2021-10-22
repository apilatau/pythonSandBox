import Order
import uuid


class OrderRepository:

    def __init__(self):
        self.__Orders = list()

    def add(self, order: Order):
        self.__Orders.append(order)

    def get(self, order_id: uuid):
        for order_item in self.__Orders:
            if order_item.id == order_id:
                return order_item
        return None

    def list_orders(self, n_latest:int = None):        
        list_for = list(self.__Orders)
        if n_latest is not None:
            last_index = len(list_for)
            for item in list_for[last_index-n_latest: last_index]:
                print(f"OrderId:{item.id} Order_date:{item.order_date} Order client_id:{item.client_id} Order.price:{item.price}")
        else:
            for item in list_for:
                print(f"OrderId:{item.id} Order_date:{item.order_date} Order client_id:{item.client_id} Order.price:{item.price}")

    def delete(self, order_id: uuid):
        deleting_order = self.get(order_id)
        self.__Orders.remove(deleting_order)


