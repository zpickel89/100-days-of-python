""" 
Pizza cost calculator
    Determine the cost depending on the inputs
    Print the final bill
"""
SMALL_PIZZA_COST = 15
MEDIUM_PIZZA_COST = 20
LARGE_PIZZA_COST = 25
SMALL_PEP_COST = 1
EXTRA_PEP_COST = 3
EXTRA_CHEESE_COST = 1

bill = 0

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")


if size == "S":
    bill += SMALL_PIZZA_COST
elif size == "M":
    bill += MEDIUM_PIZZA_COST
elif size == "L":
    bill += LARGE_PIZZA_COST
else:
    print("invalid pizza size")

if pepperoni == "Y":
    if size == "S":
        bill += SMALL_PEP_COST
    else:
        bill += EXTRA_PEP_COST

if extra_cheese == "Y":
    bill += EXTRA_CHEESE_COST

print(f"Your final bill is: {bill}.")
