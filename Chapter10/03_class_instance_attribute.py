# Class & instance Attributes

'''
Class.attr
obj.attr

'''

class student:
    college_name = "S P University"
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new students in database..")
    

s1 = student("jatin", 100)
print(s1.name, s1.marks) #Jatin
print(s1.college_name)


s2 = student("Hitakshi", 100)
print(s2.name, s2.marks) #hitakshi
print(s2.college_name)
