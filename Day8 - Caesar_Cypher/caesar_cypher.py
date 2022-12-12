#!/usr/local/bin/python

import string
from cypher_art import logo

################################################
def cypher(plain_text, shift_amount):
    cipher_text = ""
    if shift_amount > 26:
        shift_amount = shift % 26
        print(f'new shift:{shift}')
    for char in plain_text:
        #if char == ' ' or char.isnumeric():
        if char in alphabet:
            position = alphabet.index(char)
            if menu_options == 'encode':
                new_position = position + shift_amount
            else:
                new_position = position - shift_amount
            new_char = alphabet[new_position]
            cipher_text += new_char
            
        else:
            cipher_text += char
    print(f"The {menu_options} text is: {cipher_text}")
    
################################################################################

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)
continue_run = True
while continue_run:

    menu_options = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    cypher(plain_text=text, shift_amount=shift)
    run_again = input('Do you want go again? Y/N: ').lower()
    if run_again == 'no' or run_again == 'n' :
        continue_run = False
        print('So long, and thanks for all the fish.')
