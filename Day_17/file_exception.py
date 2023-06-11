'''
run time error
programs starts but for some values, it crashes.
'''

# while True:
#     first_number = int(input('Enter first number - '))
#     second_number = int(input('Enter second number - '))
#     print(first_number/second_number)

#it crashes if second_number is zero, which gives infinity and code crashes

while True:
    try:
        #risky code
        #code that can throw errors
        first_number = int(input('Enter first number - '))
        second_number = int(input('Enter second number - '))
        print(first_number/second_number)
        # pass
    except ZeroDivisionError:
        print('second number cannot be 0')
    except ValueError:
        print('Please input only numbers')
    except Exception as e:
        #code to run when there is error
        print(type(e))