# define and initialise variables
types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

# print variables
print(x)
print(y)

# print format strings with embedded variables
print(f"I said: {x}")
print(f"I also said: '{y}'")

# define and initialise variables
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

# print format string
print(joke_evaluation.format(hilarious))

# define and initialise variables
w = "This is the left side of "
e = "a string with a right side."

# print strings concatenated
print(w + e)
