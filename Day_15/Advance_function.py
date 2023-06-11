# lambda function
# list comprehension
# filter map reduce

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

# x = lambda a : a + 10
# print(x(5))

# double = lambda x: x *2
# cube = lambda x: x * x * x
# square = lambda X: x * X
# sum = lambda x,y: x+y
# difference = lambda x,y: x-y
# average = lambda x,y,z: (x+y+z)/3
# a = lambda *args: args

# print(double(10))
# print(cube(5))
# print(average(5,6,7))
# print(a('sanbaj','samir','sanjay'))

# def cube_sum(fx, value):
#     return 6 + fx(value)
# # print(cube_sum(cube, 3))  ---OR---
# print(cube_sum(lambda x: x*x*x, 3))


##############################################################

#List Comprehension
# ls = []
# for i in range(100):
#     if i % 3 == 0:
#         ls.append(i)
# print(ls)

#Now using list comprehension
# ls = [i for i in range(100) if i % 3 == 0 ]
# print(ls)

# ls = [i for i in range(3,100,3)]

# dict = {i:f'item {i}' for i in range(1,11)}
# dict = {value: key for key,value in dict.items()}
# print(dict)
# print({value:key for key, value in dict.items()})

# dresses = {dress for dress in ['dress1','dress2','dress1','dress2','dress1','dress2']}
# print(dresses)
# print(type(dresses))
################################################################
#-------------MAP------------------
# def cube(x):
#     return x*x*x
# a = [1,2,3,4,5,6,7,8,9,23,45]
# # new_list = list(map(lambda x: x*x*x, a))
# # for i in a:
# #     new_list.append(cube(i))

# # print(new_list)
# print(list(map(lambda x: x*x*x, a)))
# newl = map(cube, a)
# print(map(lambda x: x*x*x, a)) # THis returns map object.
# So, if you need list, convert it into list by using list(...)


#----------Filter-------------------
# def filter_function(a):
#     return a>7
# a = [1,2,3,4,5,6,7,8,9,23,45]
# new_list = list (filter (filter_function, a))
# print(new_list)

# A higher order function is a function which can take another function as a parameter.
# Map Filter & Reduce are higher order functions.



#----------LIST--------
## ****NOTE****
#Reduce needs to be imported first

# from functools import reduce

# num = [1,2,3,4,5,6,7,8,9]
# print(reduce(lambda x,y: x + y, num))

##############################################################

#-------------EXERCISES------------------------
# Questions site - https://www.w3resource.com/python-exercises/map/index.php
'''
1. Write a Python program to triple all numbers in a given list of integers. Use Python map.

2. Write a Python program to add three given lists using Python map and lambda.

3. Write a Python program to listify the list of given strings individually using Python map.

4. Write a Python program to create a list containing the power of said number in bases raised to the corresponding number in the index using Python map.

5. Write a Python program to square the elements of a list using the map() function.

6. Write a Python program to convert all the characters into uppercase and lowercase and eliminate duplicate letters from a given sequence. Use the map() function.

7. Write a Python program to add two given lists and find the difference between them. Use the map() function.

8. Write a Python program to convert a given list of integers and a tuple of integers in a list of strings.

9. Write a Python program to create a new list taking specific elements from a tuple and convert a string value to an integer.

10. Write a Python program to compute the square of the first N Fibonacci numbers, using the map function and generate a list of the numbers.

11. Write a Python program to compute the sum of elements of an array of integers. Use the map() function.

12. Write a Python program to find the ratio of positive numbers, negative numbers and zeroes in an array of integers.

13. Write a Python program to count the same pair in two given lists. use map() function.

14. Write a Python program to interleave two lists into another list randomly. Use the map() function.

15. Write a Python program to split a given dictionary of lists into list of dictionaries using the map function.


16. Write a Python program to convert a given list of strings into a list of lists using the map function.

17. Write a Python program to convert a given list of tuples to a list of strings using the map function.
'''

#1. Write a Python program to triple all numbers in a given list of integers. Use Python map.

# num = [1,2,3,4,5,6]
# print(list(map(lambda x: x * 3, num)))

#2. Write a Python program to add three given lists using Python map and lambda.
# a = [1,2,4,5,6,7,88]
# b = [2,4,6,7,2,4,99]
# c = [8,23,243,45,88,77,87]
# print(list(map(lambda a,b,c: a+b+c, a, b,c)))

#3. Write a Python program to listify the list of given strings individually using Python map.
# a = ['sanbaj','ansari','samir','shrestha','bob','marley']
# print(list(map(list, a)))













# list1 = ['abcd', 'efg']
# out = list(map(list, list1))
# print(out)

# string1 = 'learning monkey'
# string2 = 'living monkey'
# x = list(string1)
# y = list(string2)
# out = set(filter(lambda z: z in x,y))
# print(out)

# from functools import reduce
# lis = [0,1,2,3,4,5]
# out = reduce(lambda x,y: x*y, lis)
# print(out)


#############################################################
#-------------LAMBDA----------
#Using a lambda function inside another function
# def my_func(n):
#     return lambda x: x * n

# doubler = my_func(2)
# print(doubler(10))

#Using lambda with python built-in functions
# my_list = [1,2,3,4,5,6]
# odd_numbers = list(filter(lambda x:x % 2 ==1, my_list))
# print(odd_numbers)

#Using lambda function for sorting
# my_list = [("apple", 50), ("banana", 10), ("cherry", 30)]
# sorted_list = sorted(my_list, key = lambda x: x[1])
# print(sorted_list)