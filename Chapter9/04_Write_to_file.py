# Writing to a file

# f = open("demo.txt", "w")
# f.write("This is a new line") # overwrites the entire file

f = open("demo.txt", "a") # if the file is not exist, a and w mode will automatically create a file with demo.txt
f.write("this is a new line\n") #adds to the line
f.close()


f = open("Sample.txt", "a")
f.write("Hello to the new Sample text file")
f.close()


f = open("demo.txt", "r+")
f.write("abc")
print(f.read())
f.close()



 



