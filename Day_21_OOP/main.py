# #dry principle
# '''
# OOP came due to reusability issue in procedural programming language.
# procedural and functional programming are different.
# Note - Anything seen by eyes, kept in programming are objects.
# Class is a blueprint of an object, it defines how an object should look.
# Object is an instance of a class.
# OOP is a style of writing code.
# functional is using logic and OOP is reusing features/logic.
# Method - Function used in OOP.
# dunder method / magic method - __init__
# we use Pascal naming method in class: class Student, class Vehicle, class Motor, etc
# '''
# class Student:
#     def __init__(self, fn, ln, a, addr):     #__init__ is constructor. A function that is run at default when an object is created.
#         self.first_name = fn
#         self.last_name = ln
#         self.age = a
#         self.address = addr
#         # print('umesh')

# s = Student('Samir','Ansari',24,'chabahil')       # s is a reference variable.
# # reference variable --> variable that points to an object.
# #object is created outside of class.
# print(s.first_name, s.last_name, s.age, s.address)

# s.first_name = "hari dai"
# print(s.first_name)
# del s.first_name 
# print(s.first_name)


#---DAY_22
#NOTE - self is a reference variable that points to the currently running object in the memory.
#Note - self is a reference variable that access object inside the class
# If you wanna use objects property inside class, use self and if needs to use outside, use name of object.
'''
Instance variable - variable whose values depends on the object.
accessed by using self inside the class and object name outside of the class
copy of instance variable is created for every obejct.
It is obejct-level variable

Static Variable-
varaible whose values depend on the class
accessed by using class name both inside and outside of the class
copy of static claass os created only once
it is class-level variable
'''

class DeerwalkStudent:
    principle_name = 'Prof. Dr. Umesh Regmi'
    school_name = 'Bro Code Academy'
    school_address = 'Bro Lane'

    def __init__(self, fn, ln, a, addr):     #__init__ is constructor. A function that is run at default when an object is created.
        self.first_name = fn
        self.last_name = ln
        self.age = a
        self.address = addr
        print(id(self))

s = DeerwalkStudent('umesh', 'regmi', 28, 'balaju')
# print(s.principle_name) #BAD Practise never use this, as principle_name is a static variable
print(DeerwalkStudent.principle_name)       #Good Practise -> static variable should always be called using class name not object.

# s = Student('umesh', 'regmi', 28, 'balaju')
# print(id(s))
# print('***************************************')
# a = Student('roshan', 'khadka', 32, 'nijgadh')
# print(id(a))

# s = DeerwalkStudent('umesh', 'regmi', 28, 'balaju')
# s.age = -10
# print(s.age)



#Never write does like this
#Here, static variable are created as instance varible, which means for every object instance varibles are created, which increases object size.
class DeerwalkStudent:
    def __init__(self, fn, ln, a, addr):     #__init__ is constructor. A function that is run at default when an object is created.
        self.first_name = fn
        self.last_name = ln
        self.age = a
        self.address = addr
        self.principle_name = 'Prof. Dr. Umesh Regmi'
        self.school_name = 'Bro Code Academy'
        self.school_address = 'Bro Lane'


'''
4 Features of OOP :
1. Encapsulation - The process of grouping/binding properties and behaviour of a class inside that class.
    for eg : Student_Class, Teacher_Class, Janitor_Class, all have their own properties which is set inside the class.

2. Abstraction - The process of showing necessary details and hiding the unnecessary implementation.
'''


