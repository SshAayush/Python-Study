import random

name = input("Enter the name of users sepreated by comma:")
names = name.split(",")
size_name = len(names)
# random_name = random.randint(0,size_name-1)
random_name = (random.choice(names))

# print(f"{names[random_name]} is going to pay the bill.")

print(random_name+" will pay the bill")