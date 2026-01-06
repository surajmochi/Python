# Private (like) attributes & methods
# Conceptual implementation in python
'''
Private attributes & methods are meant to be used only within the class and are not accessible from outside the class. 
'''

class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass # __acc_pass which we have privatized under this class Account. 

    def reset_pass(self):
        print(self.__acc_pass)
    

acc1 = Account("12345", "abcde")

print(acc1.acc_no)

"""
XOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOX
"""

class Person:
    __name = "Anonymous"

    def _hello(self):
        print("Hello Person")

    def welcome(self):
        self.__hello()

p1 = Person()

print(p1.welcome())


