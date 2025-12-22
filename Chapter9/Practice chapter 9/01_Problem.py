# Create a new file "practice.txt" using python. add the following data in it:

'''
Hi everyone
we are learning file I/O
using java
i like programming in Java.
'''


with open("Practice.txt", "w") as f:
    f.write("Hi everyone \n we are learning file I/O \n")
    f.write("using java \n i like programming in Java ")


