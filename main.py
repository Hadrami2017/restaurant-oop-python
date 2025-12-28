# main.py
from restaurant.restaurant import Restaurant
from restaurant.table import Table
from restaurant.staff import Waiter, Chef
from restaurant.dishes import Pizza, Burger, Pasta


def main():
    restaurant = Restaurant("Pizza&Burger")

    # Add tables
    restaurant.add_table(Table(1, 2))
    restaurant.add_table(Table(2, 4))

    # Add staff
    waiter = Waiter("Ali")
    chef = Chef("Ahmed")
    restaurant.add_waiter(waiter)
    restaurant.add_chef(chef)

    # Build menu
    restaurant.menu.add_item(Pizza())
    restaurant.menu.add_item(Burger())
    restaurant.menu.add_item(Pasta())

    print("=== MENU ===")
    restaurant.menu.list_items()

    # Find table for 2 people
    table = restaurant.find_free_table(2)
    if table is None:
        print("No free table available!")
        return

    print(f"\nSeating customers at {table}\n")

    # Take order
    order = waiter.take_order(table, ["pizza", "burger"])

    print(f"\nOrder total: ${order.total_price():.2f}\n")

    # Chef prepares order
    chef.prepare_order(order)

    # After serving, give bill and close order
    waiter.give_bill(order)
    order.set_status(order.status.PAID)
    table.current_order = None  # free the table


if __name__ == "__main__":
    main()
