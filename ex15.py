# Use argv to get a filename
from sys import argv

script, filename = argv

# open filename, set to variable txt
txt = open(filename)

# print string, read txt
print "Here's your file %r:" % filename
# perform read command with no parameters, using the dot operator
print txt.read()

# prompt user for a filename
print "Type the filename again:"
# assign the raw_input to file_again
file_again = raw_input("> ")
# open file_again, assign to txt_again
txt_again = open(file_again)
# read the file, print
print txt_again.read()





