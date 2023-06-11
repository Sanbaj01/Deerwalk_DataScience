# functions are group of statements that together performs a specific task
# it creates reusable code

# def add():
#     print(1+1)

# add() # Function invoking / calling function ? executing function
# add()

#extra information send to the function are argument

# def add(i, j): # i & j are parameter
#     print(i + j)

# add(5,7) #5, 7 are argument
# Positional argument --> executed in the order in which it was sent

# def info(fn, ln, age, balance = 0):    #default value of balance is 0.
#     print(f'hi {fn} {ln}. You are {age} years old.')
#     print(f'Your balance is {balance}')

# # info('sanbaj', 'ansari', 24)
# # info('sanbaj', 24, 'ansari')
# # # info('sanbaj', 'ansari')
# # info(fn = 'sanbaj', age = 24, ln = 'ansari') # keyword argument --> position or order of arguments does not matter
# info(fn = 'sanbaj', age = 24, ln = 'ansari', balance= 1000)


# A function with one name cal exist only once.

# def add_2(i,j):
#     print(i+j)
# def add_3(i,j,k):
#     print(i+j+k)
# def add_4(i,j,k,l):
#     print(i+j+k+l)

# a function will same name cannot exit with same name.

# def add(*args):       # variable length positional arguments = args
#     print(args)

# add()
# add(1)
# add(1,2)
# add(1,2,3)
#variable length arguments = args --> args are multiple variable
# variable length positional arguments = args

# def info(*kwargs):     #variable length keyword argument
#     print(kwargs)

# info(fn='umesh')
# info(fn='umesh', ln = 'regmi')
# info(fn='umesh', ln='regmi', age=28)


# funcitons are group of statements that together performs a specific task.
# extra information provided to the function are called arguments.
# def add():        function declaration
    #print(1+1)

# add()  --> Funciton invoking

# def add(i, j):       #i & j are parameters
    # print(i+j)

# add(1,2)    #1 & 2 are arguments

# Types of Arguments
"""
Positional Argumets
--> The value is recieved in the order, it was sent
--> If the order mismatch, the result can be different

Keyword Arguments
--> The values are sent using specific keywords
--> The order of the arguments does not matter

default arguments
--> A default value is given for the parameter
--> If no value is supplied, it takes the default value.
    If value is supplied, the value overrides the default value.


Variable length arguments
    Variable length postitional arguments (args)
    --> represented by *args
    --> can take multiple arguments and stores in tuple

    Variable length keyword argumetns
    --> represented by **kwargs
    --> can take multiple arguments and stores in dictionary

"""

# def add(i,j):
#     total = i +j
#     return total

# result = add(3,3)
# if result > 5:
#     print('awesome')

# if result < 5:
#     print('not awesome')

# write a function that takes two numbers and prints the sum of those two numbers
# write a function that takes two numbers and returns the sum of those two numbers
# write a function that takes a radius of a circle and returns the area of the circle
# write a fucntion that takes a  number and reutrns True if the number is even and returns false if the number is odd
# write a funciton that takes a  number  and returns True if the number is even and None if the number is odd
# write a  funciton that takes a string and returns the first vowel present in that string 
# write a fucntion that takes a string and returns the len of the string
# write a fucntion that takes a string and returns the reverse of that string
#write a function that takes a string and returns the total number of vowels and consonants present in that string in a dictionary.

# write a function that takes two numbers and prints the sum of those two numbers

# def sum(i,j):
#     print(i+j)

# write a function that takes two numbers and returns the sum of those two numbers
def sum(i,j):
    add = i + j
    return add

# write a function that takes a radius of a circle and returns the area of the circle
def area(radius):
    area = 3.14 * radius * radius
    return area

# write a fucntion that takes a  number and returns True if the number is even and returns false if the number is odd
def bool(num):
    if num % 2 == 0:
        return True
    else:
        return False

# write a funciton that takes a  number  and returns True if the number is even and None if the number is odd
def boolean(num):
    if num % 2 == 0:
        return True

# write a  funciton that takes a string and returns the first vowel present in that string 
# def first_vowel(*kwarg):
#     string = input('Enter string - ')
#     for i in string:
#         if 'a' in i:
#             print('a')
#             break
#         elif 'e' in i:
#             print('e')
#             break
#         elif 'i' in i:
#             print('i')
#             break
#         elif 'o' in i:
#             print('o')
#             break
#         elif 'u' in i:
#             print('u')
#             break


# write a fucntion that takes a string and returns the len of the string
# def length(*kwargs):
#     string = input('Enter a string - ')
#     return len(string)

# write a fucntion that takes a string and returns the reverse of that string
def reverse(*kwargs):
    string = input('Enter a string - ')
    reverse_string = ''
    i = -1
    while i >= -len(string):
        reverse_string = reverse_string + string[i]
        i = i -1
    return (reverse_string)
print(reverse('sanbaj'))

#write a function that takes a string and returns the total number of vowels and consonants present in that string in a dictionary.
# while True:
#     string = input('Enter a string - ')
#     vowel = 0
#     consonant = 0
#     for i in string:
#         if 'a' in i or 'e' in i or 'i' in i or 'o' in i or 'u' in i :
#             vowel = vowel + 1
#         else:
#             consonant = consonant + 1
#     print(f'There are {vowel} vowels in the string.')
#     print(f'There are {consonant} in the string.')


# print(sum(4,5))
# print(area(4))
# print(bool(5))
# print(boolean(5))
# reverse()
# first_vowel()

