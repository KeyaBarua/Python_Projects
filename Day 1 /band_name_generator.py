# Write a program which generates a band name.
# Greeting for the user
print("Welcome to the Band Name Generator!")

# Asking the user the city they grew up in
city = input("What is the name of your city you grew up in?\n")
# Asking the user the pet name
pet_name = input("What is the name of your pet?\n")

band_name = city + " " + pet_name
print("Your band name could be " + band_name)
