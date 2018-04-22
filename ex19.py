# define function with two arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # print output to user including arguments
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

# print output to user and call function passing integers as arguments
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# print output to user, assign integers to variables
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

# call function passing variables as arguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# print output to user, call function passing results of integer math as arguments
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# print output to user, call function passing results of variable / integer math as arguments
print("Add we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
