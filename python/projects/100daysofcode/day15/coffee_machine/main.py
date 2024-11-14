MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def are_resource_sufficient(order_ingredients):
    """ Returns True if there are enough resources, returns false otherwise. """
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"You don't have enough {item}!")
            return False
    return True

def process_coins():
    """ Returns the total caluculated from the coins inserted """
    print("Please inset coins.")
    total = float(input("How many quarters? ")) * 0.25
    total += float(input("How many dimes? ")) * 0.1
    total += float(input("How many nickles? ")) * 0.05
    total += float(input("How many pennies? ")) * 0.01
    return round(total, 2)

def is_transaction_valid(money_received, drink_cost):
    """ Retutrns True if the payment is valid, returns false otherwise. """
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that is note enough money. Money refunded.")
        return False
    
def make_coffee(drink_name, order_ingredients):
    """ Deducts the required ingrediants from the resources """
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

def print_report():
    """Prints the current resource levels and the total profit."""
    print("Current resources:")
    for resource, amount in resources.items():
        print(f"{resource.capitalize()}: {amount}ml")
    print(f"Total profit: ${profit}")

profit = 0
on_status = True

while on_status:
    user_choice = input("What would you like? (espresso, latte, cappuccino): ").lower()

    if user_choice == "off":
        on_status = False
    elif user_choice == "report":
        print_report()
    elif user_choice in MENU:
        drink = MENU[user_choice]
        if are_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_valid(payment, drink["cost"]):
                make_coffee(user_choice, drink["ingredients"])
    else:
        print("Sorry, that is not a valid drink.")