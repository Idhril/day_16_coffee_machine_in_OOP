from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
coffee_machine = CoffeeMaker()
coin_collector = MoneyMachine()
MENU = Menu()

while is_on:
    order = input(f"What would you like to drink? ({MENU.get_items()}): ")
    if order == 'off':
        is_on = False
    elif order == 'report':
        coffee_machine.report()
        coin_collector.report()
    else:
        user_order = MENU.find_drink(order)
        if coffee_machine.is_resource_sufficient(user_order) and coin_collector.make_payment(user_order.cost):
            coffee_machine.make_coffee(user_order)
