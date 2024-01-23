print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? "))
tip_percentage = input("What percentage tip would you like to give? 10, 12 or 15? ")
people = input("How many people to split the bill? ")

tip = float(tip_percentage) / 100 * bill
total_bill = bill + tip
bill_per_person = total_bill / int(people)

final_bill = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_bill}")
