#Collection of values that never changes --> Tuple
# Tuple is faster than list
 
# a = ()
# b = tuple()

# print(type(a))
# print(type(b))

# a = (1, 1.1, True, 'Umesh')   heterogeneous --> can contain different data types
# print(a)

# a = ('sun', 'mon', 'tues', 'wed', 'thrus', 'frid', 'sat')
# print(a[0])
# print(a[5])
# print(a[::2])

# throws error since tuple is immutable
# a[0] = 'UmeshDay'
# del a[0]

# a = (1)    this is not tuple, cause the parenethesis does not have any meaning
# a = (1,)   Now, this is a tuple

# a = ('sun', 'mon', 'tues')
# b= ('wed', 'thrus', 'frid', 'sat')
# print(a + b)


#  Set is a collection of distincted elements, it does not allows repeatation of values

# a = set()
# print(type(a))

# a = {1, 2, 3, 4, 5, 6, 7,7,7,7,7, 8,8,8,8,8, 9,9,9,9,9,}
# print(a)

# a = {'ram', 'shyam', 'hari', 'rita', 'sita'}   Set is unordered & unindexed
# print(a)

# a = {1, 2, 3, 4, 5, 6, 7,7,7,7,7, 8,8,8,8,8, 9,9,9,9,9,}
# print(len(a))   //9

a = {'ram', 'shyam', 'hari', 'rita', 'sita'}
# a.add('rammaya')
# print(a)

# a.remove('shyam')
# a.discard('shyama') # discard does not throws error if the value does not exist, whereas remove does
# a.clear()
# print(a)

# a = {1, 2, 3, 4,}
# b = {3, 4, 5, 6, 7 , 8}

# print(a.union(b))
# print(a.intersection(b))
# print(a.difference(b))

# a = (1, 2, 3, 4, 5, 6)
# print(list(a))
# print(set(a))

# account_type = ('checking', 'savings')
# account_type = list(account_type)
# account_type.append('naari bachat khata')
# account_type = tuple(account_type)
# print(account_type)

# account_type = ('checking', 'savings')
# temp = list(account_type)
# temp.append('nari bachat khata')
# account_type = tuple(temp)
# print(account_type)

cities = ['kathmandu', 'kathmandu', 'bhaktapur', 'pokhara', 'kathmandu', 'pokhara']
# cities = set(cities)
# print(len(cities))
#####OR#####
# print(len(set(cities)))


############################################################################################################

# num = input('Enter a number ')   Input always takes input as string
# print(type(num))

num1 = input('Enter first Number ')
num2 = input('Enter second number ')
sum = int(num1) + int(num2)
print(f'The sum of {num1} and {num2} is {sum}.')
# print('The Sum of ' + num1 + " and " + num2 + " is " + sum)