"""
Day 2

    Data types
    Type conversions
    Type errors
    
"""
#Subscripting prints last letter with -1 index
print("Hello"[-1])

#String concat
print("123" + "456")

#Underscores automatically removed, can be used to make numbers more readable
print(123_456)

#String length function
len("12345")

#Type function will return the data type of the parameter
print(type("12345"))
print(type(True))
print(type(12345))
print(type(1234.56))

#Type conversion to int using int(*) function
print(int("123") + int("456"))
print(int(True))
print(int(False))


def get_name_length():
    """ Get length of input name """

    user_name = input("Enter your name")
    name_length = len(user_name)
    print("Number of letters in your name" + str(name_length))

    # or single line
    print("Number of letters in your name: " + str(len(input("Enter your name"))))

#get_name_length()


#f-strings
SCORE = 1
print(f"Your score is = {SCORE}")