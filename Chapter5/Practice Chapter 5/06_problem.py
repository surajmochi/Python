# Create an empty dictionary. allow 4 friends to enter their favorite language as value and use key as their names, assume that the names are unique.

d = {}

name = input("Enter friends name: ")
lang = input("Enter language name: ")
d.update({name:lang})

name = input("enter friends name: ")
lang = input("enter language name: ")
d.update({name:lang})

name = input("Enter friends name: ")
lang = input("Enter language name: ")
d.update({name:lang})

name = input("Enter friends name: ")
lang = input("Enter language name: ")
d.update({name:lang})

print(d.items())

