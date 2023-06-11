# write  a function in python that accepts 2 numbers and returns the maximum of those numbers.
# def maximum(i,j):
#     if i > j:
#         return i
#     else:
#         return j
## return i if i >= j else j

#######################################################################################
# write a function that takes any number of integers and returns the sum of those numbers
# def sum(*n):
#     add = 0
#     for i in n:
#         add = add + i
#     return add
# print(sum(2,3,4))

###########################################################################################
# write a function that takes any number of integers and returns the mean of those numbers.
# def mean(*n):
#     add = 0 
#     for i in n:
#         add = add + i
#     return add / len(n)
# print(mean(2,3,4,5,6,7,8))


#Write a function that takes a list of numbers and returns the multiplication of all the numbers in a list.
# def multiplication(*n):
#     multiply = 1
#     for i in n:
#         multiply = multiply * i
#     return multiply
# print(multiplication(2,3,4,5))

#Write a function that takes a string and returns the first consonant present in the string.
# def first_consonant(string):
#     vowels = ('a','e','i','o','u')
#     for i in string.lower():
#         if i not in vowels :
#             return i
# print(first_consonant('aeiousanbaj'))

"""
# def first_consonant(string):
#     vowels = ('a','e','i','o','u')
#     for i in string.lower():
#         if i != 'a' or i != 'e' or i != 'i' or i != 'o' or i !='u':
#             return i
# print(first_consonant('aeiousanbaj'))
"""
##########################################################################################################################
# Write a Python function that checks whether a passed string is a palindrome or not. NOTE: palindrome is a word that reads same backward or forward. eg: hannah, mom, eve, etc.
# def check_palindrome(string):
#     reversed_string = ''
#     reversed_string += string[::-1]
#     if reversed_string == string:
#         print('This is a palindrome string.')
#     else:
#         print('This is not a palindrome string.')
# check_palindrome('mummy')

# Write a function that takes a list of names. That funcion should capitalize each name and return it in a list.
# def capital(*names):
#     new_names = []
#     for i in names:
#         new_names.append(i.capitalize())
#     return new_names

# print(capital('sanbaj','sanjay','umesh'))



"""
def first_vowel(string):
    for i in string.lower():
        if i == 'a' or 'e' or 'i' or 'o' or 'u':
            return i
print(first_vowel('sbnanjay'))
"""



