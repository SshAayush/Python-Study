import csv

class Product:
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity: int):
        # Run validation to receive arguments
        assert price >= 0, f"Price should be greater than 0: {price}"
        assert quantity >= 0, f"Quantity should be greater than 0: {quantity}"

        # Assign value to object
        self.name = name
        self.price = price
        self.quantity = quantity

        # storig all the created objcet/instance in array
        Product.all.append(self)

    def calculate_total_amount(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instance_from_csv(cls):
        with open('product.csv', 'r') as file:
            reader = csv.DictReader(file)
            items = list(reader)

            for item in items:
                Product(
                    name = item.get('name'),
                    price = float(item.get('price')),
                    quantity = int(item.get('quantity')),
                )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item: ('{self.name}', {self.price}, {self.quantity})"



print(Product.is_integer(5.0))
# Product.instance_from_csv()
# print(Product.all)


# samsung = Product("Samsung", 500, 20)
# apple = Product("Apple", 600, 5)
# lg = Product("LG", 300, 15)
# dell = Product("Dell", 450, 10)
# hp = Product("HP", 350, 8)

# # for instance in Product.all:
# #     print(instance.name)
