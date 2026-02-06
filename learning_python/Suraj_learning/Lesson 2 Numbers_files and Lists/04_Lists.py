# Lists 
my_list = ["foo", 1, "hello", [22], None, 2.7, 'new string'] # square bracket notation.
'''Creating list         Separate the elements using commans.'''
# Data types for the element of the list can very(string, integers, booleans, other lists, etc)

print(my_list[0]) #Accessing the first element(element zero)
#output: foo
#Lists are sequential....first element, second element, third element, etc.

my_list[0] = 88 # can assign new values.
print(my_list)
#output: [88, 1, 'hello', [22], None, 2.7, 'new string']

#Accessing the last element using -1 index
print(my_list[-1])
#output: new string
#You can use -1, -2, -3 to work backwords from the end of the list.

#####################################################################################################

# lenght and Range
print(len(my_list))
#output: 7

# Range generates a sequence of numbers from 0 to (n-1). Note, This exactly corresponds to the indices of list of length n.
print(list(range(10)))
#output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#################################################################################################

# List Membership
"new string" in my_list
#output = True
"Whatever" in my_list
#output = False
'''does the given element exist in the list or not(returns a boolean.)'''

# List Methods
'''
append()
clear()
copy()
count()
extend()
index()
insert()
pop()
remove()
reverse()
sort()
'''

#Append
my_list.append("Append_string")
print(my_list)
#output: [88, 1, 'hello', [22], None, 2.7, 'new string', 'Append_string']

#################################################################################################

# List Slices - Enough with the lists already.
'''list slicing is a way to create new lists from parts of an exiting list.'''

# first index is included but the second index is excluded.
print(my_list[1:3]) # list slice

# List Slices - Dynamically create new lists.
'''No first index - start at the beginning of the list.'''
print(my_list[:3])

'''No last index = go to the end of the list.'''
print(my_list[4:])

# List Slices - Can use negative indices.
print(my_list[4:-1])






