"""
#Charcters     #Meaning
    'r'         open for reading(default)
    'w'         open for writing, truncating the file first.
    'x'         create a new file and open it for writing.
    'a'         open for writing, appending to the end of the file if it exists.
    'b'         binary mode
    't'         text mode(default)
    '+'         open a disk file for updating(reading and writing)

"""

# r+ read+overwrite existing data(pointer will be at start) -> No truncate

# w+ read+overwrite -> (exisiting data will be deleted) ->  truncate

# a+ read+append (pointer will be at the end) -> No truncate

