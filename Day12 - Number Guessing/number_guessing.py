#!/usr/local/bin/python
import random

print('''
   ___                                              _      _                                                _                      
  / __|   _  _     ___     ___     ___      o O O  | |_   | |_      ___      o O O  _ _     _  _    _ __   | |__     ___      _ _  
 | (_ |  | +| |   / -_)   (_-<    (_-<     o       |  _|  | ' \    / -_)    o      | ' \   | +| |  | '  \  | '_ \   / -_)    | '_| 
  \___|   \_,_|   \___|   /__/_   /__/_   TS__[O]  _\__|  |_||_|   \___|   TS__[O] |_||_|   \_,_|  |_|_|_| |_.__/   \___|   _|_|_  
_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| {======|_|"""""|_|"""""|_|"""""| {======|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| 
"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'./o--000'"`-0-0-'"`-0-0-'"`-0-0-'./o--000'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-' 
''')

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == 'easy':
    attempts = 10
    print('You have 10 attempts remaining to guess the number')
else:
    attempts = 5
    print('You have 5 attempts remaining to guess the number')

random_number = random.randint(0,100)
print(f'the number is:{random_number}')

count = 0
while count < attempts:
    guess = int(input('Make a guess: '))
    if guess > random_number:
        print('Too high')
        count +=1
        print(f"You have {attempts-count} attempts remaining to guess the number.")
    elif guess < random_number:
        print('Too Low')
        count +=1
        print(f"You have {attempts-count} attempts remaining to guess the number.")
    else:
        print(f"Congratulations you guessed the number!")
        count = attempts
   


