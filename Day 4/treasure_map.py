#Using nested list
# import colorsys
import os

clear = lambda:os.system('cls')

option = input("Do you want ot clear the screen:(y/n) ").lower()
if option == 'y':
    clear()

row1 = ["📦","📦","📦"]
row2 = ["📦","📦","📦"]
row3 = ["📦","📦","📦"]
map =[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
co_ordinates = input("Where do you want to place your Treasure'(X,Y)':")
col = int(co_ordinates[0])
row = int(co_ordinates[1])
selected_row = map[row - 1] 
selected_row[col - 1] = "🏴"

print(f"{row1}\n{row2}\n{row3}")


# con_co_ordinates = int(co_ordinates)

# map[splits[0]].insert(con_co_ordinates - 1,"X")

# #del map.[con_co_ordinates]
# row1.insert(con_co_ordinates - 1,"X")
# print(row1)