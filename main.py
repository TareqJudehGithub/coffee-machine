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
    "cocoa": 100
}

money = 0

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


def coins():
    quarter = 0.25
    dimes = 0.10
    nickle = 0.05
    penny = 0.01


order = input('''What would you like to order?/n 
1. Espresso
2. Latte
3. Cappuccino
4. Mocha

''').lower()

if order == "report":
    report()

# TODO: 2. Check resources Sufficient?
# TODO: 3. Process coins
# TODO: 4. Check transaction successful?
# TODO: 5. Make coffee

