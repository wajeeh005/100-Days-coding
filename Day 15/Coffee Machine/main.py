from click import option
from art import logo

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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}





def generate_report(resources,profit):
    
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")

def sufficient_resources(drink,resources):
    if drink['water']>= resources['water']:
        print('Sorry there is not enough water.')
        return False
    elif drink['milk']>= resources['milk']:
        print('Sorry there is not enough milk.')
        return False
    elif drink['coffee']>= resources['coffee']:
        print('Sorry there is not enough water.')
        return False
    return True

def process_coins():
    print("Insert Coins")
    total=int(input("How many quaters?  ")) *0.25
    total+=int(input("How many dimes?  ")) *0.10
    total+=int(input("How many nickles?  ")) *0.05
    total+=int(input("How many pennies?  ")) *0.01
    return total
    
def is_transaction_successful(money_recive,cost):
    if money_recive>=cost:
        change=round(money_recive-cost,2)
        print(f"Here is ${change} in change.")
        global profit
        profit+=cost
        return True
    print("Sorry that's not enough money. Money refunded.")
    return False


def make_coffee(drink_name,order_ingredients):
    for items in order_ingredients:
        resources[items]-=order_ingredients[items]
    print(f"Here is your {drink_name} ")

def menu():
    print("For Menu Type:   a  ")
    print("For Knowing Prices Of Drink Type :    b   ")
    print("For Order Drink  Type:    c   ")
    print("For Generating Report Type :     d   ")
    print("For Turning Off Machine Type :   e   ")
    


def coffee_shop():
    print(logo)
    global MENU
    is_on=True
    while is_on:
        option=input("For menu Type 'a' or Type What you want to do:         ").lower()
        
        if option =='a':
            menu()
        elif option =='b':
            for items in MENU:
                print(f"{items} Cost is ${MENU[items]['cost']}")
        elif option =='c':
            decision= input("What would you like? (espresso/latte/cappuccino):  ")
            drink=MENU[decision]
            if sufficient_resources(drink['ingredients'],resources):
                payment=process_coins()
                if is_transaction_successful(payment,drink['cost']):
                    make_coffee(decision,drink['ingredients'])
        elif option=="d":
            generate_report(resources,profit)
        elif option == 'e':
            is_on= False
        else:
            print("Wrong Option Try again.  ")



        
coffee_shop()
    
          


