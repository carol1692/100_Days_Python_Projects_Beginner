#!/usr/local/bin/python

import os
from auction_art import logo


print(logo)
print('Welcome to the secret auction program.')

new_bid = True
bid_dict = {}
mount_dict = {}
while new_bid != False:
    
    name = input('What is your name? ')
    bid = input("What's your bid? ")
    bid_dict[name]=int(bid)
    add_bid = input("Are there any other bidders? Type 'yes' or 'no' ").lower()
    
    if add_bid == 'no' or add_bid == 'n':
        new_bid = False
        os.system('cls')
        key_max_bid = max(bid_dict, key=bid_dict.get)
        big_bid = max(bid_dict.values())
        print(f'The winner is {key_max_bid} with a bid of ${big_bid}')
        
    else:    
        os.system('cls')
        

