# restaurant/order.py
from enum import Enum, auto
from typing import List
from .dishes import Dish
from .table import Table


class OrderStatus(Enum):
    NEW = auto()
    IN_PROGRESS = auto()
    READY = auto()
    SERVED = auto()
    PAID = auto()


class Order:
    def __init__(self, table: Table):
        self.table = table
        self.dishes: List[Dish] = []
        self.status = OrderStatus.NEW
        self._observers = []  # e.g. Waiter instances

    def add_dish(self, dish: Dish):
        self.dishes.append(dish)

    def total_price(self) -> float:
        return sum(d.price for d in self.dishes)

    def register_observer(self, observer):
        self._observers.append(observer)

    def _notify_observers(self):
        for obs in self._observers:
            obs.update(self)

    def set_status(self, new_status: OrderStatus):
        self.status = new_status
        print(f"[Order] Status for table {self.table.number} is now {self.status.name}")
        self._notify_observers()
