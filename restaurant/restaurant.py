# restaurant/restaurant.py
from typing import List, Optional
from .menu import Menu
from .table import Table
from .staff import Waiter, Chef


class Restaurant:
    def __init__(self, name: str):
        self.name = name
        self.menu = Menu()
        self.tables: List[Table] = []
        self.waiters: List[Waiter] = []
        self.chefs: List[Chef] = []

    def add_table(self, table: Table):
        self.tables.append(table)

    def add_waiter(self, waiter: Waiter):
        self.waiters.append(waiter)

    def add_chef(self, chef: Chef):
        self.chefs.append(chef)

    def find_free_table(self, people: int) -> Optional[Table]:
        for table in self.tables:
            if table.current_order is None and table.capacity >= people:
                return table
        return None
