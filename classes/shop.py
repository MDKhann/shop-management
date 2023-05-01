class Shop:
    def __init__(self, name, balance, inventory=None):
        if inventory is None:
            inventory = {}

        self.name = name
        self.balance = balance
        self.inventory = inventory

    def add_item(self, item):
        if item.name in self.inventory:
            self.inventory[item.name].quantity += item.quantity
        else:
            self.inventory[item.name] = item

    def sell_item(self, customer, item_name):
        if item_name in self.inventory and customer.budget >= customer.calculate_price(self.inventory[item_name]):
            item = self.inventory[item_name]
            price = customer.calculate_price(item)
            customer.budget -= price
            self.balance += price
            item.quantity -= 1
            if item.quantity == 0:
                del self.inventory[item_name]

    def restock(self, item_name, quantity):
        if item_name in self.inventory:
            self.inventory[item_name].quantity += quantity
        else:
            print(f"{item_name} is not sold by {self.name}.")

    def get_inventory(self):
        return self.inventory

    def get_item_names(self):
        return [item.name for item in self.inventory.values()]

    def get_item(self, item_name):
        if item_name in self.inventory:
            return self.inventory[item_name]
        else:
            return None

    def calculate_revenue(self):
        revenue = sum([item.base_value * item.demand * item.multiplier * (item.quantity - 1) for item in self.inventory.values() if item.quantity > 0])
        return revenue

    def calculate_profit(self):
        profit = self.calculate_revenue() - sum([item.base_value * item.quantity for item in self.inventory.values()])
        return profit

    def __str__(self):
        inventory = [f"{item.name} ({item.quantity})" for item in self.inventory.values() if item.quantity > 0]
        inventory_str = "\n".join(inventory) if inventory else "No items in inventory"
        return f"{self.name}\nBalance: {self.balance}\nInventory:\n{inventory_str}"
    def display_statistics(self):
        total_items = len(self.inventory)
        total_quantity = sum([item.quantity for item in self.inventory.values()])
        total_value = sum([item.base_value * item.quantity for item in self.inventory.values()])
        revenue = self.calculate_revenue()
        profit = self.calculate_profit()

        print(f"Number of items: {total_items}")
        print(f"Total quantity: {total_quantity}")
        print(f"Total value: {total_value}")
        print(f"Total revenue: {revenue}")
        print(f"Profit: {profit}")

