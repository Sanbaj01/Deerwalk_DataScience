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

# class DeerwalkStudent:
#     principle_name = 'Prof. Dr. Umesh Regmi'
#     school_name = 'Bro Code Academy'
#     school_address = 'Bro Lane'

#     def __init__(self, fn, ln, a, addr):     #__init__ is constructor. A function that is run at default when an object is created.
#         self.first_name = fn
#         self.last_name = ln
#         self.age = a
#         self.address = addr
#         print(id(self))

# s = DeerwalkStudent('umesh', 'regmi', 28, 'balaju')
# print(s.principle_name) #BAD Practise never use this, as principle_name is a static variable
# print(DeerwalkStudent.principle_name)       #Good Practise -> static variable should always be called using class name not object.

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
# class DeerwalkStudent:
#     def __init__(self, fn, ln, a, addr):     #__init__ is constructor. A function that is run at default when an object is created.
#         self.first_name = fn
#         self.last_name = ln
#         self.age = a
#         self.address = addr
#         self.principle_name = 'Prof. Dr. Umesh Regmi'
#         self.school_name = 'Bro Code Academy'
#         self.school_address = 'Bro Lane'


'''
4 Features of OOP :
1. Encapsulation - The process of grouping/binding properties and behaviour of a class inside that class.
    for eg : Student_Class, Teacher_Class, Janitor_Class, all have their own properties which is set inside the class.

2. Abstraction - The process of showing necessary details and hiding the unnecessary implementation.
'''


'''
Types OF Method
* Instance Method - Method that access instance varaibles are called instance method
                    copy of instance method is created for every object
                    self should be the first parameter
                    accessed by using self inside the class and by using object name outside of the class

* Class Method
    - method that access static variables are called classmethod
    - @classmethod decorator is required
    - cls should be the first parameter
    - can be accessed by using class name both inside and outside of the class

* Static method
    - method that do not depend on either class or object are called static method
    - accessed by using class name both inside and outside of the class 
    - can be parameterless or parameterized
    - @staticmethod decorator is required
    - used for general utility function

'''

# class DeerwalkStudent:
#     principle_name = 'Prof. Dr. Umesh Regmi'
#     school_name = 'Bro Code Academy'
#     school_address = 'Bro Lane'

#     def __init__(self, fn, ln, a, addr):     #__init__ is constructor. A function that is run at default when an object is created.
#         self.first_name = fn
#         self.last_name = ln
#         self.age = a
#         self.address = addr

    # def get_full_name(self):
    #     return '{self.first_name} {self.last_name}'

    # def get_address(self):
    #     return self.get_full_name()

#     @classmethod            # used class level variable, which is static variable
#     def get_school_name(cls):
#         return DeerwalkStudent.school_name
    
#     @staticmethod
#     def print_govt_holidays():
#         print('Dashian ko masu khane bida is for 10 days.')
#         print('Tihar ko sel khane bida is for 5 days')

#     @staticmethod
#     def add(i,j):
#         return i + j    

# a = DeerwalkStudent('umesh', 'regmi', 28, 'balaju')
# a.get_full_name()

# print(DeerwalkStudent.get_school_name())

'''
#Decorator modifies the code without touching the codes by adding functionality.
Variable that can be accessed both inside and outside of the class are public variable
Variable that can be accessed only inside the class are private variable
'''

# class DeerwalkStudent:
#     __principle_name = 'Prof. Dr. Umesh Regmi'
#     __school_name = 'Bro Code Academy'
#     __school_address = 'Bro Lane'

#     def __init__(self, fn, ln, a, addr):     #__init__ is constructor. A function that is run at default when an object is created.
#         self.__first_name = fn               #using '_' before any variable, makes is private(just for convention)
#         self.__last_name = ln                # '__' before any variable, make its private and inacessible
#         self.__age = a
#         self.__address = addr
    
#     @classmethod
#     def get_principle_name(cls):
#         return cls.__principle_name

#     @classmethod
#     def set_principle_name(cls, new_name):
#         cls.__principle_name = new_name

#     def get_age(self):
#         return self.__age
    
#     def set_age(self, new_age):
#         if new_age < 0:
#             print('invalid age')
#         else :
#             self.__age = new_age

# DeerwalkStudent.principle_name
# a = DeerwalkStudent('umesh', 'regmi', 28, 'balaju')
# a.__age = -10
# print(a.__age)



#------INHERITANCE---------
# class Employee:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name

#     def get_salary(self):
#         print('I am base class get salary')

# class FullTimeEmployee(Employee):
#     def get_salary(self):                               #Here, same method is giving different output. THis is polymorfism.
#         return print('I am full time salary.')

# class PartTimeEmployee(Employee):
#     pass

# f = FullTimeEmployee('umesh', 'regmi')
# f.get_salary()

''''
Polymorphism
method overriding - same method, giving different functionalities.
-It is an exploitation of inheritance.

method overloading - a method with same name but different parameter, is method overloading.
            Python does not support method overloading, because it uses args and kwargs, which can take multiple parameters.

OPERATOR OVERLOADING 
    1 + 1 = 2
    '1' + '1' = 11
Here + is adding in one statement and concatanating in another, so this is polymorphism.                        
'''

# class Employee:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name

#     def get_salary(self):
#         print('I am base class get salary')

# class FullTimeEmployee(Employee):
#     def __init__(self, first_name, last_name, title):
#         super().__init__(first_name, last_name)
#         self.title = title

#     def get_salary(self):                               #Here, same method is giving different output. THis is polymorfism.
#         return print('I am full time salary.')

# class PartTimeEmployee(Employee):
#     pass

# f = FullTimeEmployee('umesh', 'regmi')
# f.get_salary()


'''
Create a class BankAccount
open account --> first_name, last_name, address, balance = 0
check balance() --> print current balance
deposit balance() --> takes deposit amount from user and deposit it in the account
withdrawl balance() --> takes withdrawl amount from the user and withdraw it from the BankAccount
check interest rate() --> displays the bank's current interest rate
print govt holidays --> displays government holidays list
'''








