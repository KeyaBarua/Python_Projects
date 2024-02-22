from art import logo
import math
print(logo)
def add(n1, n2):
  return n1 + n2

def sub(n1, n2):
  return n1 - n2

def mul(n1, n2):
  return n1 * n2

def div(n1, n2):
  return n1 / n2

def square_root(n1):
  return math.sqrt(n1)

def exponent(n1, n2):
  return n1 ** n2
operations = {
  '+' : add,
  '-' : sub,
  '*' : mul,
  '/' : div,
  '√' : square_root,
  '^' : exponent
}

def calculator():
  to_continue = "y"
  
  first_number = float(input("What's the first number?: "))
  next_number = ""
  for key in operations:
    print(key)
  print("⚠️  Press ALT + 251 for √")
  
  while to_continue.lower() == "y":
    oper_key = input("Pick an operation: ")
    function_to_perform = operations[oper_key]
    if oper_key == '√':
      result = function_to_perform(first_number)
      print(f"{oper_key}{first_number} = {result}")
    else:
      next_number = float(input("What's the next number?: "))
      result = function_to_perform(first_number, next_number)
      print(f"{first_number} {oper_key} {next_number} = {result}")
    to_continue = input(f"Type 'y' to continue with {result}, or type 'n' to start a new calculation: ")
    first_number = result
    if to_continue.lower() == "n":
      calculator() # Recursion

calculator()
