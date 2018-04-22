# add import feature to program
from sys import argv

# unpack argv variable into variables
script, filename = argv

# open file and return file object
txt = open(filename)

# print string and contents of filename
print(f"Here's your file {filename}:")
print(txt.read())

# prompt user for filename and input into variable
print("Type the filename again:")
file_again = input("> ")

# open file and return file object
txt_again = open(file_again)
# print contents of filename
print(txt_again.read())
