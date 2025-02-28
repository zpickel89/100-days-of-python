"""
tip calculator exercise
"""

print("Welcome to the tip calculator")
total = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
diners = int(input("how many people to split the bill? "))

per_person = round(total * (tip / 100 + 1) / diners, 2)

print(f"Each person should pay: ${str(per_person)}")