import random
cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
card_points = {
  'A': 11, '2': 2, '3':3, '4':4, '5': 5, 
  '6': 6, '7': 7, '8': 8, '9': 9, '10' : 10, 
  'J' : 10, 'Q': 10, 'K' : 10}

def deal_cards(n):
  user_card_list = []
  for number in range(0, n):
    dealed_card = random.choice(cards)
    if n == 1:
      return dealed_card
    else:
      user_card_list.append(dealed_card)
  return user_card_list

def calc_points(card_list):
  total_point = 0
  for card in card_list:
    total_point += card_points[card]
  return total_point
  
def playBlackJack():
  # User cards
  user_cards = deal_cards(2)
  user_score = calc_points(user_cards)
  print(f"Your cards: {user_cards}, current score: {user_score}")

  # Computer's card
  computer_card = deal_cards(2)
  computer_score = calc_points(computer_card)
  print(f"Computer's first card: {computer_card[0]}")

  hit = input("Type 'y' to get another card, type 'n' to pass: ").lower()
  if hit == 'y':
    third_card = deal_cards(1)
    user_cards.append(third_card)
    user_score += calc_points(third_card)
  print(f"Your final hand: {user_cards}, final score: {user_score}")

  
  computer_hit = random.choice(['y', 'n'])
  
  if computer_hit == 'y' and computer_score < 21:
    computer_card.append(deal_cards(1))
    computer_score += calc_points(computer_card)
  print(f"Computer's final hand: {computer_card}, final score: {computer_score}")



    
    





play_game = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")
if play_game.lower() == 'y':
  playBlackJack()
elif play_game.lower() == 'n':
  print("Goodbye!")
else:
  print("Invalid input. Goodbye!")
