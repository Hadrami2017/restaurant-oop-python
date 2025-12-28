# restaurant/menu.py
from typing import List
from .dishes import Dish


class Menu:
    def __init__(self):
        self._items: List[Dish] = []

    def add_item(self, dish: Dish):
        self._items.append(dish)

    def list_items(self):
        for idx, dish in enumerate(self._items, start=1):
            print(f"{idx}. {dish}")

    def get_item(self, index: int) -> Dish:
        return self._items[index]
