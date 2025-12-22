'Pass statment : Pass is a null statement that does nothing, it is used as a placeholder for future code'

# for i in range(5):
#     pass # this will just skip the for loop and move to the next statement
# print("some useful work")

# i = 0
# while(i<45):
#     print(i)
#     i +=1


'WAP to print total of number of sum using while and for loop'

# Using While loop
n = 6
sum = 0
i = 1
while i<=n:
    sum += i
    i += 1

# Using for loop
n = 6
sum = 0
for i in range(1, n+1):
    sum += i

print("total sum", sum)


'WAP to find the factorial of first n numbers.(using for)'

n = 7
fact = 1
i = 1

while i <= n:
    fact *= i
    i += 1
print("factorial=", fact)




