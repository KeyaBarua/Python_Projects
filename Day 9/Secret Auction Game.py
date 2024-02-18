from art import logo
from replit import clear
print(logo)
print("Welcome to the Secret Auction Program")
bidder_dict = {}

# Function to add the new bidder to the dictionary
def add_new_bidder(name, price):
  bidder_dict[name] = price

# Function to get the highest bidder
def get_highest_bidder(bid_dict):
  max_price = 0
  highest_bidder = ""
  for bidder in bid_dict:
    if bid_dict[bidder] > max_price:
      highest_bidder = bidder
      max_price = bid_dict[bidder]

  print(f"The winner is {highest_bidder} with a bid of ${max_price}.")


program_to_continue = True
while program_to_continue:
  bidder_name = input("What is your name?: ")
  bidding_price = int(input("What's your bid? $"))
  add_new_bidder(bidder_name, bidding_price)
  to_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if to_continue.lower() == "yes":
    clear()
    program_to_continue = True
  elif to_continue.lower() == "no":
    program_to_continue = False
    clear()
    get_highest_bidder(bidder_dict)
