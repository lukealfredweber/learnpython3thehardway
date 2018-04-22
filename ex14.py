# add import feature to program
from sys import argv

# unpack argv variable into variables
script, user_name = argv

# declare / initialise prompt variable
prompt = '> '

# print format strings with embedded variables and input result into variable
print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

# print format strings with embedded variables and input result into variable
print(f"Where do you live {user_name}?")
lives = input(prompt)

# print format strings with embedded variables and input result into variable
print("What kind of computer do you have?")
computer = input(prompt)

# print format strings with embedded variables
print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
