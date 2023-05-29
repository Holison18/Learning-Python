# in Python a for loop is used to iterate over a sequence, list, tuples etc

# example

"""
    syntax:
    for val in sequence:
        statement(s)
"""

myDetails = ['Kwame',25,'Computer Engineering','L300']

for detail in myDetails:
    print(detail)

# looping through a string

name = "Kobina "

for letter in name:
    if letter != " ":
        print(letter)

# using the range function

values = range(3)

for i in values:
    print(i)

# in a situation whereby we won't use the items of the loop we can use the '_' operator
# for example
for _ in name:
    print('Hello World!')