# Write a function that replaces all occurence of "java" with "Python" in above file.

with open("Practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("Java", "Python")
print(new_data)

with open("Practice.txt", "w") as f:
    f.write(new_data)
    





