import coffee_data
profit=0
resources={
    "water":500,
    "milk":200,
    "coffee":100,
    "ice":50,
}
def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True
def process_coins():
    type_of_payment=input("Would u like to pay on online or not(yes/no):")
    total=0
    if type_of_payment=="yes":
        amount=int(input("Enter the money:"))
        total=amount
        return total
    else:
        print("Please insert coins:")
        coins_five=int(input("How many 5rs coins?:"))
        coins_ten = int(input("How many 10rs coins?:"))
        coins_twenty = int(input("How many 20rs coins?:"))
        total=coins_five*5 + coins_ten*10 + coins_twenty*20
        return total
def is_payment_successful(money_received,coffee_cost):
    if money_received>=coffee_cost:
        global profit
        profit+=coffee_cost
        change=money_received-coffee_cost
        print(f"Here is your Rs{change} in change")
        return True
    else:
        print("Sorry that's not enough money.Money refunded")
        return False
def make_coffee(coffee_name,coffee_ingredients):
    for item in coffee_ingredients:
        resources[item]-=coffee_ingredients[item]
    print(f"Here is your {coffee_name} ...Enjoy!!")
is_on=True
while is_on==True:
    print("The list of items present are:")
    print(coffee_data.Menu)
    choice=input("What would you like to have?:")
    if choice=="off":
        is_on=False
    elif choice=="report":
        print(f"Water={resources['water']}ml")
        print(f"Milk={resources['milk']}ml")
        print(f"Coffee={resources['coffee']}g")
        print(f"Money=Rs{profit}")
    else:
        coffee_type=coffee_data.Menu[choice]
        print(coffee_type)
        if check_resources(coffee_type['ingredients']):
            payment=process_coins()
            if is_payment_successful(payment,coffee_type['cost']):
                make_coffee(choice,coffee_type['ingredients'])
