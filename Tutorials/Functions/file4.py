# Keyword arguments

# name =  "Amos"
# print(name)
# name = "Kabiriti"
# print(name)

# Positional arguments always come before keyword arguments
def greeting(name = "Martin", intro = "Good Morning"):
    print(f"{intro},  {name}")
   

# greeting()
# Key word arguments are defined by virtue of their names
def introduction(hey, first_name="Martin", last_name="Kubona", intro = "Good morning", salut="Have a good day"):
    # pass
    # print(f"{intro} Hello my name is {first_name} {last_name} {hey}")

# introduction(last_name="Kabiriti", first_name="Amos")

# introduction(first_name="Diana", last_name="Clarissa")


# introduction("Hey", intro="Good afternoon", last_name="Toby", first_name="Diana")
