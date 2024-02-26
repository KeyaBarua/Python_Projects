import random
import art
EASY_ATTEMPT_LEVEL = 10
DIFFICULTY_ATTEMPT_LEVEL = 5
def get_a_number():
  '''Returns a random number between 1 and 100'''
  return random.randint(1, 100)


def set_attempts(difficulty):
  '''Sets the attempts left according to the difficulty level.'''
  if difficulty == "easy":
    return EASY_ATTEMPT_LEVEL
  else:
    return DIFFICULTY_ATTEMPT_LEVEL
  
    
def compare_numbers(secret, guess):
  '''Compares the secret number and the number guessed by the user.'''
  if guess == secret:
    return 0
  elif guess > secret:
    return 1
  else:
    return -1
    

def play_game(attempts):
  secret_number = get_a_number()
  continue_game = True
  while attempts > 0 and continue_game:
    print(f"You have {attempts} attempts to guess the number.")
    guess = int(input("Make a guess: "))
    if compare_numbers(secret_number, guess) == 0:
      print("You guessed the correct number!")
      continue_game = False
    elif compare_numbers(secret_number, guess) > 0:
      attempts -= 1
      print("Too High! Guess again.")
    else:
      attempts -= 1
      print("Too Low! Guess again.")

    if attempts == 0:
      print(f"You ran out of attempts. The correct number is {secret_number}.")
    



print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty_level  = input("Choose a difficulty level. Type 'easy' or 'hard': ").lower()
secret_number = random.randint(1, 100)
attempts = set_attempts(difficulty_level)
play_game(attempts)
