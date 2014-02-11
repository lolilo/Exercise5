# listdir(path)
# Return a list containing the names of the entries in the directory given by path. 

# chdir(path)
# Change the current working directory to "path".

# os.path.exists(path)
# Return True if "path" refers to an existing path. False otherwise.

# shutil.move(src, dst)
# Recursively move a file or directory (src) to another location (dsf). 
# Destination directory must not already exist. 

import os, shutil

# 1. Create 26 directories in the current directory, one for each letter of the alphabet:
#     ./a/
#     ./b/
#     ./c/
#     etc.

# Could also do this with ord(). 
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for letter in alphabet: 
    directory = letter

    if not os.path.exists(directory):
        os.makedirs(directory)

# 2. Loop through all the files in the original_files directory, 
# organize each of those files into the directory that their name starts with.
# ### Example:
#     The file named 'artichoke.txt' would go into the directory 'a',
#     'bartholomew.txt' would go into 'b'.

# Need to open original_files to look at files within.

from sys import argv

# The command 'exists' returns True if a file exists, based on its name in a string as an argument. 
# It returns False if not.
from os.path import exists

# Takes in Python script and one file as arguments. 
script, input_file = argv #input_file will be a directory name
isValid = True

# Check if input_file exists.
if not exists(input_file):
    print "%r does not exist!" % input_file
    isValid = False

if isValid:
    # print os.listdir(input_file) #input_file is a string, the user-given directory

    # Iterate through a list containing the names of the entries in the input_file directory.
    for f in os.listdir(input_file):
        # ordinal_number_of_first_letter = ord(f[0]) - 97
        # print str(ord(f[0]) - 97)
        print "Moving %s to directory %s." %(f, f[0])
        # need to change directory to access f
        # os.chdir(input_file)
        # But! We still need to access the letter directory which we were originally working...
        # Placing "./" in front is safer, in case the user inputs something dangerous.
        # "./" is explicitly the current directory. "./a/" is the same as "a/" or simply "a"
        shutil.move("./" + input_file + "/" + f, f[0])
        print "Success!"



