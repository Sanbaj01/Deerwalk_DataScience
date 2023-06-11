#write a function that takes two numbers and prints the sum of those two numbers
# def add(i,j):
#     print(i+j)
# add(1,2)    

#write a function that takes two numbers and returns the sum of those two numbers
# def sum(i,j):
#     add = i + j
#     return add
# print(sum(2,3))

#write a function that takes a radius of a circle and returns the area of the cirlce
# def area_circle(radius):
#     return 3.14 * radius * radius

# print(area_circle(3))

#write a function that takes a number and returns True if the number is even and returns false if the number is odd
# def is_even(num):
#     ### if num % 2 == 0:
#     ###     return True
#     ### else:
#     ###     return False
#     return num % 2 == 0
# print(is_even(13))

##############################################################################################
# write a function that takes a number and returns True if the number is even and None if the number is odd
# def is_even(num):
#     if num % 2 == 0:
#         return True

#########################################################################################
# write a function that takes a string and returns the first vowel present in that string
def first_vowel(string):
    for i in string.lower():
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i =='u':
            return i

print(first_vowel('Umesh'))

#####################################################################
# write a function that takes a string and returns the len of the string
# def length(*kwargs):
#     return len(kwargs)

# length = length('sanbaj')
# print(length)

###############################################################################
# write a function that takes a string and returns the reverse of that string 
# def reverse_string(string):
#     return string[::-1]
# print(reverse_string('sanbaj'))

#write a function that takes a string and returns the total number of vowels and consonants present in that string in a dictionary.
# def count_vowels_consonants(s):
#     vowels = 'aeiouAEIOU'
#     vowels_count = 0
#     consonants_count = 0
#     for item in s:
#         if item in vowels:
#             vowels_count = vowels_count + 1
#         else:
#             consonants_count = consonants_count +1
    
#     return {'vowels': vowels_count, 'consonants': consonants_count }

# print(count_vowels_consonants('samir'))

    