# Condtional Statements // If Else // Control Flow
grade = 65

# if grade >= 80:
#     print('you passed with distinction')
# elif grade >=60 and grade < 80:
#     print('first division')
# elif grade >= 50 and grade < 60:
#     print('second division') 
# else:
#     print('fail')

# short hand operator
age = 15
# allowed_to_vote = None

# if age > 18:
#     allowed_to_vote = True
# else:
#     allowed_to_vote = False

# ------------OR-------------
# allowed_to_vote = True if age > 18 else False

# if 1 == 1:
#     pass # when we don't know what to write / use, we use pass
# else:
#     print('else')

# take a user input and check whether that number is even or odd

# num = int(input('enter a number - '))
# if num % 2 == 0 :
#     print(f'{num} is even.')
# else:
#     print(f'{num} is odd.')

# Take two numbers from user and print the greatest number

# num1 = int(input('Enter first number : '))
# num2 = int(input('Enter second number : '))
# if num1 > num2 :
#     print(f'{num1} is greater than {num2}.')
# elif num2 > num1:
#     print(f'{num2} is greater than {num1}.')
# else:
#     print(f'{num1} is equals to {num2}')

# print(f'{num1} is greater than {num2}') if num1 > num2 else print(f'{num2} is greater than {num1}')

# ram 82, shyam 65, hari 43, gita 23
# if name in dictionary
# grade >= 80 distinction
# grade >= 60 and < 80 first division
# grade >= 50 and < 60 second division
# grade < 50 Mom's flying chappal received

grade = {'ram':82, 'shyam':65, 'hari':43, 'gita':64, 'samir':84, 'sanjay':75}
name = int(input('Enter a name - '))
if name in grade:
    if grade[name] >= 80:
        print(f'Hi {name}, you got distinction')
    elif grade[name] >=60 and grade[name] < 80 :
        print(f'Hi {name}, you got first division')
    elif grade[name] >=50 and grade[name] < 60 :
        print(f'Hi {name}, you got second division')
    elif grade[name] <50 :
        print(f'Hi {name}, you got mom flying chappal')
else:
    print('Name does not exist.')