#parameter = name of the data (name)
#argument = actual value of the data (u_name)  

def prnt(name,location):
    print(f"Hemlo {name} you live in {location}")
    print(f"Hiii {name} you live in {location}")
    print(f"Whats up?? {name} you live in {location}")

#using positional argument
u_name = input("Write your name:")
u_location = input("Where do you live in:")
prnt(u_name,u_location)


#using keyword argument
prnt(location = u_location, name = u_name)
