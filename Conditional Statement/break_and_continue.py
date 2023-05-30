# The break statement is use to terminate a loop when a certain condition is met or encountered
# break statements can be used in both for and while loops

# for loop with break
print('Using break with a for loop')
n = 10
for i in range(n):
    if i==4:
        break
    print(i)

# while loop with break
print('Using a while loop with a break')

while n >= 0:
    if n==4:
        break
    print(n)
    n -= 1


# The continue statement is used to skip the current iteration.
# The flow of the program goes to the next iteration

# for example we can write code to get all the even numbers in a range of a number
value = int(input('Enter a value: '))

for i in range(value):
    if i % 2 == 0 and i != 0:
        print(i)
    else:
        continue