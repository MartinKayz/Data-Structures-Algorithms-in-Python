# Keyword arguments


# Positional arguments always come before keyword arguments
def greeting(name, intro = "Good Morning"):
    print(f"{intro},  {name}")
    # print(name + " " + intro)


greeting("Good morning")

greeting("Amos")