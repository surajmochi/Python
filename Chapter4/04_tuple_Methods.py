z = (1,45,342,3424, False,"Rohan", "Suraj",5,1,6,7,1,5,1,6,1)
#print(z)

no = z.count(1) # since i mentioned 1 here this will count the number of 1 in tuple and give me number
print(no)

no = z.index("Suraj") # return index value for SUraj
print(no)


# operation with tuples


tuple1 = (1,2,3,4,5,6)
tuple2 = (7,8,9,10,11)

#Concatenated
concatenated = tuple1 + tuple2
print(concatenated)


#Rpeated
My_tuple = (" a,b,c,d ")
repeated = My_tuple * 3
print(repeated)


#Membership
My_tuple10 = (1,2,3,4,5)
print( 2 in My_tuple10) #Output = 2
print( 10 in My_tuple10) #Output = 10


#Length
print(len(z)) # total lenght of the tuple
      
#Slicing will be same like String.

#Unpacking

My_tuple11 = (1, 2, 3)
a, b, c = My_tuple11
print(a, b, c)

