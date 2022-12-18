#!/usr/local/bin/python

import blackjack_art
import random
import os

##############################
def randomNumber(cards):
    """ function create a random number between 0 and the max number of values in cards_list """
    cards = random.randint(0,len(cards)-1)
    return cards

def addCards(player, position):
    player['cards'].append(card_list[position])

def calcScore(player):
    total_score = 0
    for card in player['cards']:
        total_score += card 
    player['score'] = total_score
    return total_score

def playagain():
    play_again = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    if play_again == 'y' or play_again == 'yes':
        os.system('cls')
        return True

def showScore(total_score1, total_score2, round, dict):
    if total_score1 >= 21 or total_score2 >= 21 :
        print(f'Your final hand:{players_dict["person"]["cards"]} , final score: {total_score1} ')
        print(f"Computer's final hand:{players_dict['computer']['cards']}, final score: {total_score2} ")
        compareScore(dict)
        
    else:
        if round == True :
            print(f'Your cards:{players_dict["person"]["cards"]} , current score: {calcScore(person)} ')
            print(f"Computer's first card:{players_dict['computer']['cards']}, current score: {calcScore(computer)}")
            continue_play = playagain()
            return continue_play

        elif round == False :
            print(f'Your cards:{players_dict["person"]["cards"]} , current score: {calcScore(person)} ')
            print(f"Computer's first card:{players_dict['computer']['cards']}, current score: {calcScore(computer)}")
            continue_play = playagain()
            return continue_play
    

def compareScore(players_dict):
       
    if players_dict["person"]["score"] <= 21:
        print('You WIN! Congratulations!')
    else:
        print("You went over, you lose :'( ") 
     

    

#############################

card_list = [1,2,3,4,5,6,7,8,9,10,10,10,10]
person = {'cards':[], 'score':[]}
computer = {'cards':[], 'score':[]}


wanna_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

if wanna_play == 'y':
    print(blackjack_art.logo)
    players_dict = {'person':person, 'computer':computer}
    
    first_round = True
    if first_round == True: 
        addCards(person, randomNumber(card_list))
        addCards( person, randomNumber(card_list))
        addCards( computer, randomNumber(card_list))
        continue_play = showScore(calcScore(person),calcScore(computer), first_round,players_dict )
        first_round = False
         
               
    
    
    while continue_play == True:
        addCards(person, randomNumber(card_list))
        addCards( computer, randomNumber(card_list))
        continue_play = showScore(calcScore(person),calcScore(computer), first_round,players_dict )
        
        
            

    


    
    
            


    
