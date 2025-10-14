marks = {
    "Suraj" : 100,
    "Roshni" : 200,
    "Sagar" : 150,
    "Viraj" : 300,
    "list" : [1,2,3]
}

print(marks.items())
# output = dict_items([('Suraj', 100), ('Roshni', 200), ('Sagar', 150), ('Viraj', 300), ('list', [1, 2, 3])])
# this will give the output in list in  tuple.

print(marks.keys())
# output = dict_keys(['Suraj', 'Roshni', 'Sagar', 'Viraj', 'list'])
# this will give only keys.

print(marks.values())
# output = dict_values([100, 200, 150, 300, [1, 2, 3]])
# this will only give values.

marks.update({"Suraj" : 200, "Roshni" : 300})
print(marks)
# print updated given values.

"marks.pop method can also be used."

#Return the value of specified keys(and value is returned eg. "harry is returned here").
print(marks.get("Harry2")) # Prints None
print(marks["Harry2"]) # Returns an error.



