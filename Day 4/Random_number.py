import rand_num_generator


num=input("Enter Random Number:")
print(num)
converted_num = int(num)
print(rand_num_generator.rand_num)
print(type(rand_num_generator.rand_num))
if(converted_num == rand_num_generator.rand_num):
    print("Congratulation the number you entered matched.")
else:
    print("Sorry!! Didn't matched.")

print(rand_num_generator.rand_float)