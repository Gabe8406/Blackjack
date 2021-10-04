import os
clear = lambda: os.system('clear')
import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
                   

                                      
     


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
want_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n':\n").lower()
cards_player = []
cards_dealer = []

def score_table():
  if 11 in cards_player and sum(cards_player) > 21:
    print(f"Your cards:{cards_player}, current score: {sum(cards_player) - (cards_player.count(11))*10} \n Computer's first card: {cards_dealer[0]}")
  else:
    print(f"Your cards:{cards_player}, current score: {sum(cards_player)} \n Computer's first card: {cards_dealer[0]}")

def another_card():
  return input("Type 'y' to get another card, type 'n' to pass:\n").lower()

def append(who):
  if who == "player": 
    cards_player.append(random.choice(cards))
  elif who == "dealer":
    cards_dealer.append(random.choice(cards))
        
def want_other():
  
  while sum(cards_player) < 21 and another_card() == "y":
    append("player")
    score_table()
  if sum(cards_player) > 21:
    while sum(cards_dealer) < 11:
      append("dealer")
    print(f"Your final hand: {cards_player}, final score: {sum(cards_player)} \n Computer's final hand: {cards_dealer}, final score: {sum(cards_dealer)} \n YOU WENT OVER. YOU LOSE.")
    next_round()
  else:
    final_score()

def next_round():
  if input("Do you want to play a game of Blackjack? Type 'y' or 'n':\n").lower() == "y":
    cards_player.clear()
    cards_dealer.clear()
    clear()
    game()

def final_score():
  while sum(cards_dealer) < 17:
    append("dealer")
  while sum(cards_dealer) > 21 and 11 in cards_dealer:
    cards_dealer.remove(11)
    cards_dealer.append(1)
  if sum(cards_dealer) == sum(cards_player):
    print(f"Your final hand: {cards_player}, final score: {sum(cards_player)} \n Computer's final hand: {cards_dealer}, final score: {sum(cards_dealer)} \n It is a draw. ") 
    next_round()
  elif sum(cards_dealer) == 21:
    print(f"Your final hand: {cards_player}, final score: {sum(cards_player)} \n Computer's final hand: {cards_dealer}, final score: {sum(cards_dealer)} \n THE COMPUTER GOT A BLACKJACK. YOU LOST")        
    next_round()
  elif sum(cards_player) == 21 and sum(cards_dealer) != 21:
    print(f"Your final hand: {cards_player}, final score: {sum(cards_player)} \n Computer's final hand: {cards_dealer}, final score: {sum(cards_dealer)} \n BLACJACK! YOU WON.")
    next_round()
  elif sum(cards_dealer) > 21:
    print(f"Your final hand: {cards_player}, final score: {sum(cards_player)} \n Computer's final hand: {cards_dealer}, final score: {sum(cards_dealer)} \n THE COMPUTER WENT OVER. YOU WON")
    next_round()
  elif sum(cards_dealer) > sum(cards_player):
    print(f"Your final hand: {cards_player}, final score: {sum(cards_player)} \n Computer's final hand: {cards_dealer}, final score: {sum(cards_dealer)} \n YOU LOSE.")
    next_round()
  elif sum(cards_dealer) < sum(cards_player):
    print(f"Your final hand: {cards_player}, final score: {sum(cards_player)}\n Computer's final hand: {cards_dealer}, final score: {sum(cards_dealer)} \n YOU WON.")
    next_round()
  
def game():   
  print(logo)
  if want_play == "y":
    append("player")
    append("player")
    append("dealer")
    score_table()
    want_other()
    while sum(cards_player) > 21 and 11 in cards_player:
        cards_player.remove(11)
        cards_player.append(1)
        want_other()
  else:
    print("")

game()






