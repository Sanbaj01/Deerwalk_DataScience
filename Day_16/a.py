# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False

# lambda n: True if n % 2 == 0 else False     #This is an anonymous function

# s = lambda x,y: x + y        # This is not a anonymous function, as it has name 's', which can be called.

# write a lambda function that takes an email address and returns the domain of the email address.
# email = input('Enter your email address - ')
# domain = lambda email: email.split('@')[1]
# print(domain(email))


# name = 'umesh regmi'
# # vowels = [i for i in name if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' ]
# vowels = [i for i in name.lower() if i in 'aeiou' ]
# print(vowels)


# name = 'umesh regmi'
# # capital = [i.capitalize() for i in name]
# # print(capital)
# print([i.capitalize() for i in name])

#########################################################################################################################
#------------Filter-----------------

# def is_even(n):
#     return True if n % 2 == 0 else False
# a = list(filter(is_even, [1,2,3,4,5,6,7,8,9,10]))
# print(a)

# a = list(filter(lambda x: True if x % 2 == 0 else False, [1,2,3,4,5,6,7,8,9,10]))   # Now this lambda is an anonymous function, as it has no name.
# print(a)

#-----------------MAP----------------
# Map tranforms or converts data
#The number of output is always equal to input, while in filter, output =< input
# a = list(map(lambda x: x**2, [1,2,3,4,5,6,7,8]))
# print(a)

# a = list(map(lambda x: True if x % 2 == 0 else False, [1,2,3,4,5,6,7,8,9,10]))   # Now this lambda is an anonymous function, as it has no name.
# print(a)


#-------------Reduce-------------------
from functools import reduce

#write a reduce program to multiply elements of a list.
multiply = reduce(lambda x,y: x*y, [1,2,3,4,5,6,7,8,9])
print(multiply)


#Exception Handling
#File Handling
#Web Scraping