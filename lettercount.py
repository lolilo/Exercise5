# Write a program, lettercount.py, that opens a file named on the command line and 
# counts how many times each letter occurs in that file. 

#Your program should then print those counts to the screen, in alphabetical order. 

from sys import argv
# The command exists returns True if a file exists, based on its name in a string as an argument. 
# It returns False if not.
from os.path import exists

# Takes in Python script and one file as arguments. 
script, input_file = argv
Valid = True

# Check if input_file exists.
if not exists(input_file):
    print "%r does not exist!" % input_file
    Valid = False


## Use if, not while-loop
if Valid:
# Opens and reads input_file.
    in_file = open(input_file)
    indata = in_file.read()

    # Convert all letters to lowercase.
    indata = indata.lower()
    # Create list of alphabet, lowercase. 
    # alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # Create list to keep track of counts of each letter. 

    letter_count = [0] * 27
    # ^ Liz's better way. 

    # Counts how many times each letter occurs in indata.

    # for i in range(len(indata)): 
    #     for letter in range(len(alphabet)): 
    #         if indata[i] == alphabet[letter]:
    #             letter_count[letter] += 1

    # With ord(), don't need the second for-loop to iterate through the alphabet. 

    # Think of this as looking at numbers, from 97 to 122, inclusive. 
    # When you see 97, increment the counter for 97. 
    # Access the proper list index an increase the counter. 
    # For 97, it's letter_count[0] += 1,
    # For 98, it's letter_count[1] += 1, etc.

    for i in range(len(indata)):
        # Check for non-alphabetic characters; skip over those. 
        if ord(indata[i]) < 97 or ord(indata[i]) > 122:
            pass
        else: 
            # Increment the proper letter_counter element.
            letter_count[ord(indata[i]) - 97] += 1 

    for i in range(len(letter_count)):
        print letter_count[i]

    Valid = False
            

