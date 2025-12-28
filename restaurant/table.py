# restaurant/table.py


class Table:
    def __init__(self, number: int, capacity: int):
        self.number = number
        self.capacity = capacity
        self.current_order = None  # will point to an Order

    def __str__(self) -> str:
        return f"Table {self.number} (capacity: {self.capacity})"
