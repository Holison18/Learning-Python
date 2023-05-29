# Python if else statement is used for making decision.
# If a certain condition then perform a certain task else perform another task

# for example

number = int(input("Enter a number: "))

# an if statement
if number > 0:
    print("The number is positive")


# but in some cases we want to evaluate or perform another task if something goes wrong and hence
# we use the if else

number = int(input("Enter a number: "))

# if else block
if number > 0:
    print("The number is positive")
else:
    print("The number is negative")


# we can also have other conditions and hence we use the if elif and else statement
number = int(input("Enter a number: "))

# if,elif and else block
if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
else:
    print("zero")


# we can create an if statement within another if statement. This is called nested loops
number = int(input("Enter a number: "))

if number >= 0:
    if number == 0:
        print("Zero")
    else:
        print("Positive")
else:
    print('Negative')