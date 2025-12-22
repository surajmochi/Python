"""
Break & Continue

Break: Used to terminate the loop when encountered.
Continue : Terminates execution in the current iteraion & continues execution of the loop with the next iteration.

"""

# Break the loop if condition is matched

# for i  in range(0,54):
#     if(i == 34):
#         break # Exit hte loop right now
#     print(i)


# Skip the iteration if condition is matches in Assigment statment.

# for i in range(100):
#     if(i == 10):
#         continue # Skip this iteration right now.
#     print(i)



# i  = 1
# while i <= 5:
#     print(i)
#     if (i==3):
#         break # Terminate
#     i += 1


# i = 0
# while i <= 5:
#     if (i==3):
#         i += 1
#         continue #skip
#     print(i)
#     i += 1

# odd/ Even

i = 1
while i <= 10:
    if(i%2 != 0):
        i += 1
        continue# skip
    print(i)
    i += 1

  