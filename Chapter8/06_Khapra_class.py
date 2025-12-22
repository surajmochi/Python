'''functions in python
Block of statements that perform a specific task.
'''

'''
def func_name(param1, param2):      #function definition.
    #some work
    return val


func_name(arg1,arg2...)     # function call

'''

def calc_sum(a,b):
    return a + b

sum = calc_sum(5,6) #11
print(sum)


def print_hello():
    print("Hello")

print_hello()


# average of 3 numbers

def avg_numbers(a,b,c):
    sum = a + b + c
    avg = sum / 3
    return avg

total = avg_numbers(1,2,3)
print(total)


print("bhaikicollege", end=" ")
print("surajmochi") #end = "\n"


# sample

def cal_prod(a=4, b=3):
    print(a*b)
    return a*b

cal_prod()




"Lets Practice"

'Write a programe to print the lenght of a list (list is the parameter)'

cities = ["Delhi", "gurgaon", "Mumbai", "chennai", "pune"]
heroes = ["thor", "iron-man", "Spiderman", "batman", "Karma"]

def print_len(list):
    print(len(list))
    
print_len(cities)
print_len(heroes)



'write a program to print the element of a list in a single line.(list is the parameter)'

def print_list(list):
    for item in list:
        print(item, end= " ")
    
print_list(cities)





'WAF to find the factorial of n.(n is the parameter)'

# fact = 1
# for i in range(1, n+1):
#     fact *= i
# print(fact)

def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

cal_fact(6)

 
'write a programe to convert USD to INR'

def converter(usd_val):
    inr_val = usd_val * 90.09
    print(usd_val, "USD=", inr_val, "INR")

converter(1000)



'Homework: WAP to take the input from the user and print if the number is ODD or EVEN in a return string.'



def find_num(n):
    if (n%2 == 0):
        print("number is even")
    elif n%2 != 0:
        print("number is odd")
    
find_num(int(input("Enter any natural number: ")))

    


