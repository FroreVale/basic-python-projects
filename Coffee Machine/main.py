from data import MENU, resources

print("Thanks for stopping by for a Coffee! 😀")
print("Coffee Machine instructions")
print("Type 'report' to check the available resources in the machine.")
print("Type 'off' to turn off the machine. (Only for maintainers)\n")

remaining_water = resources['water']
remaining_milk = resources['milk']
remaining_coffee = resources['coffee']
available_money = 0

while True:
    user_input = input("\nWhat would you like? (espresso/latte/cappuccino) ").lower()

    if user_input == 'report':
        print(f"Water: {remaining_water}ml")
        print(f"Milk: {remaining_milk}ml")
        print(f"Coffee: {remaining_coffee}g")
        print(f"Money: ${available_money}")
    elif user_input == 'off':
        print("Turning off the machine...")
        break
    elif user_input in ['espresso', 'latte', 'cappuccino']:

        ingredients = MENU[user_input]['ingredients']
        required_water = ingredients.get('water',0)
        required_milk = ingredients.get('milk',0)
        required_coffee = ingredients.get('coffee',0)

        if (remaining_water >= required_water and remaining_milk >= required_milk and remaining_coffee >= required_coffee):
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickels = int(input("How many nickels?: "))
            pennies = int(input("How many pennies?: "))
            total_amount = (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)

            if total_amount >= MENU[user_input]["cost"]:
                remaining_coffee -= required_coffee
                remaining_milk -= required_milk
                remaining_water -= required_water
                remaining_change = round((total_amount - MENU[user_input]["cost"]), 2)
                available_money += MENU[user_input]["cost"]

                if total_amount == MENU[user_input]["cost"]:
                    print(f"You gave the exact change! Please enjoy your {user_input}")
                else:
                    print(f"Here is your ${remaining_change} in change! Please enjoy your {user_input}")

            else:
                print(f"Sorry! That's not enough money. Your ${total_amount} refunded")

        else:
            missing_resources = []
            if remaining_water < required_water:
                missing_resources.append('water')
            if remaining_coffee < required_coffee:
                missing_resources.append('coffee')
            if remaining_milk < required_milk:
                missing_resources.append('milk')
            if len(missing_resources) == 1:
                print(f"Sorry! There's not enough {missing_resources[0]} to make {user_input}")
            elif len(missing_resources) == 2:
                print(f"Sorry! There's not enough {missing_resources[0]} and {missing_resources[1]} to make {user_input}")
            else:
                print(f"Sorry! There's not enough {", ".join(missing_resources[:-1])} and {missing_resources[-1]} to make {user_input}")

    else:
        print("Please give a valid input!")

