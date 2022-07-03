from secrets import choice
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



menu=Menu()
coffee_maker=CoffeeMaker()
money_machine=MoneyMachine()

is_on=True
while is_on:
    option=menu.get_items()
    decision=input(f"What would you like?    ({option}):  ")
    if decision=='off':
        is_on=False
    elif decision=='report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink=menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
