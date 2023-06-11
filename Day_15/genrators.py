#generators 
#Generators creates value on the fly, which means they don't have to store values initially like list, tuple or set.
# def my_generator():
#     for i in range(5):
#         yield i
# gen = my_generator()
# print(next(gen))
# print(next(gen))


#Decorators
# def greet(fn):
#     def mfn(*args, **kwargs):
#         print('Good Morning')
#         fn(*args, **kwargs)
#         print('Thank you for using this function.')
#     return mfn
# def add(a,b):
#     print(a+b)

# @greet
# def three_multiple():
#     print(list(i for i in range(3,31,3)))
# greet(three_multiple)()

# greet(add)(2,3)

# import logging
# def log_function_call(func):
#     def decorated(*args, **kwargs):
#         logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
#         result = func(*args, **kwargs)
#         logging.info(f"{func.__name__} returned {result}")
#         return result
#     return decorated
# @log_function_call
# def my_function(a, b):
#     return a + b