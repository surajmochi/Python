# Recursion is a function which calls itself repeatedly.
# it is used to directly use a mathematical formula as function.
"""
factorial(0) = 1
factorial(1) = 1
factorial(2) = 2 X 1
factorial(3) = 3 X 2 X 1
factorial(4) = 4 X 3 X 2 X 1
factorial(5) = 5 X 4 X 3 X 2 X 1

factorial(n) = n X n-1 X......3 X 2 X 1
factorial(n) = n * factorial(n-1)

"""

def factorial(n):
    if (n==1 or n==0):
        return 1
    else:
        return n * factorial(n-1)
    
n = int(input("Enter a number: "))
print(f"The factorial od this number is: {factorial(n)}")






def show(n):
    if(n==0): # basse case
        return
    print(n)
    show(n-1)

show(3)
print("END of this one here", "/n")


# write a recursive function to calculate the first the sum of first n natural numbers.

def  cal_sum(n):
    if(n==0):
        return 0 
    return cal_sum(n-1) + n

sum = cal_sum(10)
print(sum)




     

