# listdir(path)
# Return a list containing the names of the entries in the directory given by path. 

# chdir(path)
# Change the current working directory to "path".

# os.path.exists(path)
# Return True if "path" refers to an existing path. False otherwise.

# shutil.move(src, dst)
# Recursively move a file or directory (src) to another location (dsf). 
# Destination directory must not already exist. 

import os

# 1. Create 26 directories in the current directory, one for each letter of the alphabet:
#     ./a/
#     ./b/
#     ./c/
#     etc.


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for letter in alphabet: 
    directory = letter

    if not os.path.exists(directory):
        os.makedirs(directory)



