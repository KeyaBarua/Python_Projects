import art
print(art.logo)
# A caesar cipher to encode and decode secret messages.
alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Cipher Function
def caesar_cipher(start_message, shift, action):
  end_message = ""
  shifted_position = 0
  # We take the modulus of shift so that if the shift number 
  # exceeds 26 (number of alphabets), we get a number within 26.
  shift %= 26
  for char in start_message:
    # If the character is not an alphabet like a space
    # or a punctuation symbol, we just display it.
    if not char.isalpha():
      end_message += char
    else:
      # If the character is an alphabet
      index = alphabet_list.index(char)
      # encoding message
      if action == "encode":
        shifted_position = index + shift
        # If the shifted position exceeds the length of 
        # the list, we subtract the length of the list 
        # from the shifted position
        if shifted_position >= len(alphabet_list):
          shifted_position -= len(alphabet_list)

      # decoding message
      elif action == "decode":
        shifted_position = index - shift
        # If the shifted position becomes negative, we 
        # add the length of the list 
        # to the shifted position
        if shifted_position < 0:
          shifted_position += len(alphabet_list)

      end_message += alphabet_list[shifted_position]
  print(end_message)



# Ask the user to input
user_input = "yes"
while user_input.lower() == "yes":
  event = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  message = input("Type your message:\n").lower()
  shift_number = int(input("Type the shift number:\n"))
  if event == "encode" or event == "decode":
    caesar_cipher(start_message=message, action=event, shift=shift_number)
  else:
    print("Invalid input!")
  user_input = input("Type 'yes' if you want to go again. Otherwise, type 'no':\n")
  if user_input.lower() == "no":
    print("Goodbye!")
