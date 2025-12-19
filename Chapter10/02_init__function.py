# Constructor
'All classes have a function called __init__(), which is always executed when the object is being initiated'


# Creating class

'''
class Student:
    def __init__(self,fullname):
    self.name = fullname
'''

#Creating object

'''
s1.Student("Karan")
print(s1.name)
'''

"""
The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

"""


class student:
    def __init__(self, fullname): # we anyhow need to define the self argument.
        self.name = fullname
        print("Adding new student in database..")

s1 = student("Sagar")
print(s1.name)

s2 = student("Roshni")
print(s2.name)

# attributes are values associated with an object that define its characteristics or properties.


class student:
    def __init__(self, name, marks): # we anyhow need to define the self argument.
        self.name = name
        self.marks = marks
        print("Adding new student in database..")

s1 = student("Sagar", 99)
print(s1.name, s1.marks)

s2 = student("Roshni", 100)
print(s2.name, s2.marks)

