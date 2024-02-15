import random
import hangman_arts
import hangman_words
from replit import clear

# 1. Displaying the hangman Logo
print(hangman_arts.logo)

# 1. Randomly choose a word from the list and assign it
# to a variable called chosen_word. Create a list of 
# blanks called "display" equal to the same number of 
# letters in the word.
# chosen_word = word_list[random.randint(0, len(word_list) - 1)]
chosen_list = random.choice(hangman_words.word_list)
chosen_word = chosen_list[0]
hint = chosen_list[1]

display = []
for letter in chosen_word:
  display.append("_")

print(f"Hint: {hint}")

# 2. Ask the user to guess a letter and assign it to a 
# variable called guess. Make the guess lowercase. Use a while loop to make the user guess again until the user guesses all the letters. That is, until display does not contain any "_".
# 3. Loop through each position in the chosen word. If 
# the guess matches with a letter, reveal the letter at 
# that position.
#4. Create a variable called lives_gone equal to 0. if the user guesses incorrect letter, increase the lives gone by 1. Display the hangman stages according to lives gone.

end_of_game = False
lives_gone = 0
while not end_of_game:
  guess = input("Guess a letter: ").lower()
  clear()
  
  if guess in display:
    print(f"You've already guessed {guess}.")
  
  for position in range(len(chosen_word)):
    if chosen_word[position] == guess:
      display[position] = chosen_word[position]

  # If the letter is not in the word
  if guess not in chosen_word:
    print(f"You chose {guess}, that's not in the word. You lose a life.")
    print(hangman_arts.hangman_stages[lives_gone])
    lives_gone += 1
    
  # Print the letters
  print(' '.join(display))
  
  # If all lives are gone
  if lives_gone == 7:
    end_of_game = True
    print(f"You Lose! The word was {chosen_word}.")

  # If all blanks are replaced
  if "_" not in display:
    end_of_game = True
    print("You Win!")
    
