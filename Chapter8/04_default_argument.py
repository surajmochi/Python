# Default parameter Value

"""
We can have a value as default argument in a function.
if we speficy name = "Stranger" in the line containing def, this value is used when no argument is passed.
"""


'''
def greet(name="Stranger"):
    #function body

greet() # name ll be 'Stranger' in function body(default)
greet("Harry") #name qwill be "harry" in function body (Passed)

'''

def GoodDay(name, ending = "Thank you"):
    print(f"Good Day, {name}")
    print(ending)

GoodDay("Suraj")

