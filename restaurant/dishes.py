# restaurant/dishes.py
from abc import ABC, abstractmethod


class Dish(ABC):
    def __init__(self, name: str, price: float, prep_time: int):
        self.name = name
        self.price = price
        self.prep_time = prep_time

    @abstractmethod
    def __str__(self) -> str:
        pass


class Pizza(Dish):
    def __init__(self):
        super().__init__("Pizza Margherita", 12.5, 15)

    def __str__(self) -> str:
        return f"{self.name} (${self.price})"


class Burger(Dish):
    def __init__(self):
        super().__init__("Beef Burger", 10.0, 10)

    def __str__(self) -> str:
        return f"{self.name} (${self.price})"


class Pasta(Dish):
    def __init__(self):
        super().__init__("Carbonara Pasta", 13.0, 12)

    def __str__(self) -> str:
        return f"{self.name} (${self.price})"


class DishFactory:
    """Factory to create dishes by type string."""

    @staticmethod
    def create_dish(dish_type: str) -> Dish:
        dish_type = dish_type.lower()
        if dish_type == "pizza":
            return Pizza()
        elif dish_type == "burger":
            return Burger()
        elif dish_type == "pasta":
            return Pasta()
        else:
            raise ValueError(f"Unknown dish type: {dish_type}")
