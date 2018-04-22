# add argv, exists features to program
from sys import argv
from os.path import exists

# unpack argv variable into variables
script, from_file, to_file = argv

# print message to user
print(f"Copying from {from_file} to {to_file}")

# how to do both on one line?
# indata = open(from_file).read()
in_file = open(from_file)
indata = in_file.read()

# print message to user
print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue. CTRL-C to abort.")

# wait for input from user
input()

# open and write indata to out_file
out_file = open(to_file, 'w')
out_file.write(indata)

# print status to user
print("Alright, all done.")

# close files
out_file.close()
in_file.close()
