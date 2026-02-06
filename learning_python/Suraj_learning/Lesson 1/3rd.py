# location = input("Enter data center location: ")
# l1 = location.upper().strip()
# print(l1)
# print(repr(location))

##################################################

# line = " Process board ID FAL127990LA"
# serial_no = line.split() # split will convert each word into array of string and make an indexes
# print(serial_no[3])

###############################################

# for line in str("Process board ID"):
#     print(line)


################################################

ip_addr = "10.12.17.1"
mac_addr = "0024.c4e9.48ae"
print(ip_addr + " --> " + mac_addr) # with String concatanation
print(f"{ip_addr}{" --> "}{mac_addr}") # with F string
print("{} --> {}".format(ip_addr,mac_addr))




