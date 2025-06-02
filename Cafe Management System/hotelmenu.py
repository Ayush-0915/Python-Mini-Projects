#Define The menu of restaurant
menu = {
    'Pizza': 50,
    'Burger': 30,
    'Pasta': 40,
    'Sandwich': 20,
    'Salad': 25,
    'Coffee': 15,
    'Tea': 10,
}

#Greeting message
print("Welcome to  PineApple Cafe!")
print("Pizza: Rs50 \nBurger: Rs30 \nPasta: Rs40 \nSandwich: Rs20 \nSalad: Rs25 \nCoffee: Rs15 \nTea: Rs10")

order_total = 0
#15 + 10 = 25

item_1 = input("Enter the first item you want to order: ")
if item_1 in menu :
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")
    
else:
    print(f"Ordered item {item_1} is not available in the menu")
    
another_order = input("Do you want to order another item? (yes/no): ")
if another_order == "yes":
    item_2 = input("Enter the name of second item =")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to your order")
    else:
        print(f"Ordered item {item_2} is not available in the menu")

print(f"The total amount of your order is Rs{order_total}")

