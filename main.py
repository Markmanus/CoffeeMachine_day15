from menu import MENU, resources, money

def machine(resources,money):
    machine_on = True
# TODO: 1: Prompt user by asking “What would you like? (espresso/latte/cappuccino):
    while machine_on:
        option = input("What coffee would you like to drink? espresso/latte/cappuccino\n")
        if option == "espresso" or option == "latte" or option == "cappuccino":
            print(f"Please instert £{MENU[option]['cost']}")
            if check_resources(resources,option):
                payment = check_coin()
                drink = MENU[option]
                is_transaction_succesful(payment,drink['cost'])
                ingredients = MENU[option]['ingredients']
                cost = MENU[option]['cost']
                print(f"Dispensing {option}...")
                for ingredient in ingredients:
                    resources[ingredient] -= ingredients[ingredient]
                money += cost
                print(f"Here is your {option} ☕. Enjoy!")
            else:
                print("Cannot recognise that. Please try again")
# TODO: 2: Turn off the Coffee Machine by entering “off” to the prompt.
        elif option == "report":
            report(resources,money)
        elif option == "off":
            print("Machine has been turned off")
            break

        else:
            print("cannot recognise that. Please try again")
    return machine_on

# TODO: 3: Print report.
def report(resources,money):
    print(f"Remaining Water: {resources['water']} ml")
    print(f"Remaining Milk: {resources['milk']} ml")
    print(f"Remaining Coffee: {resources['coffee']} g")
    print(f"Money : £{money} ")

# TODO: 4: Check resources sufficient?
def check_resources(resources,option):
    ingredients = MENU[option]['ingredients']
    for ingredient in ingredients:
        if resources[ingredient] < ingredients[ingredient]:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True
# TODO: 5: Process coins.
def check_coin():
    """REturns the total calculated from coins inserted"""
    print("insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total +=int(input("How many Dimes?: ")) * 0.1
    total +=int(input("How many nickles?: ")) * 0.05
    total +=int(input("How many pennies?: ")) * 0.01
    return total
    price = MENU[option]['cost']

# TODO: 6: Check transaction successful?
def is_transaction_succesful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your Change : {change}")
        global money
        money += drink_cost
        return True
    else:
        print("Not enough Money, money refunded")
        return False

machine(resources,money)
report(resources,money)





# TODO: 7: Make Coffee.