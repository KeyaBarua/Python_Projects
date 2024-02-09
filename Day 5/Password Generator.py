import random
print("Welcome to the PyPassword Generator!")
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '^']

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Easy Level
# Password comes in serial. First letters, then numbers and then symbols. ASB12*+
password = ""
# Looping through the letters
# for char in range(1, nr_letters + 1):
#   letter = letters[random.randint(0, len(letters)-1)]
#   password += letter
  
#Looping through the numbers
# for char in range(1, nr_numbers + 1):
#   number = numbers[random.randint(0, len(numbers) - 1)]
#   password += number

# Looping through the symbols
# for char in range(1, nr_symbols + 1):
#   symbol = symbols[random.randint(0, len(symbols) - 1)]
#   password +=symbol
# print(password)


# Hard Level
# Password comes in a random order 1A8b*45+^Jk
character = []
for char in range(1, nr_letters + 1):
  character.append(random.choice(letters))
for char in range(1, nr_numbers + 1):
  character.append(random.choice(numbers))
for char in range(1, nr_symbols + 1):
  character.append(random.choice(symbols))
# print(character)

# Reordering the list
random.shuffle(character)

for char in character:
  password += char
print(f"Your password is {password}")
