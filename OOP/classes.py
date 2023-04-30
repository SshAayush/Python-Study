# class Product:
#     def calculate_total_price(self, x, y):
#         return x * y


# samsung = Product()

# samsung.price = 500
# samsung.quantity = 10

# print(
#     f"Total price of Samsung: {samsung.calculate_total_price(samsung.price, samsung.quantity)}"
# )

# apple = Product()

# apple.price = 600
# apple.quantity = 5

# print(
#     f"Total price of apple: {apple.calculate_total_price(apple.price,apple.quantity)}"
# )


class Product:
    pay_rate = (
        0.8  # it is known as class attribute  which can be accessed by any objects
    )

    def __init__(self, name: str, price: float, quantity=0):
        assert price >= 0, f"Price should be greater than 0: {price}"
        assert quantity >= 0, f"Quantity should be greater than 0: {quantity}"

        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity


samsung = Product("samsung", 500, 10)

apple = Product("apple", 600, 3)

print(samsung.calculate_total_price())
print(apple.calculate_total_price())
