"""
    Print whether the number is odd or even
"""
def is_odd(number):
    return number % 2 > 0

print(is_odd(1))
print(is_odd(2))

number = int(input("what number do you want to check? "))
result = is_odd(number)

if(result):
    print(f"{number} is odd")
else:
    print(f"{number} is even")