'''
Things to work on

virtual Environment
Getter & Setter
Access Modifier
Static Methods
Instance variable vs class variables
Clear the clutter
Constructors
dir, _dict_ and help method
super keyword
magic/dunder methods
method overriding
operator overloading
Inheritance - Single , Multiple, Multilevel, Hybrid & Hierarchical
Modules & Libraries - Walrus Operator , Shutil Module, Request Module
Function Caching
Regular Expressions
AsyncIO
Multithreading
Multiprocessing & Multiprocessing

'''



"""
Small Projects to work on
Library Management System
News App
Drink Water Reminder

"""


#-------Enumerate Function----------
#here, you start enumerate from any given index -- enumerate(marks, start=1)

# marks = [10,20,30,98,45,23,45]
# for index, mark in enumerate(marks, start=1):      #here, we skipped i=0, then i++ because of enumerate function.
#     print(mark)
#     if index == 3:
#         print('Sanbaj, Awesome you have the highest score.')

# import a
# a.welcome()

# from a import welcome
# welcome()
# print(__name__)
#Code With Harry
#if __name__ == "__main__" in Python | Python Tutorial - Day #45


# ####################------------    OS MODULE   ------------------########################
# import os
# print(dir(os))

#Readline & readlines

# with open('myfile.txt', 'r') as f:
#     # while True:
#     for line in f.readlines():
#     # line = f.readlines()
#       print(line.strip())


##### File Handling Commands - seek() & tell()
'''
#NOTE- seek() function allows you to move the current position within a file to a specific point.
The position is specified in bytes, and you can move either forward or backward from the current position.

tell() --> it returns the current position within the file, in bytes.

truncate() --> sets limit on number of charcters/bytes can be written in the file.
'''
# with open('file.txt', 'r') as f:
#     print(type(f))
#     f.seek(10)      #Move to the 10th byte in the file.
#     print(f.tell())
#     data = f.read(5)    #Read the next 5 bytes.
#     print(data)

# with open('abc.txt', 'a') as f:
#     f.write('Python is fun')
#     f.truncate(10)

# with open('abc.txt','r') as f:
#     print(f.read())

################################################################################
#NOTE - is VS ==

# a = 4
# b = "4"

# print(a is b)   # exact location of object in memory
# print(a == b)   # value