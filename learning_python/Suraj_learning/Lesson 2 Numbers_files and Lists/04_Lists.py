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


###############################################################################################

#Multi- Dimension list
Roshu_list = [[22, 18,72], ["Hello", "World"]]
print(Roshu_list)

print(Roshu_list[0][2])
print(Roshu_list[1][1])

#############################################################################################

# Mutable and immutabl objects in python
# How to think about variables and names in python?

rtr1_addr                                        = "10.250.1.1"
" name that refers to the object in memory."      "Object in memory"

gw1 = rtr1_addr
# Retrieving the uniqe identifier for an object.
print(id(gw1))


if rtr1_addr is gw1:
    print("True")


##############################################################################################

# Immutable objects - things that cannot change.
ssh_timeout = 20
print(id(ssh_timeout))

# New Assignment
ssh_timeout = 10
print(id(ssh_timeout))
'''We are not actually changing the object(the thing in memory). we are just pointing to a new thing(a new memory location.)'''

ssh_timeout += 1
print(id(ssh_timeout))
"Incrementing/decrementing doesn't change this. this is still a new assignment."

# Immutable objects - what are some example of immutable objects.
'''
None
Booleans(True/False)
String
Integers
Floats
'''

#So if these are immutable objects, what are some mutable objects?
'''
Lists
Dictionaries
Sets
'''

#List - Everthing changes and nothing remains still" - Heraclitus

Data_Centers = ["sf1", "sf2", "la1", "la2", "denver", "Dallas"]
id(Data_Centers)

Data_Centers.append("NY1")
print(Data_Centers)

# Copying mutable objects
my_dcs = Data_Centers.copy() # Creating a shallow copy
my_dcs.append("Dungarpur")
print(my_dcs)

my_dcs[-1] = "Mexico"
print(my_dcs)
print(Data_Centers)

#############################################################################

# Shallow Copy Vs Deep Copy

#########################################################################

# Tuple - An immutable object

my_tuple = (1,"hello", 22, None, 2.7)
type(my_tuple)
#output = tuple

my_tuple[2]
#output = 22
"We cannot assign new values in tuple like in list(Also cannot append(), extend(), pop())"

# Tuple gotcha
ip_addresses = ("10.1.1.1", "10.1.1.2") # Standard form

ip_addresses = "10.1.1.1", "10.1.1.2" # you can also create tuple like this
type(ip_addresses)
#output = tuple

##################################################################################

# Exercises

'''1.  Create a base address variable of "192.168.254.". Prompt a user to enter a subnet prefix length from between 25 to 30 (i.e. the netmask length of the subnets). Save this input as an integer.

From the entered subnet prefix length, calculate the size of the subnet (the number of total IP addresses in the subnet). Once we know the subnet size, we can calculate the number of hosts allowed in the subnet (subtract off the network number and broadcast address).

Also calculate and print out the network number for the first two subnets using the base address specified above.

Your program should print out the following:

    The number of hosts in the subnet.
    The network number of the first two subnets.
    Both the first and last host address in the first subnet.
'''

# base address
base_address = "192.168.254."

# Ask user for subnet prefix
prefix = int(input("Enter the prrfix lenght (25-30): "))

# Validate the input
if prefix < 25 or prefix > 30:
    print("Invalid prefix lenght, Must be between 25 and 30.")
    exit()

# Calculate subnet size
host_bits = 32 - prefix
subnet_size = 2 ** host_bits

#Calculate the number of usable hosts
usable_hosts = subnet_size -2

# first two subnet netwok numbers
first_subnet_network = base_address + "0"
second_subnet_network = base_address + str(subnet_size)

#first subnet host range
first_host = base_address + "1"
least_host = base_address + str(subnet_size -2)

#output results
print("\nResults:")
print(f"NUmber of usable hosts per subnet: {usable_hosts}")
print(f"First subnet network address: {first_subnet_network}")
print(f"Second subnet network address: {second_subnet_network}")
print(f"first host in first subnet: {first_host}")
print(f"last host in first subnet: {least_host}")








