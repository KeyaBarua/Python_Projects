from data import MENU, resources


def calculate_amount(quart, dim, nick, penn):
    """Calculates the total amount paid by adding the quarters, dimes, nickels and pennies."""
    quart *= 0.25
    dim *= 0.10
    nick *= 0.05
    penn *= 0.01
    return round(quart + dim + nick + penn, 2)


def get_change(total_paid, actual_cost):
    """Returns the change amount."""
    change = round(total_paid - actual_cost, 2)
    if change < 0.0:
        return 0
    else:
        return change


def ingredients_needed(bev):
    """Returns the amount of milk, water and coffee in the beverage."""
    if bev.lower() == "espresso":
        milk = 0
    else:
        milk = MENU[bev]["ingredients"]["milk"]
    coffee = MENU[bev]["ingredients"]["coffee"]
    water = MENU[bev]["ingredients"]["water"]
    return milk, coffee, water


def update_resources(bev):
    """Updates the resources after the beverage is made."""
    if bev.lower() == "espresso":
        milk = 0
    else:
        milk = MENU[bev]["ingredients"]["milk"]
    resources["water"] -= MENU[bev]["ingredients"]["water"]
    resources["milk"] -= milk
    resources["coffee"] -= MENU[bev]["ingredients"]["coffee"]


def display_report():
    """Displays a report of the resources and the profit."""
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${profit}")


coffee_machine_running = True
profit = 0.0
while coffee_machine_running:
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order.lower() == "espresso" or order.lower() == "latte" or order.lower() == "cappuccino":
        # Get the amount of milk, water and coffee needed.
        milk_needed, coffee_needed, water_needed = ingredients_needed(order)
        # Condition to check if the resources are sufficient.
        if (milk_needed == 0 or resources["milk"] >= milk_needed) and resources["water"] >= water_needed and resources["coffee"] >= coffee_needed:
            print("Please insert coins.")
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickels = int(input("how many nickels?: "))
            pennies = int(input("how many pennies?: "))
            # Calculate change and profit
            amount_paid = round(calculate_amount(quarters, dimes, nickels, pennies))
            cost_of_beverage = MENU[order]["price"]
            change = get_change(amount_paid, cost_of_beverage)
            # if change is negative
            if change == 0:
                print("Sorry that's not enough money. Money refunded.")
            # if change is 0 or positive
            else:
                print(f"Here is ${change} in change")
                print(f"Here is your {order} ☕. Enjoy.")
                profit += cost_of_beverage
                update_resources(order)
        # if resources are not sufficient
        else:
            if resources["water"] < water_needed:
                print("Sorry there is not enough water.")
            elif resources["milk"] < milk_needed:
                print("Sorry there is not enough milk.")
            else:
                print("Sorry there is not enough coffee.")

    elif order.lower() == "report":
        display_report()
    elif order.lower() == "off":
      coffee_machine_running = False
