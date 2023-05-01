class Product:
    pay_rate = 0.8

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_amount(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate


samsung = Product("Samsung", 500, 20)
apple = Product("Apple", 600, 5)
lg = Product("LG", 300, 15)
dell = Product("Dell", 450, 10)
hp = Product("HP", 350, 8)
