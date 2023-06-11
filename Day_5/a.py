# non-primitive data type
    #list tuple set dictionay

#Empty string
# a = []  #preffered way to create an empty list
# b = list()

# students = ['ram', 'shyam', 'hari', 'rita']

#properties of list
#list is heterogenous, because it can contain value of multiple data types
# a = [1, 1.1, True, False, 'umesh']

#Non primitive is non primitive, because it can be broken down into different data type
#List is ordered and indexed

#list is mutable
# a = [4,5,6,7,8,9]
# print (a)
# print(id(a))

# a.append(100)
# print(a)
# print(id(a))

# name = 'sanbaj'
# print ('s' in name)

# students = ['ram', 'shyam', 'hari', 'rita']
# students.append('sita')
# students.append('gita')
# print(students)

#2 ways to insert data --> append & insert
# append insert data at list's end   &&  insert inputs data to a specified position/location.

# students.insert(0, 'test')
# students.insert(2, 'gita')
# print(students)

##########################################################################3
# students = ['ram', 'shyam', 'hari', 'rita']
# students.remove('ram')
# students.remove('hari')
# students.remove('gita')
#ERROR - ValueError: list.remove(x): x not in list   (gita in not in the list)

# students.pop(1)
# students.pop(10)  #IndexError: pop index out of range
# students.pop()
# students.pop()
# students.pop()
# students.pop()  #IndexError: pop from empty list
# print(students)

# del students[0]       Thes both are same.
# students.pop(0)


# students = ['ram', 'shyam', 'hari', 'rita']
# # students.clear() #print can't be used here, cause the processing/work is happening here.
# # print(students)

# students.sort()
# print(students)


# students = ['ram', 'shyam', 'hari', 'rita']
# students.reverse()
# print(students)

# students = ['ram', 'shyam', 'hari', 'rita']
# students.sort()
# students.reverse()
# print(students)

# Merging list
# a = ['ram', 'shyam', 'hari']
# b = ['rita', 'sita', 'gita']
# print(a + b)


#Nested List
# a = [[1,2,3], [4,5,6]]
# print(a[0][0])

a = ['a', 'b', 'c', 'd']
b = ['e', 'f', 'g', 'h']
b.remove('h')
c = a + b
print (c)