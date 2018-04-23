# add argv features to program
from sys import argv

# unpack argv variable into variables
script, input_file = argv

# define function with one argument to print contents of passed variable
def print_all(f):
        print(f.read())

# define function with one argument to go to reset the position of the passed variable
def rewind(f):
        f.seek(0)

# define function with two arguments to print a specified line
def print_a_line(line_count, f):
    print(line_count, f.readline())

# open file for writing and return file object
current_file = open(input_file)

# print whole file
print("First let's print the whole file:\n")

print_all(current_file)

# reset position of file to 0
print("Now let's rewind, kind of like a tape.")

rewind(current_file)

# print first three lines from file
print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

# current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)

# current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)

