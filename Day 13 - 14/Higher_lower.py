import data
import random
import art
from replit import clear
def generate_random_account():
  '''Generate a random choice from the list of dictionaries.'''
  return random.choice(data.data)

def display_info(data):
  '''Format string for displaying the comparison accounts.'''
  return f"{data['name']}, a(n) {data['work']}, from {data['country']}."

def compare_data(data1, data2):
  '''Compares the number of followers of two different accounts.'''
  if data1 > data2:
    return 'A'
  elif data1 < data2:
    return 'B'

def start_game():
  '''Starts the Higher Lower game'''
  correct_answer = True
  current_score = 0
  first_data = generate_random_account()
  while correct_answer:
    second_data = generate_random_account()
    # If the second data is same as the first, second data is 
    # generated again.
    while first_data == second_data:
      second_data = generate_random_account()

    # Printing the data
    print("Compare A: " + display_info(first_data))
    print(art.against)
    print("Against B: " + display_info(second_data))
    
    user_input = input("Who has more followers? Type 'A' or 'B': ")
    higher_data = compare_data(first_data['followers'], second_data['followers'])
    # Swapping the data
    first_data = second_data
    clear()
    print(art.logo)

    # Comparing the user input with account with the higher 
    # number of followers.
    if user_input.upper() == higher_data:
      current_score += 1
      print(f"You're right. Current score: {current_score}")
    else:
      print(f"Sorry that's wrong. Current score: {current_score}")
      correct_answer = False


print(art.logo)
start_game()
