import csv
class Product:
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

    @staticmethod
    def is_integer():
        #Tjis should be used when something have relationship with class, 
        # but not something that must be unique per instance
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    @classmethod
    def instance_from_csv(cls):
        #this should do something that have the relationship with the class , 
        # But usually these are used to manipulate different 
        #structure of data to instance onjects, like we have done eith csv.

        with open('product.csv', 'r') as file:
            reader = csv.DictReader(file)
            items = list(reader)

            for item in items:
                Product(
                    name = item.get('name'),
                    price = int(item.get('price')),
                    quantity = int(item.get('quantity')),
                )
                
    def __repr__(self):
        return f"Item: ('{self.name}', {self.price}, {self.quantity})"

Product.instance_from_csv()
print(Product.all)