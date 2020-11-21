from time import sleep

MENU = {
    1: {
        # espresso
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    2: {
        # latte
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },

    3: {
        # cappuccino
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
    4: {
        # mocha
        "ingredients": {
            "water": 150,
            "milk": 50,
            "coffee": 24,
            "cocoa": 150
        },
        "cost": 3.0
    }
}

resources = {
    "water": 1000,
    "milk": 1000,
    "coffee": 500,
    "cocoa": 500
}

money = 0


def coins():
    quarter = 0.25
    dimes = 0.10
    nickle = 0.05
    penny = 0.01


# TODO: 1. Print report
'''
So, the report, should return all Coffee Machine ingredients stock:
    - Water     ml
    - Milk      ml
    - Sugar     g
    - Coffee    g
    - Money     $    
'''


def report():
    for k, v in resources.items():
        if k == "water" or k == "milk":
            print(f"{k}: {v}ml")
        else:
            print(f"{k}: {v}g")
    print(f"Money: {money}$")
    print("")

# TODO: 2. Check resources Sufficient?


def is_resource_sufficient(order_ingredients):
    """Returns True when orders are successfully submitted, else return False:"""
    for item, value in order_ingredients.items():
        if value >= resources[item]:
            print(f"Not enough {item}.")
            return False

        return True


# TODO: 3. Process coins
def process_coins():
    """Returns total calculated from coins inserted: """
    print("Please insert coins:")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.10
    total += int(input("How many nickles? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total


# TODO: 4. Check transaction successful?
def is_transaction_successful(money_received, drink_cost):
    """Return True if payment is accepted, else return False:"""
    if money_received >= drink_cost:
        global money
        money += drink_cost
        change = round(money_received - drink_cost, 2)
        print(f"Your change: {change}")
        return True
    else:
        print("Sorry, not enough coins. Your coins will be refunded.")


# TODO: 5. Make coffee
def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for k, v in order_ingredients.items():
        resources[k] -= v
    print(resources)
    print(f"Enjoy your drink! ")


machine_on = True
while machine_on:

    choice = int(input('''What would you like to order?
    1. Espresso
    2. Latte
    3. Cappuccino
    4. Mocha
    5. Report 
    6. Quit

    Choose: '''))

    if choice == 5:
        print("")
        report()

    elif choice == 6:
        print("Good Bye!")
        machine_on = False

    else:
        print("")
        drink = MENU[choice]

        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

        sleep(3)
        print("""
        """)

