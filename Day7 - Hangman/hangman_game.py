#!/usr/local/bin/python

import random

hangman_error_list = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_pool = ['water','mouse','house','egg','candle','pencil']

#get a number between 0 and max lenght of word pool
random_number = random.randrange(0,len(word_pool))

#get lenght of word 
word_length = len(word_pool[random_number])



#generate list with empty spaces
guess_list = []
for item in range(word_length):
    guess_list.append('_')

#generate list with word to be guessed
word_list = []
print(f'word:{word_pool[random_number]}')
for letter in word_pool[random_number]:
    word_list.append(letter)

#number of tries, counter of letters tries, flag indicate end of game
errors = 6
count = 0
end_of_game = False

#
while end_of_game == False:
    guess = input('Guess a letter:').lower()
    correct_guess = False
    
    #verify guess, count 
    for letter in word_list:
        if guess == letter:
            correct_guess = True
            count += 1
            position = word_list.index(letter)
            guess_list[position] = letter
            print(f'count:{count}')
            if count == word_length:
                end_of_game = True

           
    if correct_guess == False:
        print(hangman_error_list[errors])
        errors = errors - 1
        if errors < 0:
            end_of_game = True
            print(f'errors:{errors}')
            print(f'end_of_game:{end_of_game}')

                
            
    print(guess_list)
if count != word_length:
    print('SHAME ON YOU, GET OUT HERE!')
else:
    print('WHAT AN AMAZING PERSON YOU ARE!')

    



    
        
    

