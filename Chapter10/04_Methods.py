# Methods are functions that belong to the object.

# Creating class
class Student:
    def __init__(self, fullname, fullmarks):
        self.name = fullname
        self.marks = fullmarks

    def welcome(self):
        print("Welcome students,", self.name)
    
    def get_marks(self):
        return self.marks


#Creating object
s1 = Student("Jatin", 100)
s1.welcome()
print(s1.get_marks())
        