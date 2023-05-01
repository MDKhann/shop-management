from classes import shop
from classes import item
from classes import customers

my_shop = shop.Shop("Pawn shop", 1000)

item1 = item.Item("Apples", 2.0, 0.6, 1.2, 500)
item2 = item.Item("Bananas", 1.5, 0.8, 1.5, 500)
item3 = item.Item("Oranges", 2.5, 0.4, 1.3, 500)
items = [item1, item2, item3]

for item in items:
    my_shop.add_item(item)

customer_controller = customers.CustomerController(my_shop)

for i in range(100):
    customer = customer_controller.generate_customer()

my_shop.display_statistics()