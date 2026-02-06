f = open("test_file.txt", "w")
f.write("testing..\n")
f.flush

f = open("test_file.txt", mode = "a")
f.write("Hello Again \n")
f.flush()
f.close()
