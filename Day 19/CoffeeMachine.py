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

# TODO 1. Take user input
user_choice = input("What would you like? (espresso/latte/cappuccino):").lower()

if user_choice == "report":
    print(resources)

chosen_input = MENU[user_choice]

chosen_input_ingr = chosen_input["ingredients"]
user_choice_cost = chosen_input["cost"]
print(user_choice_cost)

print("Please insert coins.")
quarters = int(input("How many quarters: "))
dimes = int(input("How many dimes: "))
nickels = int(input("How many nickels: "))
pennies = int(input("How many pennies: "))


sum_coins = float((quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.10))

if user_choice_cost >= sum_coins:
    print("available")
else:
    print("Not available")

def ingredients_left(item_type):
    """Takes item type and updates resources available"""
    water_available = resources["water"]
    milk_available = resources["milk"]
    coffee_available = resources["coffee"]

    water = item_type["water"]
    milk = item_type["milk"]
    coffee = item_type["coffee"]

    water_available -= water
    milk_available -= milk
    coffee_available -= coffee

    print(f"Water left: {water_available}")
    print(f"Milk left: {milk_available}")
    print(f"Coffee left: {coffee_available}")


ingredients_left(chosen_input_ingr)
