# Write a program to print the following star pattern.

"""
for n = 3

  *
 ***
*****

if n = 4 then we would have to start with three spaces for the first star.

"""

n = int(input("Enter the number: "))
for i in range(1, n+1):
    print("  "* (n-1),end="")
    print("*"* (2*i-1), end="")
    print("")



