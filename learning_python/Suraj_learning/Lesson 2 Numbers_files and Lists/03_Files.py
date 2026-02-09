#What is file


# Reading from a file
f = open("show_version.txt") #open file for reading
data = f.read() #Use the .read() method to read in the entire file as a string
f.close() # Close the file
f = open("show version.txt", mode = "r") # you can explicitly declare the mode.


# different ways of reading in the files contents.
f = open("show_version.txt")
f.readline() # read a line at a time.
f.readlines() # read all of the lines of the file into a list.
f.seek(0) # go to the begining of the file

# for line in f: #loop over the linex in a file.
#     print(line)

# f.close()

######################################################################

# Writing a file
f = open("test_file.txt", "w") # mode = write
f.write("Testing...\n") # use the .write() to send contents to the file.
f.flush() # .flush() or .close() the file to force the content to the disk.


# The write operation is destructive
f = open("test_file.txt", "w")
f.write("new message \n")
f.close()

#######################################################################

#Appending to the end of the file.
f = open("test_file.txt", mode = "a")
f.write("Hello Again \n")
f.flush()
f.close()
