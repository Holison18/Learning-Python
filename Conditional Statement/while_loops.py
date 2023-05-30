# Python while loops are use to perform a task over and over again until a condition is false
'''
    syntax:
    while condition:
        statement(s)
'''

# basic example
n = 1

while n <= 5:
    print('Hello World!')
    n+=1


# a simple while loop to add numbers whiles the user provides input
isRun = True
Total = 0
while isRun:
    num1 = int(input('Enter a number: '))
    Total += num1
    ask = input("Do you want to add another number? y/n: ")
    if ask == 'y':
        continue
    else:
        isRun == False
        break
print(f"Total: {Total}")


# in python we while loops can have an addition else block. This means that when the condition
# Evaluates to false, the else block is run

num2 = 0
while num2 < 3:
    print(num2)
    num2 += 1
else:
    print('Loop has terminated')



# The else block will not execute if the while loop is terminated by a break statement
counter = 0

while counter < 3:
    '''Copied from programiz'''
    # loop ends because of break
    # the else part is not executed 
    if counter == 1:
        break

    print('Inside loop')
    counter = counter + 1
else:
    print('Inside else')
