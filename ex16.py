# add import feature to program
from sys import argv

# unpack argv variable into variables
script, filename = argv

# print strings and embedded variables
print("We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

# prompt user for input
input("?")

# open file for writing and return file object
print("Opening the file...")
target = open(filename, 'w')

# empty file
print("Truncating the file. Goodbye!")
target.truncate()

# prompt user for inputs / assign to variables
print("Now I'm going to ask you for three lines.")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

# prompt user and write variables to file
print("I'm going to write these to the file.")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# prompt user and close file
print("And finally, we close it.")
target.close
