#!/usr/local/bin/python

from higher_lower_logo import logo
from famous_people import famous_people
import random

#########################################

def comparefollower(instagramer1, instagramer2):
  if famous_people[instagramer1]["followers"] > famous_people[instagramer2]["followers"]:
    return instagramer1,instagramer2, 'a'
  else: 
    return instagramer2,instagramer1, 'b'

def randomNumbers(number1):
  if number1 == -1:
      random_number1 = random.randint(0,len(famous_people)-1)
      random_number2 = random.randint(0,len(famous_people)-1)
      if random_number1 == random_number2:
          random_number2 = random.randint(0,len(famous_people)-1)
      return random_number1, random_number2
  else:
      random_number1 = number1
      random_number2 = random.randint(0,len(famous_people)-1)
      if random_number1 == random_number2:
          random_number2 = random.randint(0,len(famous_people)-1)
      return random_number1, random_number2
      

def checkAnswer(answer, play, score):
    if answer == correct_answer:
        score +=1
        print(f"You're right! Current score: {score}.")
        play = True
        return score,play
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        play = False
        return score, play

#########################################
print(logo)
play = True
score = 0
number = -1
while play == True:
    number1, number2 = randomNumbers(number)
    print(f'Compare A: {famous_people[number1]["name"]}, {famous_people[number1]["activity"]}, from {famous_people[number1]["country"]}')
    print(f'Against B: {famous_people[number2]["name"]}, {famous_people[number2]["activity"]}, from {famous_people[number2]["country"]}')
    user_answer = input('Who has more follower? Type "A" or "B": ').lower()
    big_insta, low_insta, correct_answer = comparefollower(number1,number2)
    score, play = checkAnswer(user_answer,play, score)
    if play == True:
      number = low_insta
    
    


