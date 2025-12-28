# restaurant/staff.py
from .dishes import DishFactory
from .order import Order, OrderStatus
from .table import Table


class Waiter:
    def __init__(self, name: str):
        self.name = name

    def take_order(self, table: Table, dish_types: list[str]) -> Order:
        print(f"[{self.name}] Taking order from {table}")
        order = Order(table)
        for dt in dish_types:
            dish = DishFactory.create_dish(dt)
            order.add_dish(dish)
            print(f"[{self.name}] Added {dish} to order for table {table.number}")
        table.current_order = order
        order.register_observer(self)
        return order

    def serve_order(self, order: Order):
        print(f"[{self.name}] Serving order to {order.table}")
        order.set_status(OrderStatus.SERVED)

    def give_bill(self, order: Order):
        total = order.total_price()
        print(f"[{self.name}] The total bill for table {order.table.number} is ${total:.2f}")

    # Observer callback
    def update(self, order: Order):
        if order.status == OrderStatus.READY:
            print(f"[{self.name}] Notified: Order for table {order.table.number} is READY. Going to serve...")
            self.serve_order(order)


class Chef:
    def __init__(self, name: str):
        self.name = name

    def prepare_order(self, order: Order):
        print(f"[{self.name}] Started preparing order for table {order.table.number}...")
        order.set_status(OrderStatus.IN_PROGRESS)

        # Here you could simulate time / complexity
        print(f"[{self.name}] Finished preparing order with {len(order.dishes)} dishes.")
        order.set_status(OrderStatus.READY)
