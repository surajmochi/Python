# write a python function to print n lines of the following pattern.

"""
***
**
*

- for n = 3
"""


# def pattern(n):
#     if n == 0:
#         return
#     print("*" * n)
#     pattern(n-1)

# pattern(100)


def suraj(s):
    if (s==0):
        return
    print("$" * s)
    suraj(s-1)

suraj(50)
