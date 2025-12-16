# from a file containing numbers separated by comma, print the count of even numbers.

with open("practice.txt", "r") as f:
    data = f.read()
    print(data)

    num = ""
    for i in range(len(data)):
        if(data[i] == ","):
            print(int(num))
            num = ""
        else:
            num += data[i]

# Extract individual numbers
# Pass / typcasting to integer value


# Another method

count = 0
with open("practice.txt", "r") as f:
    data = f.read()

    num = data.split(",")
    for val in num:
        if(int(val) % 2 == 0):
            count +=1

print(count)

