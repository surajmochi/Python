# Loops in python
# Sometimes we want to repeat a set of statements in our program, for instace: print 1 to 1000.
# Loops make it easy for a programmer to tell the computer which set of instructions to repeat and how!

# Loops are used for sequential traversal, for traversing list, string, tuple etc.

# print(1)
# print(2)
# print(3)
# print(4)
# print(5)

# for i in range(1,9):
#     print(i)
    


str = "surukishaadi"

for char in str:
    if (char == "k"):
        print("k found")
        break
    print(char)

print("END")
