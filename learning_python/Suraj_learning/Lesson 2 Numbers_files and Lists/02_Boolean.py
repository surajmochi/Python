my_value = None

val1 = False
val2 = True

if val1 and val2:
    print("Hello")

if val1 or val2:
    print("World")

if my_value is None:
    print("Whatever")

'''
my_var = True
type(my_var)
#bool

my_var2 = False
type(my_var2)
#bool

'''

"""
my_var1 = True
my_var2 = True

my_var1 and my_var2
#True

"""

# Truish
'''What happen if we use non-boolean as a conditional statement?'''

if "some string":
    print("Hello")

if 22:
    print("Hello")
