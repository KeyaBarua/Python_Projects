from replit import clear
from art import logo
print(logo)
def add(n1, n2):
  return n1 + n2

def sub(n1, n2):
  return n1 - n2

def mul(n1, n2):
  return n1 * n2

def div(n1, n2):
  return n1 / n2

operations = {
  '+' : add,
  '-' : sub,
  '*' : mul,
  '/' : div
}

def calculator():
  to_continue = "y"
  
  first_number = float(input("What's the first number?: "))
  for key in operations:
    print(key)
  
  while to_continue.lower() == "y":
    oper_key = input("Pick an operation: ")
    next_number = float(input("What's the next number?: "))
    function_to_perform = operations[oper_key]
    result = function_to_perform(first_number, next_number)
    print(f"{first_number} {oper_key} {next_number} = {result}")
    to_continue = input(f"Type 'y' to continue with {result}, or type 'n' to start a new calculation: ")
    first_number = result
    if to_continue.lower() == "n":
      clear()
      calculator()

calculator()
