f = open("demo.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()


f = open("demo.txt", "r")
data1 = f.readline()
print(data1)
f.close()



# With Syntax

with open("demo.txt", "r") as f:
    data = f.read()
    print(data)
# using with syntax you dont need to close the file.
with open("demo.txt", "w") as f:
    data = f.write("Hello Dost")
    print(data)




# Deleting a file
'''
using the os module
Module(like a code library) is a file written by another programmer that generally has a function we can use.


import os
os.remove(filename)
'''

