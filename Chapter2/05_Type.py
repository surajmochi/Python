# #init for type
a = 3
t = type(a)
print(t)

# #String for type
a = "Hello"
t = type(a)
print(t)   

# #Float for type
a = 3.5
t = type(a)
print(t)

# #String to float conversion
a = "3.5"
b = float(a)
t = type(b)
print(t)



#Commented
'''
#Boolean for type
a = True
t = type(a)
print(t)

#List for type
a = [1,2,3,4]
t = type(a)
print(t)

#Tuple for type
a = (1,2,3,4)
t = type(a)
print(t)

#Dictionary for type
a = {"name":"Suraj","age":24}
t = type(a)
print(t)

#Set for type
a = {1,2,3,4}
t = type(a)
print(t)

#NoneType for type
a = None    
t = type(a)
print(t)

#Complex for type
a = 3 + 4j
t = type(a)
print(t)

#Range for type
a = range(5)
t = type(a)
print(t)

#Bytes for type
a = b"Hello"
t = type(a)
print(t)

#Bytearray for type
a = bytearray(5)
t = type(a)
print(t)   

#Frozenset for type
a = frozenset([1, 2, 3, 4])
t = type(a)
print(t)    

#Memoryview for type
a = memoryview(b"Hello")
t = type(a)
print(t)

#Function for type
def my_function():
    return "Hello"
t = type(my_function)
print(t)   

#Lambda for type
a = lambda x: x + 1
t = type(a)
print(t)

#Module for type
import math
t = type(math)
print(t)

#Class for type
class MyClass:
    pass
t = type(MyClass)
print(t)

#Object for type
obj = MyClass()
t = type(obj)
print(t)

#Exception for type
try:
    1 / 0
except ZeroDivisionError as e:
    t = type(e)
    print(t)

#Ellipsis for type
a = ...
t = type(a)
print(t)

#NotImplemented for type
a = NotImplemented
t = type(a)
print(t)



#Custom Class for type
class Custom:
    def __init__(self, value):
        self.value = value

a = Custom(5)
t = type(a)
print(t)



#Method for type
def my_method(self):
    return self.value

t = type(my_method)
print(t)

#Static Method for type
class MyStaticClass:
    @staticmethod
    def my_static_method():
        return "Hello"
t = type(MyStaticClass.my_static_method)
print(t)    

#Class Method for type
class MyClassMethod:
    @classmethod
    def my_class_method(cls):
        return "Hello"  
t = type(MyClassMethod.my_class_method)
print(t)


#Generator for type
def my_generator():
    yield 1
    yield 2
    yield 3 
gen = my_generator()
t = type(gen)
print(t)


#Coroutine for type
import asyncio
async def my_coroutine():
    await asyncio.sleep(1)
    return "Hello"
coro = my_coroutine()
t = type(coro)
print(t)


#Async Generator for type
async def my_async_generator():
    yield 1
    yield 2
    yield 3
agen = my_async_generator()
t = type(agen)
print(t)



#Traceback for type
import traceback
try:
    1 / 0
except ZeroDivisionError:
    tb = traceback.format_exc()
    t = type(tb)
    print(t)



#Frame for type
import sys
def my_frame():
    frame = sys._getframe()
    t = type(frame)
    print(t)
my_frame()


#Code for type
def my_code():
    return "Hello"
t = type(my_code)
print(t)

'''