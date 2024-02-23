cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
card_points = {
  'A': 11, '2': 2, '3':3, '4':4, '5': 5, 
  '6': 6, '7': 7, '8': 8, '9': 9, '10' : 10, 
  'J' : 10, 'Q': 10, 'K' : 10}

def deal_cards():
  """Returns a random card from the deck"""
  return random.choice(cards)
  

def calc_points(card_list):
  """Calculates the points based on the cards""" 
  total_points = 0
  for card in card_list:
    total_points += card_points[card]
  # BlackJack condition
  if total_points == 21 and len(card_list) == 2:
    return 0
  # Changing the ACE score to 1 if the total score exceeds 21
  if 'A' in card_list and total_points > 21:
    return total_points - 10
  return total_points

def playBlackJack():
  """Starts the BlackJack game"""
  print(logo)
  user_cards = []
  computer_cards = []
  is_game_over = False
  for _ in range(2):
    user_cards.append(deal_cards())
    computer_cards.append(deal_cards())

  # User's game
  while not is_game_over:
    user_score = calc_points(user_cards)
    computer_score = calc_points(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      while not user_score > 21:
        deal_another = input("\nType 'y' to get another card, type 'n' to quit: ")
        if deal_another.lower() == 'y':
          user_cards.append(deal_cards())
          user_score = calc_points(user_cards)
          print(f"Your cards: {user_cards}, current score: {user_score}")
        else:
          is_game_over = True
          break
      break

  print(f"\n\nYour final hand: {user_cards}, current score: {user_score}")
  print(f"Computer's final hand: {computer_cards}, computer's score: {computer_score}\n\n")

  print(compare_score(user_score, computer_score))

# Start
while input("Do you want to play a game of BlackJack? Type 'y' or 'n': ").lower() == 'y':
    clear()
    playBlackJack()
