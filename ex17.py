from sys import argv
# The command exists returns True if a file exists, based on its name in a string as an argument. 
# It returns False if not.
from os.path import exists

# Takes in Python script and two files as arguments.
script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how? 
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

# Checks if output file alaready exists.
print "Does the output file exist? %r" % exists(to_file)
print "Read, hit RETURN to continue, CTRL-C to abort."
raw_input()

# Opens the to_file and write indata to to_file.
out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done." 

# Close files. 
out_file.close()
in_file.close()

