"""
    Day 3: Control flow, logical operators
"""

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))
BILL = 0

if height >= 120:
    print("You can ride the rollercoaster")
    if age <= 12:
        print("Child tickets are $5")
        BILL += 5
    elif age <= 18:
        print("Youth tickets are $7")
        BILL += 7
    # elif age >= 45 and age <= 55:
    elif 45 <= age <= 55:
        print("Midlife crisis tickets are free!")
    else:
        print("Adult tickets are $12")
        BILL += 12

    wants_photo = input("Do you want a photo? y for yes and n for no ")
    if wants_photo == "y":
        BILL += 3
    print(f"Your total bill is ${BILL}")
else:
    print("Sorry you have to grow taller before you can ride")


# Modulo operator
print(10 % 3)
print(10 % 5)

# logical operators
print(True and True)
print(True and False)

print(True or False)
print(True or True)

print(not True)