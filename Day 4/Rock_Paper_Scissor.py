# Designing a rock, paper, scissor game
# ASCII art off rock, paper, scissor
# Rock
import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
user_choice = int(
    input(
        "What do you choose? Type 0 for rock, 1 for paper or 2 for scissor:\n")
)

# Computer choice
computer_choice = random.randint(0, 2)
game_images = [rock, paper, scissor]

# If the user typed something other than 0, 1 or 2
if user_choice >= 3 or user_choice < 0:
  print("You typed an invalid number, you lose!")
else:
  # Printing the images
  print(game_images[user_choice])
  print(f"Computer chose:\n {game_images[computer_choice]}")
  
  # User winning case
  if (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
    print("You win!")

  # Computer winning case
  elif (user_choice == 0 and computer_choice == 1) or (user_choice == 1 and computer_choice == 2) or (user_choice == 2 and computer_choice == 0):
    print("You lose!")

  # Draw case
  elif user_choice == computer_choice:
    print("It is a draw!")
    
  
