# Python Basics Chapter 14:
# =========================

# 1. Introduction 

# def sqaure(a):
#     return a**2

# s = sqaure(7)
# print(s)

# s = sqaure
# print(s(7))

# print(sqaure.__name__)
# print(s.__name__)

# print(sqaure)
# print(s)

# 2. Pass Function As Argument

# def square(a):
#     return a**2

# l = [1, 2, 3, 4]

# print(list(map(square, l)))
# print(list(map(lambda a : a**2, l)))

# def my_map(function, iterable):
#     out = []
#     for item in iterable:
#         out.append(function(item))
#     return out

# def my_map(function, iterable):
    # return [function(item) for item in iterable]

# print(my_map(square, l))
# print(my_map(lambda a : a**3, l))
# 
# 3. Function Returning Function

# def outer_func():
#     def inner_func():
#         return f"Inside inner function :)"
#     return inner_func

# var = outer_func()
# print(var())

# def outer_func():
#     def inner_func():
#         return f"Inside inner function :)"
#     return inner_func()

# var = outer_func()
# print(var)

# def outer_func(msg):
#     def inner_func():
#         return f"Message from outer function : {msg}"
#     return inner_func

# var = outer_func("Welcome")
# print(var())

# 4. Closures Practice

# function returning function (closure or first class function)

# def to_power(power):
#     def calc_power(number):
#         return number ** power
#     return calc_power

# p, n = input("Enter power and number separated by space : ").split()

# func = to_power(int(p))
# print(func(int(n)))

# 5. Decorators Introduction

# Enhance the functionality of other functions
# @ (syntactic sugar) use for decorator

# def decorator_function(any_function):
#     def wrapper_function():
#         print("this is awesome function")
#         any_function()
#     return wrapper_function

# def func1():
#     print("This is function 1")

# def func2():
#     print("This is function 2")

# func1 = decorator_function(func1)
# func1()

# func2 = decorator_function(func2)
# func2()

# @decorator_function
# def func1():
#     print("This is function 1")
 
# @decorator_function
# def func2():
#     print("This is function 2")

# func1()
# func2()

# 6. Decorators Part - 2

# def decorator_function(any_function):
#     def wrapper_function(*args, **kwargs):
#         print("this is awesome function")
#         return any_function(*args, **kwargs)
#     return wrapper_function

# @decorator_function
# def func(a):
#     print(f"This is function with argument : {a}")

# @decorator_function
# def add(a, b):
#     return f"Sum : {a+b}"

# func(2)
# print(add(2, 3))

# 7. Decorators Part - 3

# from functools import wraps

# def decorator_function(any_function):
#     @wraps(any_function)
#     def wrapper_function(*args, **kwargs):
#         """this is wrapper function"""
#         print("this is awesome function")
#         return any_function(*args, **kwargs)
#     return wrapper_function

# @decorator_function
# def add(a, b):
#     """this is add function"""
#     return f"Sum : {a+b}" 

# print(add.__doc__)
# print(add.__name__)

# Structure of Decorator :

# from functools import wraps

# def outer_function(any_function):
#     @wraps(any_function)
#     def inner_function(*args, **kwargs):
#         """block of code"""
#         return any_function(*args, **kwargs)
#     return inner_function

# A decorator is a design pattern in Python that allows a user 
# to add new functionality to an existing object without 
# modifying its structure. Decorators are usually called before 
# the definition of a function you want to decorate using 
# syntactic sugar (@). 

# 8. Decorators Practice - 1

# @print_function_data

# Output :
# You are calling add function
# This function takes two numbers as arguments and return their sum
# 6

# from functools import wraps

# def print_function_data(any_function):
#     @wraps(any_function)
#     def wrapper_function(*args, **kwargs):
#         print(f"You are calling {any_function.__name__} function")
#         print(f"{any_function.__doc__}")
#         return any_function(*args, **kwargs)
#     return wrapper_function

# @print_function_data
# def add(a, b):
#     """This function takes two numbers as arguments and return their sum"""
#     return a+b

# print(add(2, 4))

# 9. Exercise - 1

# Define a decorator -

# import time

# t1 = time.time()
# print("This is line one :)")
# x = 10
# if x == 10:
#     print(f"x is equal to {x}")
# for i in range(2, x+1):
#     print(f"This is line {i} :)")
# t2 = time.time()

# t = t2 - t1
# print(round(t, 3))

# @calculate_time
# def func():
#   print("This is function")

# func()
# This function took 3 sec to run

# 10. Exercise - 1 Solution

# import time
# from functools import wraps

# def calculate_time(any_func):
#     @wraps(any_func)
#     def wrapper_func(*args, **kwargs):
#         print(f"Executing ... {any_func.__name__} function")
#         t1 = time.time()
#         returned_value = any_func(*args, **kwargs)
#         t2 = time.time()
#         print(f"This function took {round(t2-t1, 2)} seconds to run")
#         return returned_value
#     return wrapper_func

# @calculate_time
# def square(n):
#     return [i**2 for i in range(1, n+1)]

# num = int(input("Enter a number : "))
# square(num)

# 11. Decorators Practice - 2

# from functools import wraps

def allow_only_int(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if all([type(arg)==int for arg in args]):
        return func(*args, **kwargs)
        return f"Only integers are allowed :)"
    return wrapper

@allow_only_int
def add_all(*args):
    total = 0
    for i in args:
        total += i
    return total

print(add_all(1,2,3,4,5,[6,7,8,9]))
print(add_all(1,2,3,4,5))

# 12. Decorators With Arguments 

# from functools import wraps

# def allow_any_data_type(data_type):
#     def allow_any_data_type_decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             if all([type(arg)==data_type for arg in args]):
#                 return func(*args, **kwargs)
#             return f"Only {data_type} type values are allowed :)"
#         return wrapper
#     return allow_any_data_type_decorator

# @allow_any_data_type(int)
# def add_all(*args):
#     return sum(args)

# @allow_any_data_type(str)
# def join_string(*args):
#     string = ""
#     for s in args:
#         string += s
#     return string

# print(add_all(1,2,3,4,5,[6,7,8,9]))
# print(add_all(1,2,3,4,5))

# print(join_string("Anshul", "Manya"))
# print(join_string(0, "Anshul", "Manya", 1))

# from functools import wraps
# import time

# def allow_any_data_type(*myArgs):
#     def allow_any_data_type_decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             """this is a decorator with arguments."""
#             if all([type(arg) in myArgs for arg in args]):
#                 t1 = time.time()
#                 returned_value = func(*args, **kwargs)
#                 t2 = time.time()
#                 print(f"This function took {t2-t1} seconds to evaluate the sum.")
#                 return returned_value
#             return f"Only {myArgs} type values are allowed :)"
#         return wrapper
#     return allow_any_data_type_decorator

# @allow_any_data_type(int, float)
# def add_all(*args):
#     """this function takes any numbers and return their sum."""
#     return sum(args)

# print(add_all(1, 2, 3.5))
# print(add_all(1, 2, 3.5, '4'))
