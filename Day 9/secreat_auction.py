import os
from turtle import update
clear = lambda: os.system('cls')
from art import logo

print(logo)
auction_dic = {}
bid_name = ""
amt = 0
end = False
while not end:
    name = input("What's your name: ")
    amount = input("What's your bid amount? : $")
    auction_dic.update({name : amount})
    check = input("Is there any other bid 'yes/no'? :")
    clear()
    if check == "no":
        end = True
    bid_name = max(auction_dic, key = auction_dic.get)
    amt = auction_dic[bid_name]
    
    
print(f"The higest bidder is {bid_name} with ${amt}.")