from OrderRepository import OrderRepository
from Good import Good
from Order import Order
import uuid
from datetime import datetime


def create_good(name: str = None, price: float = None):
    added_good: Good = Good()
    uuid1 = uuid.uuid4()
    added_good.id = uuid1
    added_good.name = name
    added_good.price = price
    return added_good


def create_order(client_id: uuid, list_goods):
    added_order: Order = Order(list_goods)
    added_order.id = uuid.uuid4()
    added_order.order_date = datetime.now()
    added_order.client_id = client_id
    return added_order


order_repository = OrderRepository()

good_1 = create_good("good1", 1.0)
good_2 = create_good("good_2", 2.0)
good_3 = create_good("good_3", 1.0)
good_4 = create_good("good_4", 2.0)

goods = [good_1, good_2, good_3, good_4]
order_1 = create_order(uuid.uuid4(), goods)
order_2 = create_order(uuid.uuid4(), goods)

order_repository.add(order_1)
order_repository.add(order_2)
order_repository.list_orders(1)
order_repository.list_orders()
order = order_repository.get(order_1.id)
order_repository.delete(order.id)


