print('''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|

''')
print("Welcome to the Treasure Island.🏴‍☠️")
print("Your mission is to find the treasure.")
choice1 = input(
    "You're at a crossroad ⚔️, where do you want to go? Type \"left\" or \"right\" >>\n").lower()

if choice1 == "left":
  # Continue in the game.
  choice2 = input("Now you've come to a lake 🤽. There is an island 🏝️ in the middle of the lake. Type \"wait\" if you want to wait for a boat ⛵ or \"swim\" if you want to swim >>\n").lower()
  if choice2 == "wait":
    choice3 = input("You've arrived at the island unharmed. You see three doors 🚪 of red, yellow and blue color. Which door do you want to open? Type \"blue\" or \"red\" or \"yellow\" >>\n").lower()
    if choice3 == "red":
      print("You enter a room full of fire 🔥. Game over!")
    elif choice3 == "yellow":
      print("You found the treasure 🪙. Congratulations. You win!")
    elif choice3 == "blue":
      print("You enter a room of beasts 🦁. Game over!")
    else:
      print("You chose a door that doesn't exist. Game over!")
  else:
    print("Oh no! You got attacked by a hungry crocodile 🐊. Game over!")
else:
  print("Oops! You fell into a hole 🕳️. Game over!")
