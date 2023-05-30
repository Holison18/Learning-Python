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

