# Parameterized Functions

"""
Syntax: 

def function_name(parameter):
    body


When calling a function with a parameter, 
the data(value) is called an argument

"""

def greeting(salut, name):
    print(salut + " " +  name)



greeting("Good afternoon", "Seth")

greeting("Good night", "Isaac")

#greeting("Good morning")
#Returns an error: TypeError: greeting() missing 1 required positional argument: 'name'


greeting("Toby", "What's up")
