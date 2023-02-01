# Parameterized Functions

"""
Syntax: 

def function_name(parameter):
    body


When calling a function with a parameter, 
the data(value) is called an argument

"""
# Keyword arguments

def introduction(first_name="Martin", last_name="Kubona"):
    print(first_name + " " +  last_name)


# Calling without arguments
introduction()

# Replacing default arguments
introduction("Isaac", "Nsubuga")

# Supplying one value
introduction("Toby")

