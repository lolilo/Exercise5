# Write a program, lettercount.py, that opens a file named on the command line and 
# counts how many times each letter occurs in that file. 

#Your program should then print those counts to the screen, in alphabetical order. 

from sys import argv
# The command exists returns True if a file exists, based on its name in a string as an argument. 
# It returns False if not.
from os.path import exists

# Takes in Python script and one file as arguments. 
script, input_file = argv

# Check if input_file exists.
# if not exists(input_file):
#     print "%r does not exist!" % input_file
#     break

# Opens and reads input_file.
in_file = open(input_file)
indata = in_file.read()

# count = 0
# for char in indata:
#     print char
#     count += 1

# print count

# Convert all letters to lowercase.
indata = indata.lower()
# Create list of alphabet, lowercase. 
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# Create list to keep track of counts of each letter. 
# Need to replace all elements with proper numbers later.
letter_count = range(27)

# Set all elements in letter_count to number 0.
for i in range(len(letter_count)):
    # index needs to reach 27, i = 27 for the 26th element of the alphabet list
    # print i
    # print "length", len(letter_count)
    letter_count[i] = 0

# Counts how many times each letter occurs in indata.
for i in range(len(indata)): 
    
    for letter in range(len(alphabet)): 
        if indata[i] == alphabet[letter]:
            print indata[i]
            letter_count[letter] += 1

print letter_count

            

