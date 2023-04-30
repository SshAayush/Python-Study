def prime(number,addr):
    for num in range(1,number + 1):
        if number % num == 0:
            addr = addr+1
    if addr == 2:
        print("It's a prime number")
    else:
        print("It's not a prime number")

number = int(input("Enter the number:"))
addr = 0
prime(number,addr)
