# Testing how python executes functions


"""
Syntax:

def function_name():
    body


"""



asks_name = "Martin"

print(asks_name)

def asks_name():
    name = input("Please, What is your name?")
    print(name)




print("We are starting to call the function here")
print(asks_name)
asks_name()

asks_name()

asks_name()
print("We are ending  the function calls here")


