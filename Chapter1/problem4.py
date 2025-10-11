# Write a python programe to print the contents of a directory using OS module, Search online for the
# function of which does that.

import os

directory_path = '/'

content = os.listdir(directory_path)

for item in content:
    print(item) 