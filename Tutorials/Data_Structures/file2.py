""" Classes """

class Student:

    name = "Mark"
    email = 'm@gmail.com'


    # Init method
    def __init__(self, my_name, my_access, my_regno):
        self.my_name = my_name
        self.my_access = my_access
        self.my_regno = my_regno

    

student1 = Student("Amos", "A94545", "S22B23/312")
student2 = Student("Tobi", "A94545", "S22B23/312")
student3 = Student("Akunda", "A94545", "S22B23/312")
student4 = Student("Seth", "A94545", "S22B23/312")

print(type(student1))





def greeting():
    print("What is your name?")