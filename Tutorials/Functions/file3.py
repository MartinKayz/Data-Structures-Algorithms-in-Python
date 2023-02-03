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
def introduction(first_name="Martin", last_name="Kubona"):
    print(f"Hello my name is {first_name} {last_name}")

introduction(last_name="Kabiriti", first_name="Amos")

introduction(first_name="Diana", last_name="Clarissa")

