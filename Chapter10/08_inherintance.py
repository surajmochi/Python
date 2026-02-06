# Inheritance
'''
When one class(child/derived) derives the properties & Methods of another class(parent/base).
'''

"""
class car:
    ...

Class Toyota(car2)
    ...

"""

class Cisco_Router:
    Version = "7.2.1"
    @staticmethod
    def show_interface():
        print("Showing interfaces..")
    
    def show_vlans():
        print("showing VLANs..")
    

class Fortinet(Cisco_Router):
    def __init__(self, int_name, vlan_name):
        self.interfaces = int_name
        self.vlans = vlan_name


fw = Fortinet("E0/0", "VLAN10")
fw = Fortinet("E1/0", "VLAN20")

print(fw.show_interface())
print(fw.Version)


#Types of inheritance

"""

-> Single inheritance
-> Multi-level inheritance
-> Multiple Inheritance

"""

class A:
    varA = "Welcome to class a"

class B:
    varB = "Welcome to class b"

class C(A, B):
    varC = "welcome to class C"


c1 = C()

print(c1.varC)
print(c1.varB)
print(c1.varA)



