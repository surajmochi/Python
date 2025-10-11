# label the programe written in problem 4 with comments.

import os

# Speficy the directory path
directory_path = '/'

#list the content of the directory
content = os.listdir(directory_path)

#print the content of the directory
for item in content:
    print(item) 