# # print the element of the following list using a loop.

# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# for i in nums:
#     print(i)



# # Search for a number x in this tuple using loop:

# x = 49
# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49)
# idx = 0

# for i in nums:
#     if(i == 49):
#         print("Found the number of X, which is ", idx)
#         break
#     idx += 1


# count = 1

# Q1. print numbers from 1 t to 100
# i = 1
# while i<=100:
#     print (i)
#     i +=1



# Q2. print numbers from 100 to 1
# i = 100
# while i>=1:
#     print(i)
#     i-=1 


# Q3. print the multiplication of number n.
# n = int("Enter nunber of n to print its table:")
# i = 1
# while i<=10:
#     print(n*i)
#     i += 1


# Q4. print the elements of the following list using a loop:
# num = [1,4,9,16,25,36,49,64,81,100]
# idx = 0
# while idx < len(num):
#     print(num[idx])
#     idx +=1


nums = [1,4,9,16,25,36,49,64,81,100]
x = 36
i = 0

while i < len(nums):
    if(nums[i] == x):
        print("Found at idx", i)
        break
    else:
        print("FINDING...")
    i += 1




 







