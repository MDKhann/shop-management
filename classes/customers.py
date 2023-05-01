class Customer:
    def __init__(self, name, budget, mood=1):
        self.name = name
        self.budget = budget
        self.mood = mood

    def buy_item(self, shop, item_name):
        shop.sell_item(self, item_name)

    def calculate_price(self, item):
        base_price = item.base_value * item.multiplier
        demand_modifier = item.demand * 0.1
        price = base_price * (1 + demand_modifier) * self.mood
        return round(price)

import random

class CustomerController:
    def __init__(self, shop):
        self.shop = shop
        self.customer_names = []
        with open("data/customer_names.txt", "r") as file:
            self.customer_names = file.read().splitlines()

    def generate_customer(self):
        name = random.choice(self.customer_names)
        budget = random.randint(10, 100)
        print(f"Customer {name} enters the shop with a budget of {budget}")
        found_item = False
        for item_name in self.shop.get_item_names():
            item = self.shop.get_item(item_name)
            if random.random() < item.demand / len(self.shop.get_item_names()):
                price = item.base_value * item.multiplier
                if price <= budget:
                    self.shop.sell_item(item_name, price)
                    print(f"Customer {name} bought {item_name} for {price} dollars")
                    found_item = True
                    break
        if not found_item:
            print(f"Customer {name} could not find anything to buy")
